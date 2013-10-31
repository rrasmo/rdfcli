from rdflib import URIRef

class Controller:

    def __init__(self):
        self.node = None

    def set_model(self, model):
        self.model = model

    def load(self, source):
        return self.model.load(source)

    def size(self):
        return self.model.size()

    def go(self, uri):
        ref = URIRef(uri)
        if self.model.contains_resource(ref):
            self.node = ref
            return True
        return False

    def this(self):
        return self.node

    def pred(self):
        return self.model.pred(self.node)

    def obj(self, pred):
        return self.model.obj(self.node, URIRef(pred))

