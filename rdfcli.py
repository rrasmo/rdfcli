#!/usr/bin/python

from view import View
from controller import Controller
from model import Model

if __name__ == '__main__':

    view = View()
    controller = Controller()
    model = Model()

    view.set_controller(controller)
    controller.set_model(model)

    view.cmdloop()

