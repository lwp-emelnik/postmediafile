import pathlib
from configparser import ConfigParser


class IniConfig:

    def __init__(self):
        """
        Prepare configuration, preload data from the file
        """
        self.filename = pathlib.Path(__file__).parent.absolute().__str__() + '/../../data/config.ini'
        self.data = ConfigParser()
        self.data.read(self.filename)

    def get_config(self, key):
        """
        Get options list for the specified section name
        :param key: Section name
        :return: Dictionary of key=>value options
        """
        return self.data[key]

    def set_config(self, section, values):
        """
        Set options to the specified section and save to the file
        :param section: Section name
        :param values: Dict of key=>values
        :return: 
        """
        for option in values:
            self.data[section][option] = values[option]

        with open(self.filename, 'w') as configfile:
            self.data.write(configfile)
