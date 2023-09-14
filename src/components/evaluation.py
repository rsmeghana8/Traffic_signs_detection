from src.config.configuration import EvaluationConfig
from ultralytics import YOLO

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config
    def eval(self):
        best_model = YOLO(self.config.best_model)
        best_model.val(data = "test.yaml")
