class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        return self.first + self.second

    def __sub__(self):
        return self.first - self.second

    def __mul__(self):
        return self.first * self.second

    def __div__(self):
        return self.first / self.second


