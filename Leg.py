class Leg:

    pins = ()
    angles = ()
    moves = []
    lastUpdate = 0
    
    def __init__(self, pins, angles):
        self.pins = pins
        self.angles = angles

    def addMove(self, move):
        self.moves.append(move)

    def callback(self, currTime):
        #Make sure next move has not passed yet
        if (self.moves[0][3] < currTime):
            self.moves.pop(0)
            if (len(self.moves)==0):
                return
        
        nextMove = self.moves[0]
        moveAngles = nextMove[0:3]
        moveTime = nextMove[3]

        interval = moveTime - self.lastUpdate

        ratio = (currTime-self.lastUpdate)*(1.0/interval)

        newAngles = [0.0,0.0,0.0]
        for i in range(3):
            newAngles[i] = self.angles[i]*(1.0-ratio) + moveAngles[i]*ratio

        self.angles = newAngles
        self.lastUpdate = currTime  

        self.sendAngles()


    def sendAngles(self):
        print(self.lastUpdate, self.angles)

    def pendingMoves(self):
        return len(self.moves) > 0