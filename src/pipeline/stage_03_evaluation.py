from src.config.configuration import ConfigurationManager
from src.components.evaluation import Evaluation
from src import logger 

STAGE_NAME = "Evaluation"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_eval_config()
        model = Evaluation(config=eval_config)
        model.eval()

if __name__=="__main__":

    try:
        logger.info(f"***************************************************")
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e