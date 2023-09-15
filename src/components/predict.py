from src.config.configuration import PredictConfig
from ultralytics import YOLO

class Predict:
    def __init__(self, config: PredictConfig):
        self.config = config
        
    def pred(self):
        best_model = YOLO(self.config.best_model)
        best_model.predict(source= self.config.video_path,
                           conf = self.config.conf,
                           iou= self.config.iou,
                           save= True)