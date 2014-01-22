from cmd import Cmd

HELP_MSG = '''
Commands:

  load URI    # Load triples from URI or file.
  go URI      # Go to a resource and load related triples.
  size        # Print the number of triples in the graph.
  types       # List all types, i.e. objects of rdf:type.
  this        # Print the current resource.
  pred        # List all predicates of the current resource.
  ls [PRED]   # List outgoing predicates and objects. If a predicate is given, print the objects.
  fw PRED     # Follow outgoing predicate, go to the object.
  is [PRED]   # List incoming subjects and predicates. If a predicate is given, print the subjects.
  bw PRED     # Follow backwards incoming predicate, go to the subject.
  f           # Go forward in history
  b           # Go back in history
  hist        # Print history stack.
  help        # Print this help.
  exit        # Exit.
'''

class View(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = '> '

    def set_controller(self, controller):
        self.controller = controller

    def do_help(self, params):
        print HELP_MSG

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
        if isinstance(res, dict):
            self.__print_properties(res)
        elif isinstance(res, list):
            self.__print_objects(res)
        else:
            print 'nope'

    def do_is(self, uri):
        res = self.controller.is_(uri)
        if isinstance(res, dict):
            self.__print_properties(res, reverse=True)
        elif isinstance(res, list):
            self.__print_objects(res)
        else:
            print 'nope'

    def do_go(self, uri):
        ref = self.controller.go(uri)
        if ref != False:
            self.__update_prompt(ref)
        else:
            print 'nope'

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

    def do_f(self, params):
        ref = self.controller.forward()
        if ref != False:
            self.__update_prompt(ref)
        else:
            print 'nope'

    def do_b(self, params):
        ref = self.controller.back()
        if ref != False:
            self.__update_prompt(ref)
        else:
            print 'nope'

    def do_hist(self, params):
        history = self.controller.history
        for i, ref in enumerate(history.refs):
            print '%d: %s' % (i, ref)
        print 'current: ' + str(history.current)

    def do_this(self, params):
        ref = self.controller.this()
        print self.__norm(ref)

    def do_pred(self, params):
        predicates = self.controller.pred()
        for pred in predicates:
            print self.__norm(pred)

    def do_types(self, params):
        types = self.controller.types()
        for type_ in types:
            print self.__norm(type_)

    def __norm(self, ref, trim=False):
        res = self.controller.norm(ref)
        if trim and res[0] == '<' and res[-1] == '>':
            return res[1:-1]
        return res

    def __print_properties(self, props, reverse=False):
        for prop, vals in props.items():
            if reverse:
                print "    is %s of" % (self.__norm(prop))
            else:
                print "    %s" % (self.__norm(prop))
            for val in vals:
                print "        %s" % (self.__norm(val))

    def __print_objects(self, res):
        for r in res:
            print "    " + self.__norm(r)

    def __update_prompt(self, ref):
        if ref:
            self.prompt = str(self.__norm(ref, True)) + '> '
        elif ref == None:
            self.prompt = '> '

