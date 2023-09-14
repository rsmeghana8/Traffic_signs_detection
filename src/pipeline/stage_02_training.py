from src.config.configuration import ConfigurationManager
from src.components.training import Training
from src import logger

STAGE_NAME = "Training"

class TrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training= Training(config=training_config)
        training.Train()

if __name__=="__main__":

    try:
        logger.info(f"***************************************************")
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
        obj = TrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e
