from textSummarizer.config.configuration import DataIngestionConfiguration
import os
from datasets import load_dataset

class DataIngestion:
    def __init__(self,config: DataIngestionConfiguration):
        self.config = config
    
    def downloadData(self):
        os.makedirs(self.config.root_dir, exist_ok=True)
        load_dataset(self.config.source_URL_hugging_face).save_to_disk(self.config.localDataFolder)

    def run(self):
        self.downloadData()