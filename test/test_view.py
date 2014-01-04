import unittest

import rdfcli.view
import mocks


class TestView(unittest.TestCase):

    def setUp(self):
        self.view = rdfcli.view.View()
        self.view.set_controller(mocks.MockController())

    def test_view(self):
        pass

