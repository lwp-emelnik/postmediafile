import os
import xml.etree.ElementTree as ElementTree


class ACDSeeXmp:

    def __init__(self, file_name, xmp_content):
        """
        Prepare object, parse xml file
        :param xmp_content: Content of the file
        """
        self.file_name = file_name
        self.xmp_parsed_content = ElementTree.fromstring(xmp_content)

    def get_parsed_data(self):
        """
        Return parsed object
        :return: Root tree object
        """
        return {'filename': os.path.splitext(self.file_name)[0]}
