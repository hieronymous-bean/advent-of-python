# exercise file 2 for the 2015 advent of code #

# import the exercise file #
from cgitb import small


file = open('./assets/2015/2015.2.txt', 'r').read()

# helper functions
def calculateSurfaceArea(l, w, h):
  return (2*l*w) + (2*w*h) + (2*h*l)

def calculatePerimeter(l, w):
  return (2*l) + (2*w)

def smallestOfThree(x, y, z):
  if (x < y) and (x < z):
    return x
  
  if (y < x) and (y < z):
    return y

  if (z < x) and (z < y):
    return z

  if (x == y):
    return x
  
  if (x == z):
    return x

  if (y == z):
    return y

# main program #
def main(input):
  dimensions = input.splitlines()
  sumOfSurfaceAreas = 0

  for dimension in dimensions:
    parsedDimension = dimension.split('x')
    l = int(parsedDimension[0])
    w = int(parsedDimension[1])
    h = int(parsedDimension[2])

    orderedAreas = [l, w, h]
    orderedAreas.sort()

    sideOne = (l * w)
    sideTwo = (l * h)
    sideThree = (w * h)

    surfaceArea = calculateSurfaceArea(l, w, h)

    perimeter = calculatePerimeter(orderedAreas[0], orderedAreas[1])
    cubicFeet = (l * w * h)

    smallestSideArea = smallestOfThree(sideOne, sideTwo, sideThree)

    sumOfSurfaceAreas = sumOfSurfaceAreas + perimeter + cubicFeet

  print(sumOfSurfaceAreas)

# primary program function #
if __name__ == "__main__":
  main(file)
