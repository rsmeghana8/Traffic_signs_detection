from src.config.configuration import TrainingConfig
from src.components.prepare_base_model import PrepareBaseModel

class Training:
  def __init__(self, config: TrainingConfig):
        self.config = config

  def Train(self):
         base_model= PrepareBaseModel()
         model = base_model.get_base_model()
         print("model trained")
         model.train(data = "data.yaml",
                     epochs = self.config.params_epochs,
                     freeze = self.config.freeze,
                     name = self.config.exp_name,
                     imgsz = self.config.image_size)