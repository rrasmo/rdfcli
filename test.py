#!/usr/bin/python

import unittest
from view import View
from controller import Controller 
from model import Model
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

