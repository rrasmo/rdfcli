from rdflib import Graph
from rdflib import URIRef
import re

class Model:

    def __init__(self):
        self.g = Graph()

    def load(self, source):
        try:
            self.g.parse(source)
        except:
            return False
        return True

    def size(self):
        return len(self.g)

    def pred(self, subj):
        return list(set(self.g.predicates(subj)))

    def obj(self, subj, pred):
        return list(self.g.objects(subj, pred))

    def contains_resource(self, ref):
        resources = filter(lambda x: type(x) == URIRef, self.g.all_nodes())
        return ref in resources

    def get_resource_objects(self, subj, pred):
        return filter(lambda x: type(x) == URIRef, self.g.objects(subj, pred))

    def get_objects(self, subj, pred):
        return list(self.g.objects(subj, pred))

    def get_predicate_objects(self, subj):
        return list(self.g.predicate_objects(subj))

    def norm(self, ref):
        return self.g.namespace_manager.normalizeUri(ref) if ref else None

    def to_uriref(self, string):
        '''expand QName to UriRef based on existing namespaces'''
        if not string:
            return None
        elif re.match('\w*:\w+', string):
            prefix, name = string.split(':')
            try:
                namespace = dict(self.g.namespaces())[prefix]
                return namespace + name
            except:
                return None
        else:
            return URIRef(string)


