

def transform_3D(self, x, y):
    yLinear = (y * self.yPerspective) / self.height
    if yLinear > self.yPerspective: # can't go above
        yLinear = self.yPerspective

    xDiff = x - self.xPerspective
    yDiff = self.yPerspective - yLinear

    yFactor = yDiff / self.yPerspective
    yFactor = pow(yFactor, 3)

    xTransform = self.xPerspective + (xDiff * yFactor)
    yTransform = self.yPerspective - (yFactor * self.yPerspective)
    return int(xTransform), int(yTransform)

def transform_2D(self, x, y):
    return int(x), int(y)