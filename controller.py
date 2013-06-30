
class Controller:

    def __init__(self):
        pass

    def set_model(self, model):
        self.model = model

    def load(self, source):
        return self.model.load(source)

    def size(self):
        return self.model.size()

