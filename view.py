from cmd import Cmd

uris = {
    'tim': 'http://www.w3.org/People/Berners-Lee/card#i'
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

    def do_size(self, params):
        print self.controller.size()

    def do_go(self, uri):
        if uri :
            if uris.has_key(uri):
                uri = uris[uri]
            self.controller.go(uri)
            self.prompt = uri + '> '

    def do_this(self, params):
        print self.controller.this()

    def do_pred(self, params):
        predicates = self.controller.pred()
        for pred in predicates:
            print pred

    def do_obj(self, pred):
        objects = self.controller.obj(pred)
        for obj in objects:
            print obj

