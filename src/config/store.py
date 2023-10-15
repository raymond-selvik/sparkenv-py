import shelve
from pathlib import Path
from typing import Dict

from src.config.models import SparkVersion

APP_PATH = Path.home().joinpath(".sparkenv")

def init_app_config():
    with shelve.open(APP_PATH.joinpath("config")) as config:
        config['spark_versions']: Dict[str, SparkVersion] = dict()
    
def add_spark_version(spark_version: SparkVersion):
    with shelve.open(APP_PATH.joinpath("config")) as config:
        config['spark_versions'][spark_version.name] = spark_version

def get_spark_version(spark_version_name: str) -> SparkVersion:
    with shelve.open(APP_PATH.joinpath("config")) as config:
        return config['spark_versions'][spark_version_name]

