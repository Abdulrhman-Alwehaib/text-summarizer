import os
from box.exceptions import BoxValueError
from box import ConfigBox
from textSummarizer.loggining.logger import loggerInstance
from ensure import ensure_annotations
from pathlib import Path
import yaml


@ensure_annotations
def readYaml(pathToYaml: Path) -> ConfigBox:
    try:
        with open(pathToYaml) as yamlFile:
            content = yaml.safe_load(yamlFile)
            loggerInstance.info(f"yaml file {pathToYaml} loaded!")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def createDirectories(pathToDirectory: list,verbos=True):
    for path in pathToDirectory:
        os.makedirs(path,exist_ok=True)
        if verbos:
            loggerInstance.info(f"created diretory at {path}")