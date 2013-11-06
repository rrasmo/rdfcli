#!/usr/bin/python

from view import View
from controller import Controller
from model import Model
import sys

if __name__ == '__main__':

    view = View()
    controller = Controller()
    model = Model()

    view.set_controller(controller)
    controller.set_model(model)

    if len(sys.argv) > 1:
        view.do_load(sys.argv[1])

    view.cmdloop()

