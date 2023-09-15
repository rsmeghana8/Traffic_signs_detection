from src.constants import *
from src.utils.common import read_yaml,create_directories
from src.entity.config_entity import DataIngestionConfig, TrainingConfig ,EvaluationConfig, PredictConfig



class ConfigurationManager:
    def __init__(
            self,
            config_filepath= CONFIG_FILE_PATH,
            params_filepath= PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)-> DataIngestionConfig:
            config = self.config.data_ingestions
            params = self.params
            
            create_directories([config.root_dir])

            data_ingestion_config = DataIngestionConfig(
                root_dir= config.root_dir,
                    source_dir= config.source_dir,
                    train_images= config.train_images,
                    test_images= config.test_images,
                    val_images= config.val_images,
                    train_labels= config.train_labels,
                    test_labels= config.test_labels,
                    val_labels= config.val_labels,
                    train_test_split = params.TRAIN_TEST_SPLIT,
                    train_val_split= params.TRAIN_VAL_SPLIT
            )

            return data_ingestion_config
  
    
    def get_training_config(self)-> TrainingConfig:

        config = self.config.Training
        training_config = TrainingConfig(

            params_epochs= self.params.EPOCHS,
            exp_name = config.experiment_name,
            image_size = self.params.IMAGE_SIZE,
            freeze = self.params.FREEZE_LAYERS
        )
        return training_config
    

    def get_eval_config(self)-> EvaluationConfig:

        config = self.config.evaluation

        eval_config = EvaluationConfig(

            best_model = Path(config.runs)/ config.exp_name / config.best

        )
        return eval_config
    

    def get_predict_config(self)-> PredictConfig:

        config_eval = self.config.evaluation
        config = self.config.prediction


        predict_config = PredictConfig(

            video_path= config.video_path,
            best_model = Path(config_eval.runs)/ config_eval.exp_name / config_eval.best ,
            conf = self.params.CONF,
            iou = self.params.IOU

        )
        return predict_config