import yaml
from textSummarizer.config.configuration import DataValidationConfiguration
import os
class DataValidation:
    def __init__(self,config: DataValidationConfiguration):
        self.config = config
    

    def validatingFiles(self):
        try:
            os.makedirs(self.config.root_dir,exist_ok=True)
            print(str(self.config.inputData))
            files = set(os.listdir(str(self.config.inputData)))
            requiredFiles = set(self.config.REQUIRED_FILES)
            missingFiles = requiredFiles - files

            status = {
                "Status" : "VALID" if not missingFiles else "INVALID",
                "missingFiles": list(missingFiles)
            }

            with open(self.config.STATUS_FILE,"w") as f:
                yaml.safe_dump(status,f)
            if missingFiles:
                raise ValueError("Missing Files are: ", missingFiles)
        except Exception as e:
            raise e
    def run(self):
        self.validatingFiles()