import cv2
import numpy as np


def letterbox(
    im: np.ndarray,
    new_shape: int | tuple[int, int],
    color=(114, 114, 114),
    auto=False,
    scale_fill=False,
    scale_up=True,
    stride=32,
):
    """
    Resize and pad image while meeting stride-multiple constraints
    Returns:
        im (array): (height, width, 3)
        ratio (array): [w_ratio, h_ratio]
        (dw, dh) (array): [w_padding h_padding]
    """
    shape = im.shape[:2]  # current shape [height, width]
    if isinstance(new_shape, int):  # [h_rect, w_rect]
        new_shape = (new_shape, new_shape)

    # Scale ratio (new / old)
    r = min(new_shape[0] / shape[0], new_shape[1] / shape[1])
    if not scale_up:  # only scale down, do not scale up (for better val mAP)
        r = min(r, 1.0)

    # Compute padding
    ratio = r, r  # wh ratios
    new_unpad = int(round(shape[1] * r)), int(round(shape[0] * r))  # w h
    dw, dh = (
        new_shape[1] - new_unpad[0],
        new_shape[0] - new_unpad[1],
    )  # wh padding

    if auto:  # minimum rectangle
        dw, dh = np.mod(dw, stride), np.mod(dh, stride)  # wh padding
    elif scale_fill:  # stretch
        dw, dh = 0.0, 0.0
        new_unpad = (new_shape[1], new_shape[0])  # [w h]
        ratio = (
            new_shape[1] / shape[1],
            new_shape[0] / shape[0],
        )  # [w_ratio, h_ratio]

    dw /= 2  # divide padding into 2 sides
    dh /= 2
    if shape[::-1] != new_unpad:  # resize
        im = cv2.resize(im, new_unpad, interpolation=cv2.INTER_LINEAR)
    top, bottom = int(round(dh - 0.1)), int(round(dh + 0.1))
    left, right = int(round(dw - 0.1)), int(round(dw + 0.1))
    im = cv2.copyMakeBorder(
        im, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color
    )
    return im, ratio, (dw, dh)


def rescale_coords(
    boxes: np.ndarray,
    image_shape: tuple[int, int],
    input_shape: tuple[int, int],
):
    """Rescale bounding boxes to the original image shape."""
    image_height, image_width = image_shape
    input_height, input_width = input_shape

    scale = min(input_width / image_width, input_height / image_height)

    pad_w = (input_width - image_width * scale) / 2
    pad_h = (input_height - image_height * scale) / 2

    boxes[:, [0, 2]] = (boxes[:, [0, 2]] - pad_w) / scale
    boxes[:, [1, 3]] = (boxes[:, [1, 3]] - pad_h) / scale

    boxes[:, [0, 2]] = np.clip(boxes[:, [0, 2]], 0, image_width)
    boxes[:, [1, 3]] = np.clip(boxes[:, [1, 3]], 0, image_height)
    return boxes.astype(int)


def preprocess(
    image: np.ndarray,
    input_shape: tuple[int, int],
):
    """YOLOv10 preprocess."""
    # Resize
    input_img = letterbox(image, input_shape)[0]
    # Transpose
    input_img = input_img[..., ::-1].transpose(2, 0, 1)
    # Expand
    input_img = input_img[np.newaxis, :, :, :].astype(np.float32)
    # Contiguous
    input_img = np.ascontiguousarray(input_img)
    # Norm
    blob = input_img / 255.0
    return blob


def postprocess(
    outs: np.ndarray,
    conf_thres: float,
    image_shape: tuple[int, int],
    input_shape: tuple[int, int],
):
    """YOLOv10 postprocess."""
    # Filtered by conf
    outs = outs[outs[:, 4] >= conf_thres]

    # Extract
    boxes = outs[:, :4]
    scores = outs[:, -2]
    labels = outs[:, -1].astype(int)

    # Rescale
    boxes = rescale_coords(boxes, image_shape, input_shape)
    return boxes, scores, labels
