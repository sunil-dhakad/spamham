from collections import namedtuple


DataIngestionConfig = namedtuple("IngestionConfig",
                                 ["download_url",
                                  "raw_data_dir",
                                  ])