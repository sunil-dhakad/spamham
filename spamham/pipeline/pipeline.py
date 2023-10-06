from spamham.config.configuration import Configuration
import os,sys
from spamham.components.ingestion import Ingestionclass
from spamham.exception import CustomException
from spamham.logger import logging


class Pipeline:
    def __init__(self,):
        try:
            self.ingestionclass = Ingestionclass()
        except Exception as e:
            raise CustomException(e,sys)
        

    def run_pipeline(self):
        try:

            #ingestionclass_obj = self.ingestionclass()
            self.ingestionclass.initiate_data_ingestion()
        except Exception as e:
            raise CustomException(e,sys)