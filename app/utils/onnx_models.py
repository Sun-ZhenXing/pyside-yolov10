from abc import ABC, abstractmethod
from os import PathLike
from typing import Iterable

import cv2
import numpy as np
from onnxruntime import InferenceSession

from app.utils.yolov10 import postprocess, preprocess

DEFAULT_PROVIDERS = ["CUDAExecutionProvider", "CPUExecutionProvider"]
DEFAULT_INPUT_SHAPE = (1280, 1280)
DEFAULT_THRESHOLD = 0.25


class OnnxModel(ABC):
    """ONNX model wrapper class."""

    def __init__(self, model_path: str | bytes | PathLike) -> None:
        self._model_path = model_path
        self._session = InferenceSession(
            model_path,
            providers=DEFAULT_PROVIDERS,
        )

    @abstractmethod
    def predict(self, *args, **kwargs) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Make predictions using the model."""


class YoloV10Model(OnnxModel):
    """YoloV10 model wrapper class."""

    def __init__(
        self,
        model_path: str | bytes | PathLike,
        labels: Iterable[str] | None = None,
        input_shape: tuple[int, int] = DEFAULT_INPUT_SHAPE,
        conf_threshold: float = DEFAULT_THRESHOLD,
    ) -> None:
        super().__init__(model_path)
        self._labels = list(labels) if labels else None
        self._input_shape = input_shape
        self._conf_threshold = conf_threshold

    def predict(
        self,
        img: np.ndarray,
        input_shape: tuple[int, int] | None = None,
        conf_threshold: float | None = None,
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Returns `(boxes, scores, labels)` from the model.

        >>> model = YoloV10Model("model.onnx")
        >>> boxes, scores, labels = model.predict(img)
        >>> for label, score, box in zip(labels, scores, boxes):
        ...     ...
        """
        input_shape = input_shape or self._input_shape
        conf_threshold = conf_threshold or self._conf_threshold
        image_shape = img.shape[0], img.shape[1]
        blob = preprocess(img, self._input_shape)
        outs = self._session.run(None, {"images": blob})[0][0]
        boxes, scores, labels = postprocess(
            outs,
            conf_threshold,
            image_shape,
            input_shape,
        )
        return boxes, scores, labels

    def draw(
        self,
        img: np.ndarray,
        labels: Iterable[str] | None = None,
    ) -> np.ndarray:
        """Draw bounding boxes on the image."""
        boxes, scores, labels = self.predict(img)
        label_names = self._labels or (list(labels) if labels else None)
        if not label_names:
            label_names = list(map(str, range(max(labels) + 1)))
        class_colors = [
            [np.random.randint(0, 255) for _ in range(3)]
            for _ in range(len(label_names))
        ]
        for label, score, box in zip(labels, scores, boxes):
            label_text = f"{label_names[label]}: {score:.2f}"
            cv2.rectangle(
                img, (box[0], box[1]), (box[2], box[3]), class_colors[label], 2
            )
            cv2.putText(
                img,
                label_text,
                (box[0], box[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 255),
                1,
            )
        return img
