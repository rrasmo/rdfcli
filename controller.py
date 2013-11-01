from rdflib import URIRef

class Controller:

    def __init__(self):
        self.current = None

    def set_model(self, model):
        self.model = model

    def load(self, source):
        '''load triples in graph from source'''
        return self.model.load(source)

    def size(self):
        '''return number of triples in graph'''
        return self.model.size()

    def ls(self, uri):
        '''return predicates-objects if uri exists, return objects of current if predicate given, return current predicates-objects if no uri is given'''
        if uri:
            ref = URIRef(uri)
            if self.model.contains_resource(ref):
                return self.model.get_predicate_objects(ref)
            elif self.current:
                return self.model.get_objects(self.current, ref)
        elif self.current:
            return self.model.get_predicate_objects(self.current)
        return None

    def go(self, uri):
        '''set current to given uri, or to object of given predicate of current'''
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
        '''return current'''
        return self.current

    def pred(self):
        '''return predicates of current'''
        return self.model.pred(self.current)

    def obj(self, pred):
        '''return objects of predicate of current'''
        return self.model.obj(self.current, URIRef(pred))

