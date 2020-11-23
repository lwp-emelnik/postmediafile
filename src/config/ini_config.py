import pathlib
from configparser import ConfigParser


class IniConfig:

    def __init__(self):
        """
        Prepare configuration, preload data from the file
        """
        filename = pathlib.Path(__file__).parent.absolute().__str__() + '/../../data/config.ini'
        self.data = ConfigParser()
        self.data.read(filename)

    def get_config(self, key):
        """
        Get options list for the specified section name
        :param key: Section name
        :return: Dictionary of key=>value options
        """
        return self.data[key]
