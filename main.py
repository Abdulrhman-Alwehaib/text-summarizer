from textSummarizer.pipeline.dataIngestionStage import runDataIngestion
from textSummarizer.loggining.logger import loggerInstance

try:
    loggerInstance.info("STAGE 1 <DATA INGESTION STARTING>")
    runDataIngestion()
    loggerInstance.info("STAGE 1 <DATA INGESTION> COMPLETED")
except Exception as e:
    raise e
