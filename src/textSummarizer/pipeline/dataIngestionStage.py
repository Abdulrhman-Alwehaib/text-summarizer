from textSummarizer.components.dataIngestion import DataIngestion
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.loggining.logger import loggerInstance


def runDataIngestion():
    config = ConfigurationManager()
    dataIngestionConfig = config.getDataIngestionConfig()
    dataIngestionObj = DataIngestion(dataIngestionConfig)
    dataIngestionObj.run()