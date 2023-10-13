import shelve
from pathlib import Path
from typing import Dict

from app_config.models import SparkVersion

APP_PATH = Path.home().joinpath(".sparkenv")

def init_app_config():
    with shelve.open(APP_PATH.joinpath("config")) as config:
        config['spark_versions']: Dict[str, SparkVersion] = dict()
    
def add_spark_version(spark_version: SparkVersion):
    with shelve.open(APP_PATH.joinpath("config")) as config:
        config['spark_versions']
