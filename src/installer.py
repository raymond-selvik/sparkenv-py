from downloader import download, get_versions
from config.store import (
    add_spark_version,
    get_all_spark_versions, 
    is_installed,
    set_active_version,
    get_active_version
)

def get_available_versions() -> list[str]:
    return get_versions()

def install_spark(version: str):
    if not is_installed(version):
        installed_spark_version = download(version)
        add_spark_version(installed_spark_version)
    else:
        print(f"{version} is already installed.")


def get_installed_spark():
    print("Version \t Path")
    print("-----------------------------------------------")
    for v in get_all_spark_versions():
        print(f"{v.name}\t{v.install_path}")

def set_spark_version(spark_version: str):
    if is_installed(spark_version):
        set_active_version(spark_version)
    else:
        raise Exception("Could not set active spark version. Spark version is not installed")
    
def get_active_spark_version():
    return get_active_version()

