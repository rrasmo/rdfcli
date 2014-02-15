# -*- coding: utf-8 -*-

import unittest
from rdflib import Graph
from rdflib.namespace import Namespace, RDF, FOAF
from rdflib.term import URIRef, Literal

from rdfcli.controller import Controller
from rdfcli.model import Model

N = Namespace('http://example.org/#')
REL = Namespace('http://www.perceive.net/schemas/relationship/')

class TestController(unittest.TestCase):

    def setUp(self):
        self.controller = Controller()

        # stub Model.load to load only a local file
        def load_stub(self, source, format=None):
            self.graph.parse('test/fixture.rdf')

        Model.load = load_stub
        model = Model()
        self.controller.set_model(model)
        self.controller.load('test/fixture.rdf')

    def test_initialization(self):
        self.assertEqual(self.controller.current, None)
        self.assertEqual(self.controller.history.refs, [])

    def test_size(self):
        result = self.controller.size()
        self.assertEqual(7, result)

    def test_ls(self):
        self.controller.go(N.spiderman)
        result = self.controller.ls(None)
        self.assertIn(FOAF.Person, result[RDF.type])
        self.assertIn(Literal('Spiderman'), result[FOAF.name])
        self.assertIn(Literal(u'Человек-паук', lang=u'ru'), result[FOAF.name])
        result = self.controller.ls('foaf:name')
        self.assertIn(Literal('Spiderman'), result)
        self.assertIn(Literal(u'Человек-паук', lang=u'ru'), result)

    def test_is(self):
        self.controller.go(N.spiderman)
        result = self.controller.is_(None)
        self.assertIn(N.green_goblin, result[REL.enemyOf])
        result = self.controller.is_('rel:enemyOf')
        self.assertIn(N.green_goblin, result)

    def test_go(self):
        result = self.controller.go(N.green_goblin)
        self.assertEqual(N.green_goblin, result)
        self.assertEqual(N.green_goblin, self.controller.current)
        result = self.controller.go(None)
        self.assertEqual(None, result)
        self.assertEqual(None, self.controller.current)

    def test_fw(self):
        self.controller.go(N.spiderman)
        result = self.controller.fw(REL.enemyOf)
        self.assertEqual(N.green_goblin, result)
        self.assertEqual(N.green_goblin, self.controller.current)

    def test_bw(self):
        self.controller.go(N.green_goblin)
        result = self.controller.bw(REL.enemyOf)
        self.assertEqual(N.spiderman, result)
        self.assertEqual(N.spiderman, self.controller.current)

    def test_forward(self):
        self.controller.go(N.spiderman)
        self.controller.back()
        result = self.controller.forward()
        self.assertEqual(N.spiderman, self.controller.current)

    def test_back(self):
        self.controller.go(N.spiderman)
        result = self.controller.back()
        self.assertEqual(None, self.controller.current)

    def test_this(self):
        self.controller.go(N.spiderman)
        result = self.controller.this()
        self.assertEqual(N.spiderman, self.controller.current)

