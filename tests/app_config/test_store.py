import os
import unittest
from unittest.mock import patch
from pathlib import Path
import shutil

from src.config.store import init_app_config, get_spark_version, add_spark_version
from src.config.models import SparkVersion



class AppConfigStoreTestCase(unittest.TestCase):
    TMP_FOLDER = "./tmp"

    @patch("src.config.store.APP_PATH", Path('./tmp'))
    def setUp(self) -> None:
        Path.mkdir(self.TMP_FOLDER, exist_ok=True)
        init_app_config()

    
    def tearDown(self) -> None:
        if Path(self.TMP_FOLDER).exists() and Path(self.TMP_FOLDER).is_dir():
            shutil.rmtree(self.TMP_FOLDER)

    
    @patch("src.config.store.APP_PATH", Path('./tmp'))
    def test_add_and_get_spark_version(self):
        expected_spark_version = SparkVersion(name =  "aa", install_path = "bb")

        add_spark_version(expected_spark_version)
        actual_spark_version = get_spark_version(expected_spark_version.name)

        assert expected_spark_version == actual_spark_version



