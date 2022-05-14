# exercise file 1 for the 2015 advent of code #
import os

# import the exercise file #
file = open('./assets/2015/2015.1.txt', 'r').read()

# main function #
def mainFunction(fileInput):
  floor = 0
  basementIndex = 0

  for character in enumerate(fileInput, start = 1):
    if character[1] == '(':
      floor = floor + 1
    elif character[1] == ')':
      floor = floor - 1

      if floor == -1 and basementIndex == 0:
        basementIndex = character[0]

  return (floor, basementIndex)

# run the main function to get the result #
floor = mainFunction(file)
print(floor)