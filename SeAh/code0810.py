class My3DVector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def print(self):
        print(f'vector: <{self.x}, {self.y}, {self.z}>')

    def __add__(self, other):
        return My3DVector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return My3DVector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return My3DVector(self.x * other, self.y * other, self.z * other)
        return My3DVector(self.x * other.x, self.y * other.y, self.z * other.z)

    def __matmul__(self, other):
        return My3DVector(self.y * other.z - self.z * other.y,
                          -1 * self.x * other.z + self.z * other.x,
                          self.x * other.y - self.y * other.x)
