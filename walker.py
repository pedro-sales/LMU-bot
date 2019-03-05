from Leg import Leg
import time

def step

rightLeg = Leg((1,2,3),(0,0,0))

rightLeg.addMove((5,5,5,1))
rightLeg.addMove((-5,-5,-5,2))

startTime = time.time()

while (rightLeg.pendingMoves()):
    rightLeg.callback(time.time() - startTime)
    time.sleep(0.05)