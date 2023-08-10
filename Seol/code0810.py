class My3DVector:
    def __init__(self, x, y, z):  # dunder init
        self.x = x
        self.y = y
        self.z = z

    def print(self):
        print(f'vector: <{self.x}, {self.y}, {self.z}>')

    #Operator overloading
    def __add__(self, other):
        #self.x = self.x + other.x
        #self.y = self.y + other.y
        return My3DVector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return My3DVector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return My3DVector(self.x * other.x, self.y * other.y, self.z * other.z)

    def __matmul__(self, other):
        '''
        Cross product of two 3D vectors.

        :param other:
        :return:
        '''
        return My3DVector(self.y * other.z-self.z * other.y,
                          self.z * other.x-self.x * other.z,
                          self.x * other.y-self.y * other.x)


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
        return My2DVector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return My2DVector(self.x * other.x, self.y * other.y)

    def __matmul__(self, other):
        return My3DVector(self.y * 0-0 * other.y, 0 * other.x-self.x * 0, self.x * other.y-self.y * other.x)
