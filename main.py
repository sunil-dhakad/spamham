from spamham.exception import CustomException
from spamham.logger import logging
import os,sys
from spamham.pipeline.pipeline import Pipeline

import pandas as pd 
import numpy as np



def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        raise CustomException(e,sys)


if __name__=="__main__":
    main()