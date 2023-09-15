from src.config.configuration import ConfigurationManager
from src.components.predict import Predict
from src import logger 

STAGE_NAME = "Prediction"


class PredictionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        pred_config = config.get_predict_config()
        model = Predict(config=pred_config)
        model.pred()

if __name__=="__main__":

    try:
        logger.info(f"***************************************************")
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
        obj = PredictionPipeline()
        obj.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e