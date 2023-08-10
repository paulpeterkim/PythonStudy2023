from SeAh import code0810 as vec


a = vec.My3DVector(1, 0, 0)
b = vec.My3DVector(0, 1, 0)
a.print()
b.print()
k = a + a + a + b + b
j = k - a - b
k.print()
j.print()
c = a @ b
d = b @ a
c.print()
d.print()


# print()
# a2 = vec.My2DVector(1, 0)
# b2 = vec.My2DVector(0, 1)
# a2.print()
# b2.print()
# c2 = a2 @ b2
# c2.print()
