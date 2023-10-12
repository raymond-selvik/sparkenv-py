import requests
from bs4 import BeautifulSoup

BASE_URL: str = "https://archive.apache.org/dist/spark/"

def get_versions() -> list[str]:
    r = requests.get(BASE_URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    spark_versions = [link.get('href').strip('/').split('/')[-1] for link in soup.find_all('a') if link.get('href', '').startswith('spark-')]

    for version in spark_versions:
        print(version)

def download(version: str):
    r = requests.get(f"{BASE_URL}/{version}")
    soup = BeautifulSoup(r.content, 'html.parser')
    spark_installs = [link.get('href').strip('/').split('/')[-1] for link in soup.find_all('a') if link.get('href', '').endswith('.tgz')]
    install_chooser(spark_installs)


def install_chooser(versions: list[str]) -> str:
    print("Please choose which version to install:")
    for i, version in enumerate(versions):
        print(f"{i}: {version}")
    choice = int(input())
    print(versions[choice])
