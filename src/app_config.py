from pathlib import Path

def setup_app_dirs():
    base_dir = Path.home().joinpath(".sparkenv")

    if not base_dir.exists():
        print("no app config. Creating new")
        Path.mkdir(base_dir)
    if not base_dir.joinpath("versions").exists():
        Path.mkdir(base_dir.joinpath("versions"))

