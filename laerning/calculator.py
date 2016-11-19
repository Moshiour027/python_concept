class Calculator(object):
    def __init__(self,*vals):
        self.vals = vals

    def add(self):
        return sum(self.vals)
    def substraction(self):
        return