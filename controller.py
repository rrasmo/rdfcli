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
        self.node = URIRef(uri)

    def this(self):
        return self.node

