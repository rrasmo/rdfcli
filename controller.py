from rdflib import URIRef

class Controller:

    def __init__(self):
        self.current = None

    def set_model(self, model):
        self.model = model

    def load(self, source):
        return self.model.load(source)

    def size(self):
        return self.model.size()

    def ls(self, uri):
        if uri:
            ref = URIRef(uri)
        elif self.current:
            ref = self.current
        else:
            return None
        if self.model.contains_resource(ref):
            #TODO: show preds and objs of that resource
            return [ref]
        elif self.current:
            return self.model.get_objects(self.current, ref)
        return None

    def go(self, uri):
        ref = URIRef(uri)
        if self.model.contains_resource(ref):
            self.current = ref
            return ref
        elif self.current:
            objs = self.model.get_resource_objects(self.current, ref)
            if len(objs) > 0:
                obj = objs[0]
                self.current= obj
                return obj
        return False

    def this(self):
        return self.current

    def pred(self):
        return self.model.pred(self.current)

    def obj(self, pred):
        return self.model.obj(self.current, URIRef(pred))

