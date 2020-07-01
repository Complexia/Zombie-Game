import numpy

# 0s represent empty cells, 1s are zombies, 2s are civillians
class World:

    def __init__(self, xDim, yDim, initialZombiePos, civillianPos, zombieMoves):
        self.__grid = numpy.zeros((yDim, xDim))
        self.__initialZombiePos = initialZombiePos
        self.__civillianPos = civillianPos
        self.__zombieMoves = zombieMoves
        self.__zombieList = [initialZombiePos]
        self.__zombiePoints = 0
        self.__finalZombiePositions = []

        #populating world with civillians
        for civillian in civillianPos:
            self.__grid[int(civillian["y"]), int(civillian["x"])] = 2
        
        #saving grid state prior to zombies for visualization purposes
        self.__gridPrev = self.__grid.copy()
        self.__gridPrev[int(initialZombiePos["y"]), int(initialZombiePos["x"])] = 1

    #moves the zombie cell by cell on the grid    
    def zombieMove(self, zombiePos):       
        currentPosition = zombiePos
        currentPositionSymbol = 0
        zombieMoves = self.__zombieMoves
        #taking each move as a letter (U,D,L,R) from the zombieMoves list
        for move in zombieMoves:
            #if there was a civ there before, now there is a zombie
            if currentPositionSymbol == 2:
                currentPositionSymbol = 1
            #upon leaving the cell, update to previous state
            self.__grid[int(currentPosition["y"]), int(currentPosition["x"])] = currentPositionSymbol
            #update current position as per move
            #uncomment below line for detailed output of each move  
            #print("move: ", move, " currentPosition: ", currentPosition)
            
            if move == "U":
                if int(currentPosition["y"]) == 0:
                    currentPosition["y"] = len(self.__grid)
                currentPosition["y"] = int(currentPosition["y"] - 1)
            elif move == "D":
                if int(currentPosition["y"]) == len(self.__grid) - 1:
                    currentPosition["y"] = 0
                else:
                    currentPosition["y"] = int(currentPosition["y"] + 1)
            elif move == "L":
                if int(currentPosition["x"]) == 0:
                    currentPosition["x"] = len(self.__grid[0])
                currentPosition["x"] = int(currentPosition["x"] -1)
            elif move == "R":
                if int(currentPosition["x"]) == len(self.__grid[0]) - 1:
                    currentPosition["x"] = 0
                else:     
                    currentPosition["x"] = int(currentPosition["x"] +1)
            #record symbol for use as indicator of occupants of cell
            currentPositionSymbol = self.__grid[int(currentPosition["y"]), int(currentPosition["x"])]
            if currentPositionSymbol == 0:
                self.__grid[int(currentPosition["y"]), int(currentPosition["x"])] = 1
            elif currentPositionSymbol == 1:
                #leave same/do nothing
                self.__grid[int(currentPosition["y"]), int(currentPosition["x"])] = 1
            elif currentPositionSymbol == 2:
                #add new zombie
                self.__zombieList.append(currentPosition.copy())
                print("zombie added @ ", currentPosition)
                self.__grid[int(currentPosition["y"]), int(currentPosition["x"])] = 1
                self.__zombiePoints += 1
        print("Zombie finished @ ", currentPosition)
        self.__finalZombiePositions.append(currentPosition.copy())

    #iterate the move command for each zombie
    def run(self):
        #get each zombie on the list to complete its moves. As new zombies are added,
        #the list grows
        for zombie in self.__zombieList:
            self.zombieMove(zombie)

        #return values for output purposes
        return self.__zombiePoints, self.__finalZombiePositions

    #print the grid for positional visualization
    #can be changed to return instead of print for different types of visualizations
    def printGrid(self):
        #update the grid with all of the final zombie positions as 1s.
        #this is for visualization purposes only, and does not affect the functionality
        for position in self.__finalZombiePositions:
            self.__grid[int(position["y"]), int(position["x"])] = 1

        #print initial grid before zombies attacked
        print(self.__gridPrev)
        print("")
        print("-----------------------------")
        print("")

        #print the final grid after the aftermath
        print(self.__grid)

    
