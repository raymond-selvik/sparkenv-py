from pathlib import Path
from config.models import SparkVersion
import requests
from bs4 import BeautifulSoup
import tarfile

BASE_URL: str = "https://archive.apache.org/dist/spark/"

def get_versions() -> list[str]:
    r = requests.get(BASE_URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    spark_versions = [link.get('href').strip('/').split('/')[-1] for link in soup.find_all('a') if link.get('href', '').startswith('spark-')]
    
    return spark_versions


def download(version: str) -> SparkVersion:
    options = __get_spark_install_options(version)
    option = __install_chooser(options)
    
    r =  requests.get(f"{BASE_URL}/{version}/{option}", stream=True)
    print("Downloading...")
    installation_path = Path.home().joinpath(f".sparkenv/versions")

    with tarfile.open(fileobj=r.raw, mode="r|*") as tar:
        tar.extractall(installation_path)

    return SparkVersion(version, installation_path)


def __get_spark_install_options(version:str):
    r = requests.get(f"{BASE_URL}/{version}")
    if not r.ok:
        raise Exception(f"Did not find Spark Version: {version}")
    soup = BeautifulSoup(r.content, 'html.parser')
    version_options = [link.get('href').strip('/').split('/')[-1] for link in soup.find_all('a') if link.get('href', '').endswith('.tgz')]
    version_options = [v for v in version_options if 'bin' in v]
    
    return version_options

def __install_chooser(options: list[str]) -> str:
    print("Please choose which version to install:")
    for i, version in enumerate(options):
        print(f"{i}: {version}")
    print("Choice:")
    choice = int(input())
    try:
        return options[choice]
    except:
        print("Not a valid choice")
