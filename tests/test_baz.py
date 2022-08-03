#!/usr/bin/env python3
import unittest
import time
import sys
import os

# # handle for errors arising from python3 -m unittest ...
# TODO: figure out how to fix this import
try:
    from classes import CustomTestCase
except ModuleNotFoundError:
    THIS_DIR = os.path.dirname(os.path.realpath(__file__))
    sys.path.insert(0, THIS_DIR)
    from classes import CustomTestCase
    sys.path.pop(0)


class TestBaz(CustomTestCase):
    def test_baz_1(self):
        time.sleep(5)

    def test_baz_2(self):
        time.sleep(5)

    def test_baz_3(self):
        time.sleep(5)

    def test_baz_4(self):
        time.sleep(5)

    def test_baz_5(self):
        time.sleep(5)

    def test_baz_6(self):
        time.sleep(5)


if __name__ == "__main__":
    unittest.main()
