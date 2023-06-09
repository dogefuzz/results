"""
this module contains the logic of the inputs service
"""
import os
import zipfile

from os import path

from aggregator.config import Config
from aggregator.shared.singleton import SingletonMeta


class InputService(metaclass=SingletonMeta):

    def __init__(self) -> None:
        self._config = Config()

    def extract_inputs(self):
        """
        extracts inputs from resources folder
        """
        inputs_folder = path.join(
            self._config.temp_folder, self._config.inputs_folder)
        inputs_zip_path = path.join(
            self._config.resources_folder, self._config.inputs_zip_filename)

        if path.exists(inputs_folder):
            return
        os.makedirs(inputs_folder)

        with zipfile.ZipFile(inputs_zip_path, 'r') as zip_file:
            zip_file.extractall(inputs_folder)
