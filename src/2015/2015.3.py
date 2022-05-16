# exercise file 3 for the 2015 advent of code #

# import the exercise file #
file = open('./assets/2015/2015.3.txt', 'r').read()

# helper functions #
def moveNorth(currentPosition):
  currentX = currentPosition[0]
  currentY = currentPosition[1]

  newX = currentX
  newY = currentY + 1

  return [newX, newY]

def moveSouth(currentPosition):
  currentX = currentPosition[0]
  currentY = currentPosition[1]

  newX = currentX
  newY = currentY - 1

  return [newX, newY]

def moveEast(currentPosition):
  currentX = currentPosition[0]
  currentY = currentPosition[1]

  newX = currentX + 1
  newY = currentY

  return [newX, newY]

def moveWest(currentPosition):
  currentX = currentPosition[0]
  currentY = currentPosition[1]

  newX = currentX - 1
  newY = currentY

  return [newX, newY]

def existsInArray(array, value):
  for item in array:
    if item == value:
      return 1

  return 0

def isEven(n):
  return n % 2 == 0

def isOdd(n):
  return n % 2 != 0

# primary parsing function for part one #
def parseCoordinateDataOne(input):
  startingLocation = [0, 0]
  visitedLocations = [[0,0]]

  currentPosition = startingLocation

  for coordinate in input:

    if coordinate == "^":
      currentPosition = moveNorth(currentPosition)

    if coordinate == "v":
      currentPosition = moveSouth(currentPosition)

    if coordinate == ">":
      currentPosition = moveEast(currentPosition)
    
    if coordinate == "<":
      currentPosition = moveWest(currentPosition)

    alreadyVisited = existsInArray(visitedLocations, currentPosition)
    if alreadyVisited != 1:
      visitedLocations.append(currentPosition)

  print(len(visitedLocations))

def parseCoordinateDataTwo(input):
  startingLocation = [0, 0]
  
  santaLocation = startingLocation
  robotLocation = startingLocation

  visitedLocations = [[0,0]]

  for item in enumerate(input, start = 1):

    # move north
    if item[1] == '^':

      if isEven(item[0]):
        santaLocation = moveNorth(santaLocation)
        if existsInArray(visitedLocations, santaLocation) != 1:
          visitedLocations.append(santaLocation)

      elif isOdd(item[0]):
        robotLocation = moveNorth(robotLocation)
        if existsInArray(visitedLocations, robotLocation) != 1:
          visitedLocations.append(robotLocation)

    # move south
    if item[1] == 'v':

      if isEven(item[0]):
        santaLocation = moveSouth(santaLocation)
        if existsInArray(visitedLocations, santaLocation) != 1:
          visitedLocations.append(santaLocation)

      elif isOdd(item[0]):
        robotLocation = moveSouth(robotLocation)
        if existsInArray(visitedLocations, robotLocation) != 1:
          visitedLocations.append(robotLocation)

    # move south
    if item[1] == '>':

      if isEven(item[0]):
        santaLocation = moveEast(santaLocation)
        if existsInArray(visitedLocations, santaLocation) != 1:
          visitedLocations.append(santaLocation)

      elif isOdd(item[0]):
        robotLocation = moveEast(robotLocation)
        if existsInArray(visitedLocations, robotLocation) != 1:
          visitedLocations.append(robotLocation)

    # move west
    if item[1] == '<':

      if isEven(item[0]):
        santaLocation = moveWest(santaLocation)
        if existsInArray(visitedLocations, santaLocation) != 1:
          visitedLocations.append(santaLocation)

      elif isOdd(item[0]):
        robotLocation = moveWest(robotLocation)
        if existsInArray(visitedLocations, robotLocation) != 1:
          visitedLocations.append(robotLocation)
  
  print(len(visitedLocations))



parseCoordinateDataTwo(file)