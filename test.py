import numpy as np 

class Player(object):
    def __init__(self):
        self.velocity = np.array((3, 3), int)
        self.position = np.array((1,1), int)
        self.gravity = np.array((0,2), int)

        pX, pY = self.position
        vX, vY = self.velocity
        gX, gY = self.gravity

        pX += vX
        pY += vY

        vX += gX
        vY += gY

        self.position = (pX, pY)
        self.velocity = (vX, vY)

p1 = Player()

print(p1.position)
print(p1.velocity)