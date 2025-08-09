from textSummarizer.pipeline.dataIngestionStage import runDataIngestion
from textSummarizer.pipeline.dataValidationStage import runValidationPipeline
from textSummarizer.loggining.logger import loggerInstance

try:
    loggerInstance.info("STAGE 1 <DATA INGESTION STARTING>")
    runDataIngestion()
    loggerInstance.info("STAGE 1 <DATA INGESTION> COMPLETED")

    loggerInstance.info("STAGE 2 <DATA VALIDATION STARTING>")
    runValidationPipeline()
    loggerInstance.info("STAGE 2 <DATA VALIDATION> COMPLETED")
except Exception as e:
    raise e
