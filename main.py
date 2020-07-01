from world import World
import json

#loading zombieData.json
with open("zombieData.json") as f:
   data = json.load(f)

xDim = int(data["gridDimensions"]["x"])
yDim = int(data["gridDimensions"]["y"])
initialZombiePos = data["initialZombiePosition"]
civillianPositions = []
for civ in data["civillianPositions"]:
	civillianPositions.append(data["civillianPositions"][civ].copy())

zombieMoves = list(data["zombieMoves"])

#initializing world with data from zombieData.json
world = World(xDim, yDim, initialZombiePos, civillianPositions, zombieMoves)
#running world
zombiePoints, finalZombiePositions = world.run()
print("Total zombie points: ", zombiePoints)
print("Final zombie positions on the grid: ", finalZombiePositions)

#printing initial and final grid for visualization. Not neccesary for functionality
#world.printGrid()


