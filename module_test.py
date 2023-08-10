class My2DVector:
    def __init__(self, x, y):  # dunder init
        self.x = x
        self.y = y

    def print(self):
        print(f'vector: <{self.x}, {self.y}>')

    # Operator overloading
    def __add__(self, other):
        # self.x = self.x + other.x
        # self.y = self.y + other.y
        return My2DVector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        return My2DVector(self.x * other.x, self.y * other.y)

    def __matmul__(self, other):
        pass
