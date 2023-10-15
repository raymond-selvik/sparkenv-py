from pathlib import Path

from config.store import init_app_config

def setup_app_dirs():
    base_dir = Path.home().joinpath(".sparkenv")

    if not base_dir.exists():
        print("no app config. Creating new")
        Path.mkdir(base_dir)
        init_app_config()
    if not base_dir.joinpath("versions").exists():
        Path.mkdir(base_dir.joinpath("versions"))

