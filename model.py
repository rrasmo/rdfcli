from rdflib import Graph
from rdflib import URIRef

class Model:

    def __init__(self):
        self.g = Graph()
        self.load('foaf.rdf')

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


