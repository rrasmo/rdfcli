from rdflib import URIRef

class Controller:

    def __init__(self):
        self.resource = None

    def set_model(self, model):
        self.model = model

    def load(self, source):
        return self.model.load(source)

    def size(self):
        return self.model.size()

    def go(self, uri):
        ref = URIRef(uri)
        if self.model.contains_resource(ref):
            self.resource = ref
            return ref
        elif self.resource:
            objs = self.model.get_resource_objects(self.resource, ref)
            if len(objs) > 0:
                obj = objs[0]
                self.resource = obj
                return obj
        return False

    def this(self):
        return self.resource

    def pred(self):
        return self.model.pred(self.resource)

    def obj(self, pred):
        return self.model.obj(self.resource, URIRef(pred))

