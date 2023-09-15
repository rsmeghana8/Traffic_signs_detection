from src import logger
from src.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.pipeline.stage_02_training import TrainingPipeline
from src.pipeline.stage_03_evaluation import EvaluationPipeline


#STAGE_NAME="Data Ingestion"
#try:
#    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
#    data_ingestion = DataIngestionPipeline()
#    data_ingestion.main()
#    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<")   
#except Exception as e:
#    logger.exception(e)
#    raise e

STAGE_NAME="Training"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = TrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<")   
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME= "Evaluation"

try:
    logger.info(f"***************************************************")
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e 
