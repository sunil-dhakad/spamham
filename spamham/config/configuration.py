import os,sys
from spamham.logger import logging
from spamham.exception import CustomException
from spamham.constant import *
from spamham.entity.config_entity import DataIngestionConfig 
from spamham.utils.utils import read_yalm_function
from spamham.utils.utils import create_dir



try:
    pass
except Exception as e:
    raise CustomException(e,sys)



class Configuration:

    def __init__(self,config_file_path:str=CONFIG_FILE_PATH):
        try:
            self.config_info = read_yalm_function(file_path=config_file_path)
        except Exception as e:
            raise CustomException(e,sys)
        


    def get_ingestion_config(self)->DataIngestionConfig:
        try:
             data_ingestion_config_var = self.config_info['ingestion_config']
             artifact_dir_var = self.config_info['artifacts_config']['artifact_dir']
             create_dir(artifact_dir_var)
             raw_data_dir_var = data_ingestion_config_var['raw_data_dir']
 
             download_url_var = data_ingestion_config_var['download_url']

             ingestion_config = DataIngestionConfig(
                                 download_url=download_url_var,
                                  raw_data_dir=raw_data_dir_var,)
                                  
             

             return ingestion_config
        

        except Exception as e:
            raise CustomException(e,sys)
