from cmd import Cmd

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

