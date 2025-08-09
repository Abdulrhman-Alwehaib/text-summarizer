from textSummarizer.constants.constantsValues import *
from textSummarizer.utils.common import readYaml, createDirectories
from textSummarizer.entity.entity import *

class ConfigurationManager:
    def __init__(self,
                 configFilePath=CONFIG_FILE_PATH,
                 paramsFilePath=PARAMS_FILE_PATH):
        self.config = readYaml(configFilePath)
        #self.params = readYaml(paramsFilePath)

    def getDataIngestionConfig(self) -> DataIngestionConfiguration:
        config = self.config.data_ingestion

        return DataIngestionConfiguration(
            root_dir = config.root_dir,
            source_URL_hugging_face = config.source_URL_hugging_face,
            localDataFolder = config.localDataFolder
        )
