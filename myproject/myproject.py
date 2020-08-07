'''This script uninstalls multiplle/all packages in requirements.txt file'''

import os
import logging
import unittest

logging.basicConfig(filename='myproject_log.txt',format='%(asctime)s : %(filename)s : %(funcName)s : %(levelname)s :  %(lineno)d - %(message)s', \
                    level = logging.DEBUG)

class Testcase1(unittest.TestCase):
    def setUp(self):
        self.file = open('requirements.txt')
        self.file_list = self.file.readlines()

    def test_uninstalling(self):
        for i in self.file_list:
            logging.debug('Current Package under work: {}'.format(i))
            exit_code = os.system('pip uninstall -y {}'.format(i))
            if exit_code:
                logging.info('succesfully uninstalled all libraries in requirements.txt file.')
            else:
                logging.error(' Error occured while uninstalling some libraties in requiremets.txt.')

    def tearDown(self):
        self.file.close()
        pass

unittest.main()