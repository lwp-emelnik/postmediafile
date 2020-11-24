import os
import xml.etree.ElementTree as ElementTree


class ACDSeeXmp:

    def __init__(self, file_name, xmp_content):
        """
        Prepare object, parse xml file
        :param file_name: File name
        :param xmp_content: Content of the file
        """
        self.file_name = file_name
        self.xmp_parsed_content = ElementTree.fromstring(xmp_content)

    def get_parsed_data(self):
        """
        Return parsed object
        :return: Root tree object
        """
        sidecar_file_name = os.path.splitext(os.path.abspath(self.file_name))[0]
        if not os.path.exists(sidecar_file_name):
            raise Exception('Sidecar file ' + sidecar_file_name + ' not found')

        title = self.xmp_parsed_content.find('.//{http://ns.acdsee.com/iptc/1.0/}caption').text
        if not title:
            title = os.path.splitext(os.path.basename(sidecar_file_name))[0]

        text = self.xmp_parsed_content.find('.//{http://ns.acdsee.com/iptc/1.0/}notes').text

        return {
            'sidecar_file_name': sidecar_file_name,
            'title': title,
            'text': text
        }
