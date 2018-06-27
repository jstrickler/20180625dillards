#!/usr/bin/env python
import sys
import unittest
from textfile import TextFile

FILE_NAME = 'DATA/mary.txt'


class TestTextFile(unittest.TestCase):
    def setUp(self):
        self.t = TextFile(FILE_NAME)

    @unittest.skipUnless(sys.platform=='win32', "only implemented on Windows" )
    def test_name_property(self):
        self.assertEqual(FILE_NAME, t.file_name)

    def test_adding_files(self):
        file_name2 = 'DATA/alice.txt'
        t2 = TextFile(file_name2)
        result = self.t + t2
        self.assertEqual('HA HA HA', result)

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
