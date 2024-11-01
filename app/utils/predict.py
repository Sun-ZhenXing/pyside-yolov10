import numpy as np
from ultralytics import YOLO
from ultralytics.models.yolo.detect.predict import Results

model = YOLO("models/yolo11m.pt")


def predict(img: np.ndarray):
    results: list[Results] = model.predict(img)
    result = results[0]
    img = result.plot()
    return (result.plot(),)
