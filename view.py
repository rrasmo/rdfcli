from cmd import Cmd

class View(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = '> '

    def set_controller(self, controller):
        self.controller = controller

    def do_quit(self, params):
        return True

    def help_quit(self):
        print 'quit #exit'

    def do_exit(self, params):
        return True

    def help_exit(self):
        print 'exit #exit'

    def do_EOF(self, params):
        print
        return True

    def help_EOF(self):
        print '(Ctrl-D) #exit'

    def emptyline(self):
        pass

    def do_load(self, uri):
        if uri:
            res = self.controller.load(uri)
            print 'Loaded %s' % uri if res else 'Error loading %s' % uri
        else:
            print 'what?'

    def help_load(self):
        print 'load <uri> #load a file or url into the graph'

    def do_size(self, params):
        print self.controller.size()

    def help_size(self):
        print 'size #print number of triples in the graph'

    def do_ls(self, uri):
        res = self.controller.ls(uri)
        if res:
            self.__print_results(res)
        else:
            print 'nope'

    def help_ls(self):
        print 'ls #list predicate-objects of current resource'
        print 'ls <predicate_uri> #list objects of current resource for given predicate'

    def do_is(self, uri):
        res = self.controller.is_(uri)
        if res:
            self.__print_results(res)
        else:
            print 'nope'

    def help_is(self):
        print 'is #list subject-predicates of current resource'
        print 'is <predicate_uri> #list subjects of current resource for given predicate'

    def do_go(self, uri):
        ref = self.controller.go(uri)
        if ref != False:
            self.__update_prompt(ref)
        else:
            print 'nope'

    def help_go(self):
        print 'go <resource_uri> #go to a resource'

    def do_fw(self, uri):
        objs = self.controller.get_objects(uri)
        index = 0
        if len(objs) > 1:
            for i, obj in enumerate(objs):
                print '    %d) %s' % (i, obj)
            try:
                index = int(raw_input('Select one resource: '))
            except ValueError:
                print 'not a number'
                return
        ref = self.controller.fw(uri, index)
        if ref != False:
            self.__update_prompt(ref)
        else:
            print 'what?'

    def help_fw(self):
        print 'fw <predicate_uri> #go to the object of a predicate of current resource'

    def do_bw(self, uri):
        subjs = self.controller.get_subjects(uri)
        index = 0
        if len(subjs) > 1:
            for i, subj in enumerate(subjs):
                print '    %d) %s' % (i, subj)
            try:
                index = int(raw_input('Select one resource: '))
            except ValueError:
                print 'not a number'
                return
        ref = self.controller.bw(uri, index)
        if ref != False:
            self.__update_prompt(ref)
        else:
            print 'what?'

    def help_bw(self):
        print 'bw <predicate_uri> #come to the subject of a predicate pointing to current resource'

    def do_f(self, params):
        ref = self.controller.forward()
        if ref != False:
            self.__update_prompt(ref)
        else:
            print 'nope'

    def help_f(self):
        print 'f #go forward in history'

    def do_b(self, params):
        ref = self.controller.back()
        if ref != False:
            self.__update_prompt(ref)
        else:
            print 'nope'

    def help_b(self):
        print 'b #go back in history'

    def do_hist(self, params):
        history = self.controller.history
        for i, ref in enumerate(history.refs):
            print '%d: %s' % (i, ref)
        print 'current: ' + str(history.current)

    def help_hist(self):
        print 'hist #print history'

    def do_this(self, params):
        ref = self.controller.this()
        print self.__norm(ref)

    def help_this(self):
        print 'this #print current resource'

    def do_pred(self, params):
        predicates = self.controller.pred()
        for pred in predicates:
            print self.__norm(pred)

    def help_pred(self):
        print 'pred #print predicates of current resource'

    def do_obj(self, uri):
        objects = self.controller.obj(uri)
        for obj in objects:
            print self.__norm(obj)

    def help_obj(self):
        print 'obj #print objects of any predicate of current resource'
        print 'obj <predicate_uri> #print objects of predicate of current resource'

    def do_props(self, params):
        props = self.controller.props()
        for prop in props:
            print self.__norm(prop)

    def help_props(self):
        print 'props #print all predicates in the graph'

    def do_types(self, params):
        types = self.controller.types()
        for type_ in types:
            print self.__norm(type_)

    def help_types(self):
        print 'types #print all terms in the graph that are objects of rdf:type'

    def __norm(self, ref, trim=False):
        res = self.controller.norm(ref)
        if trim and res[0] == '<' and res[-1] == '>':
            return res[1:-1]
        return res

    def __print_results(self, res):
        for r in res:
            if isinstance(r, tuple):
                print "    %s\n        %s" % (self.__norm(r[0]), self.__norm(r[1]))
            else:
                print "    " + self.__norm(r)

    def __update_prompt(self, ref):
        if ref:
            self.prompt = str(self.__norm(ref, True)) + '> '
        elif ref == None:
            self.prompt = '> '

