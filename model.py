from rdflib import Graph

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

