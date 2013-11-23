from rdflib import URIRef

class Controller:

    def __init__(self):
        self.current = None #URIRef

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
            ref = self.model.to_uriref(uri)
            if self.model.contains_resource(ref):
                return self.model.get_predicate_objects(ref)
            elif self.current:
                return self.model.get_objects(self.current, ref)
        elif self.current:
            return self.model.get_predicate_objects(self.current)
        return None

    def is_(self, uri):
        '''return subjects-predicates if uri exists, return subjects of current if predicate given, return current subjects-predicates if no uri is given'''
        if uri:
            ref = self.model.to_uriref(uri)
            if self.model.contains_resource(ref):
                return self.model.get_subject_predicates(ref)
            elif self.current:
                return self.model.get_subjects(ref, self.current)
        elif self.current:
            return self.model.get_subject_predicates(self.current)
        return None

    def go(self, uri):
        '''set current to given resource uri, to object of given predicate of current, or to None if no uri is given'''
        if uri:
            ref = self.model.to_uriref(uri)
            if self.model.contains_resource(ref):
                self.current = ref
                return ref
            elif self.current:
                objs = self.model.get_resource_objects(self.current, ref)
                if len(objs) > 0:
                    obj = objs[0]
                    self.current = obj
                    return obj
            return False
        else:
            self.current = None
            return None

    def come(self, uri):
        '''set current to given resource uri, to subject of given predicate of current, or to None if no uri is given'''
        if uri:
            ref = self.model.to_uriref(uri)
            if self.model.contains_resource(ref):
                self.current = ref
                return ref
            elif self.current:
                subjs = self.model.get_subjects(ref, self.current)
                if len(subjs) > 0:
                    subj = subjs[0]
                    self.current = subj
                    return subj
            return False
        else:
            self.current = None
            return None

    def this(self):
        '''return current'''
        return self.current

    def pred(self):
        '''return predicates of current'''
        return self.model.pred(self.current)

    def obj(self, uri):
        '''return objects of predicate of current'''
        ref = self.model.to_uriref(uri)
        return self.model.obj(self.current, ref)

    def props(self):
        '''return all terms that exist as predicates'''
        return self.model.props()

    def types(self):
        '''return all terms that exist as objects of rdf:type'''
        return self.model.types()

    def norm(self, ref):
        return self.model.norm(ref)

