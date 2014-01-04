#!/usr/bin/env python

import os
import sys
import unittest

TEST_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.realpath(os.path.join(TEST_ROOT, '..')))

from rdfcli.view import View
from rdfcli.controller import Controller 
from rdfcli.model import Model
import mocks


class TestView(unittest.TestCase):

    def setUp(self):
        self.view = View()
        self.view.set_controller(mocks.MockController())


class TestController(unittest.TestCase):

    def setUp(self):
        self.controller = Controller()
        self.controller.set_model(mocks.MockModel())


class TestModel(unittest.TestCase):

    def setUp(self):
        self.model = Model()


if __name__ == '__main__':
    unittest.main()

