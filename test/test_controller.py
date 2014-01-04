import unittest

import rdfcli.controller
import mocks


class TestController(unittest.TestCase):

    def setUp(self):
        self.controller = rdfcli.controller.Controller()
        self.controller.set_model(mocks.MockModel())

    def test_controller(self):
        pass

