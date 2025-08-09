from textSummarizer.components.dataIngestion import DataIngestion
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.loggining.logger import loggerInstance


def runDataIngestion():
    configManager = ConfigurationManager()
    dataIngestionConfig = configManager.getDataIngestionConfig()
    dataIngestionObj = DataIngestion(dataIngestionConfig)
    dataIngestionObj.run()