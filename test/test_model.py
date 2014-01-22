# -*- coding: utf-8 -*-

import unittest
from rdflib.term import URIRef, Literal
from rdflib.namespace import Namespace, RDF, FOAF

import rdfcli.model

N = Namespace('http://example.org/#')
REL = Namespace('http://www.perceive.net/schemas/relationship/')

class TestModel(unittest.TestCase):

    def setUp(self):
        self.model = rdfcli.model.Model()
        self.model.load('test/fixture.ttl', format='turtle')

    def test_has_empty_graph(self):
        self.model = rdfcli.model.Model()
        self.assertEqual(len(self.model.graph), 0)

    def test_load_local_file(self):
        self.model = rdfcli.model.Model()
        self.model.load('rdfcli/foaf.rdf')
        self.assertEqual(len(self.model.graph), 213)

    def test_size(self):
        self.assertEqual(self.model.size(), 7)

    def test_pred(self):
        result = self.model.pred(N.spiderman)
        self.assertIn(FOAF.name, result)
        self.assertIn(REL.enemyOf, result)
        self.assertIn(RDF.type, result)

    def test_types(self):
        result = self.model.types()
        self.assertIn(FOAF.Person, result)

    def test_contains_resource(self):
        result = self.model.contains_resource(N.spiderman)
        self.assertTrue(result)

    def test_get_resource_objects(self):
        result = self.model.get_resource_objects(N.spiderman, RDF.type)
        self.assertIn(FOAF.Person, result)

    def test_get_objects(self):
        result = self.model.get_objects(N.spiderman, FOAF.name)
        self.assertIn(Literal('Spiderman'), result)
        self.assertIn(Literal(u'Человек-паук', lang=u'ru'), result)

    def test_get_subjects(self):
        result = self.model.get_subjects(RDF.type, FOAF.Person)
        self.assertIn(N.spiderman, result)
        self.assertIn(N.green_goblin, result)

    def test_get_properties(self):
        result = self.model.get_properties(N.spiderman)
        self.assertIn(N.green_goblin, result[REL.enemyOf])
        self.assertIn(FOAF.Person, result[RDF.type])
        self.assertIn(Literal('Spiderman'), result[FOAF.name])
        self.assertIn(Literal(u'Человек-паук', lang=u'ru'), result[FOAF.name])

    def test_get_reverse_properties(self):
        result = self.model.get_reverse_properties(N.green_goblin)
        self.assertIn(N.spiderman, result[REL.enemyOf])

    def test_to_uriref(self):
        ref = self.model.to_uriref('rel:enemyOf')
        self.assertEqual(ref, URIRef(u'http://www.perceive.net/schemas/relationship/enemyOf'))

