import os,sys
import pandas as pd 
import numpy as np
from spamham.exception import CustomException
from spamham.logger import logging
from spamham.config.configuration import Configuration
from spamham.entity.config_entity import DataIngestionConfig
from spamham.constant import *
import urllib
import requests
from spamham.utils.utils import create_dir


class Ingestionclass:
    def __init__(self,ingestion_configuration_class_var = Configuration()):
        try:
            self.ingestion_configuration_fn_var = ingestion_configuration_class_var.get_ingestion_config()
        except Exception as e:
            raise CustomException(e,sys)


    def download_data(self):
        try:
            logging.info("running download_data function of ingestion class")
            download_url_var = self.ingestion_configuration_fn_var.download_url
            download_in_rawdir_var = self.ingestion_configuration_fn_var.raw_data_dir
            logging.info("making directory for downloading")
            create_dir(download_in_rawdir_var)
            
            download_file_name_var = os.path.basename(download_url_var)
            file_path_var =os.path.join(download_in_rawdir_var,download_file_name_var)
            logging.info("downloading data")
            urllib.request.urlretrieve(download_url_var,file_path_var)
            logging.info("downloading successfull")
            
            #df = pd.read_csv(file_path_var)
            #print(df)
            logging.info("data download successfull")
            return print(file_path_var)
        except Exception as e:
            raise CustomException(e,sys)
        


    
    def initiate_data_ingestion(self):
        try:
            logging.info("initiT DATA ingestion function running")
            self.download_data()
            logging.info("downloa complete")

        except Exception as e:
            raise CustomException(e,sys)