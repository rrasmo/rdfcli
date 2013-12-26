
class History:

    def __init__(self):
        self.refs = []
        self.current = -1

    def push(self, ref):
        self.refs = self.refs[0:self.current + 1]
        self.refs.append(ref)
        self.current += 1

    def forward(self):
        if self.current < len(self.refs) - 1:
            self.current += 1
            if self.current <= len(self.refs) - 1:
                return self.refs[self.current]
        return False

    def back(self):
        if self.current >= 0:
            self.current -= 1
            if self.current >= 0:
                return self.refs[self.current]
            return None
        return False

