from history import History

class Controller:

    def __init__(self):
        self.current = None #URIRef
        self.history = History()

    def set_model(self, model):
        self.model = model

    def load(self, source):
        """Load triples in graph from source."""
        return self.model.load(source)

    def size(self):
        """Return number of triples in graph."""
        return self.model.size()

    def ls(self, uri):
        """Return objects of current if predicate given, return current predicates-objects if no uri is given."""
        if uri:
            ref = self.model.to_uriref(uri)
            if ref and self.current:
                return self.model.get_objects(self.current, ref)
        elif self.current:
            return self.model.get_predicate_objects(self.current)
        return None

    def is_(self, uri):
        """Return subjects of current if predicate given, return current subjects-predicates if no uri is given."""
        if uri:
            ref = self.model.to_uriref(uri)
            if ref and self.current:
                return self.model.get_subjects(ref, self.current)
        elif self.current:
            return self.model.get_subject_predicates(self.current)
        return None

    def go(self, uri):
        """Set current to given resource uri, or to None if no uri is given."""
        if uri:
            ref = self.model.to_uriref(uri)
            self.model.load(str(ref))
            if self.model.contains_resource(ref):
                self.current = ref
                self.history.push(ref)
                return ref
            return False
        else:
            self.current = None
            self.history.push(None)
            return None

    def fw(self, uri):
        """Set current to object of given predicate of current."""
        if uri:
            ref = self.model.to_uriref(uri)
            if ref and self.current:
                objs = self.model.get_resource_objects(self.current, ref)
                if len(objs) > 0:
                    obj = objs[0]
                    self.model.load(str(obj))
                    self.current = obj
                    self.history.push(obj)
                    return obj
            return False
        else:
            return False

    def bw(self, uri):
        """Set current to subject of given predicate pointing to current."""
        if uri:
            ref = self.model.to_uriref(uri)
            if ref and self.current:
                subjs = self.model.get_subjects(ref, self.current)
                if len(subjs) > 0:
                    subj = subjs[0]
                    self.model.load(str(subj))
                    self.current = subj
                    self.history.push(subj)
                    return subj
            return False
        else:
            return False

    def forward(self):
        ref = self.history.forward()
        if ref != False:
            self.current = ref
        return ref

    def back(self):
        ref = self.history.back()
        if ref != False:
            self.current = ref
        return ref

    def this(self):
        """Return current."""
        return self.current

    def pred(self):
        """Return predicates of current."""
        return self.model.pred(self.current)

    def obj(self, uri):
        """Return objects of predicate of current."""
        ref = self.model.to_uriref(uri)
        return self.model.obj(self.current, ref)

    def props(self):
        """Return all terms that exist as predicates."""
        return self.model.props()

    def types(self):
        """Return all terms that exist as objects of rdf:type."""
        return self.model.types()

    def norm(self, ref):
        return self.model.norm(ref)

