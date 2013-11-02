from cmd import Cmd
from rdflib import URIRef

uris = {
    'tim': 'http://www.w3.org/People/Berners-Lee/card#i',
    'name': 'http://xmlns.com/foaf/0.1/name',
    'img': 'http://xmlns.com/foaf/0.1/img',
    'knows': 'http://xmlns.com/foaf/0.1/knows',
    'type': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type'
}

class View(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = '> '

    def set_controller(self, controller):
        self.controller = controller

    def do_quit(self, params):
        return True

    def do_exit(self, params):
        return True

    def do_EOF(self, params):
        print
        return True

    def emptyline(self):
        pass

    def do_load(self, params):
        if params:
            res = self.controller.load(params)
            print res
        else:
            print 'what?'

    def do_size(self, params):
        print self.controller.size()

    def do_ls(self, uri):
        if uri and uris.has_key(uri):
            uri = uris[uri]
        res = self.controller.ls(uri)
        if res:
            for r in res:
                if type(r) == tuple:
                    print "%s\n    %s" % (self.norm(r[0]), self.norm(r[1]))
                else:
                    print self.norm(r)
        else:
            print 'nope'

    def help_ls(self):
        print 'ls <resource_uri> #list a resource uri'
        print 'ls <predicate_uri> #list the values of a predicate of current resource'

    def do_go(self, uri):
        if uri and uris.has_key(uri):
            uri = uris[uri]
        ref = self.controller.go(uri)
        if ref:
            self.prompt = str(self.norm(ref, True)) + '> '
        elif ref == None:
            self.prompt = '> '
        else:
            print 'nope'

    def help_go(self):
        print 'go <resource_uri> #go to a resource'
        print 'go <predicate_uri> #go to the value of a predicate of current resource'

    def do_this(self, params):
        ref = self.controller.this()
        print self.norm(ref)

    def do_pred(self, params):
        predicates = self.controller.pred()
        for pred in predicates:
            print self.norm(pred)

    def do_obj(self, uri):
        if uri and uris.has_key(uri):
            uri = uris[uri]
        objects = self.controller.obj(uri)
        for obj in objects:
            print self.norm(obj)

    def norm(self, ref, trim=False):
        res = self.controller.norm(ref)
        if trim and res[0] == '<' and res[-1] == '>':
            return res[1:-1]
        return res

