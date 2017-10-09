import numpy as numpy

BodyX = numpy.load("bodyfat_x_15_252.npy")
BodyX = numpy.float32(BodyX)
BodyY = numpy.load("bodyfat_y_252.npy")
BodyY = BodyY.reshape((252, 1))
MyCC = 0
cpw = numpy.dot(numpy.dot(numpy.linalg.inv(MyCC * numpy.identity(15) + numpy.dot(BodyX.T, BodyX)), BodyX.T), BodyY)
print cpw
