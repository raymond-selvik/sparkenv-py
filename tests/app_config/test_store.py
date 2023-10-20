import os
import unittest
from unittest.mock import patch
from pathlib import Path
import shutil

from src.config import store
from src.config.models import SparkVersion



class AppConfigStoreTestCase(unittest.TestCase):
    TMP_FOLDER = "./tmp"

    @patch("src.config.store.APP_PATH", Path('./tmp'))
    def setUp(self) -> None:
        Path.mkdir(self.TMP_FOLDER, exist_ok=True)
        store.init_app_config()

    
    def tearDown(self) -> None:
        if Path(self.TMP_FOLDER).exists() and Path(self.TMP_FOLDER).is_dir():
            shutil.rmtree(self.TMP_FOLDER)

    
    @patch("src.config.store.APP_PATH", Path('./tmp'))
    def test_add_and_get_spark_version(self):
        expected_spark_version = SparkVersion(name =  "aa", install_path = Path("bb"))
        
        store.add_spark_version(expected_spark_version)
        actual_spark_version = store.get_spark_version(expected_spark_version.name)

        assert expected_spark_version == actual_spark_version

    @patch("src.config.store.APP_PATH", Path('./tmp'))
    def test_add_and_get_all_spark_versions(self):
        expected_spark_versions = [
            SparkVersion(name =  "a1", install_path = Path("b1")),
            SparkVersion(name =  "a2", install_path = Path("b2"))
        ]

        store.add_spark_version(expected_spark_versions[0])
        store.add_spark_version(expected_spark_versions[1])

        actual_spark_versions = store.get_all_spark_versions()

        assert expected_spark_versions == actual_spark_versions
    
    @patch("src.config.store.APP_PATH", Path('./tmp'))
    def test_remove_spark_version(self):
        spark_version  = SparkVersion(name =  "a1", install_path = Path("b1"))
    
        store.add_spark_version(spark_version)
        store.remove_spark_version(spark_version.name)

        self.assertRaises(Exception,  lambda: store.get_spark_version(spark_version.name))





