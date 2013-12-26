from rdflib import Graph, URIRef
from rdflib.namespace import RDF
import re

class Model:

    def __init__(self):
        self.graph = Graph()
        self.loaded = set()

    def load(self, source):
        if source not in self.loaded:
            self.loaded.add(source)
            try:
                self.graph.parse(source)
            except Exception as e:
                print e
                return False
        return True

    def size(self):
        return len(self.graph)

    def pred(self, subj):
        return list(set(self.graph.predicates(subj)))

    def obj(self, subj, pred):
        return list(self.graph.objects(subj, pred))

    def props(self):
        return set(self.graph.predicates())

    def types(self):
        return set(self.graph.objects(predicate=RDF.type))

    def contains_resource(self, ref):
        resources = filter(lambda x: type(x) == URIRef, self.graph.all_nodes())
        return ref in resources

    def get_resource_objects(self, subj, pred):
        return filter(lambda x: type(x) == URIRef, self.graph.objects(subj, pred))

    def get_objects(self, subj, pred):
        return list(self.graph.objects(subj, pred))

    def get_subjects(self, pred, obj):
        return list(self.graph.subjects(pred, obj))

    def get_predicate_objects(self, subj):
        return list(self.graph.predicate_objects(subj))

    def get_subject_predicates(self, obj):
        return list(self.graph.subject_predicates(obj))

    def norm(self, ref):
        return self.graph.namespace_manager.normalizeUri(ref) if ref else None

    def to_uriref(self, string):
        """Expand QName to UriRef based on existing namespaces."""
        if not string:
            return None
        elif re.match('\w*:\w+', string):
            prefix, name = string.split(':')
            try:
                namespace = dict(self.graph.namespaces())[prefix]
                return namespace + name
            except:
                return None
        else:
            return URIRef(string)


