from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.dataValidation import DataValidation
from textSummarizer.loggining.logger import loggerInstance

def runValidationPipeline():
    try:

        configManager = ConfigurationManager()
        validationConfig = configManager.getDataValidationConfiguration()
        DataValidationObj = DataValidation(validationConfig)
        DataValidationObj.run()
    except Exception as e:
        raise e