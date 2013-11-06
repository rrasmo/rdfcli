from cmd import Cmd
from rdflib import URIRef

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

    def do_load(self, uri):
        if uri:
            res = self.controller.load(uri)
            print 'Loaded %s' % uri if res else 'Error loading %s' % uri
        else:
            print 'what?'

    def do_size(self, params):
        print self.controller.size()

    def do_ls(self, uri):
        res = self.controller.ls(uri)
        if res:
            for r in res:
                if type(r) == tuple:
                    print "%s\n    %s" % (self.__norm(r[0]), self.__norm(r[1]))
                else:
                    print self.__norm(r)
        else:
            print 'nope'

    def help_ls(self):
        print 'ls <resource_uri> #list a resource uri'
        print 'ls <predicate_uri> #list the values of a predicate of current resource'

    def do_go(self, uri):
        ref = self.controller.go(uri)
        if ref:
            self.prompt = str(self.__norm(ref, True)) + '> '
        elif ref == None:
            self.prompt = '> '
        else:
            print 'nope'

    def help_go(self):
        print 'go <resource_uri> #go to a resource'
        print 'go <predicate_uri> #go to the value of a predicate of current resource'

    def do_this(self, params):
        ref = self.controller.this()
        print self.__norm(ref)

    def do_pred(self, params):
        predicates = self.controller.pred()
        for pred in predicates:
            print self.__norm(pred)

    def do_obj(self, uri):
        objects = self.controller.obj(uri)
        for obj in objects:
            print self.__norm(obj)

    def __norm(self, ref, trim=False):
        res = self.controller.norm(ref)
        if trim and res[0] == '<' and res[-1] == '>':
            return res[1:-1]
        return res

