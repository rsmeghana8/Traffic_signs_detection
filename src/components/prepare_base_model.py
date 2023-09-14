from ultralytics import YOLO

class PrepareBaseModel:
    def __init__(self):
        pass

    def get_base_model(self):
        model = YOLO("yolov8n.yaml", )
        return model