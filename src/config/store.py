import shelve
from pathlib import Path
from typing import Dict

from config.models import SparkVersion

APP_PATH = Path.home().joinpath(".sparkenv")

def init_app_config():
    with shelve.open(APP_PATH.joinpath("config")) as config:
        config['spark_versions']: Dict[str, SparkVersion] = dict()
    
def add_spark_version(spark_version: SparkVersion):
    with shelve.open(APP_PATH.joinpath("config"), writeback=True) as config:
        spark_versions =  config['spark_versions']
        spark_versions[spark_version.name] = spark_version

def get_spark_version(spark_version_name: str) -> SparkVersion:
    with shelve.open(APP_PATH.joinpath("config")) as config:
        spark_versions = config['spark_versions']
        if spark_versions.get(spark_version_name) is None:
            raise Exception("Spark version does not exist in config.")
        else:
            return spark_versions[spark_version_name]

def get_all_spark_versions() -> list[SparkVersion]:
    with shelve.open(APP_PATH.joinpath("config")) as config:
        spark_versions = config['spark_versions']
        return list(spark_versions.values())

def remove_spark_version(spark_version: str):
    with shelve.open(APP_PATH.joinpath("config"), writeback=True) as config:
        del config['spark_versions'][spark_version]

def is_installed(spark_version: str) -> bool:
    with shelve.open(APP_PATH.joinpath("config"), writeback=True) as config:
       return spark_version in config['spark_versions']
    
def set_active_version(spark_version_name: str):
    with shelve.open(APP_PATH.joinpath("config"), writeback=True) as config:
        if is_installed(spark_version_name):
            config["spark_version_active"] = spark_version_name
        else:
            raise Exception(f"Could not set version. {spark_version_name} does not exist")

def get_active_version():
    with shelve.open(APP_PATH.joinpath("config")) as config:
        return config.get('spark_version_active', None)
