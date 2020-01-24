# BogoSort is sorting by random shuffler.

from random import randint
from random import shuffle

# Variables
NumbersArray = [] # Empty array that must be sorted.
ArrayRange = int(input("Enter range of your array: ")) # How many elements will array contain
IterationsCount = 0
Counter = 0

# Numbers' generation
for element in range(ArrayRange):
    element = randint(-100, 100)
    NumbersArray.append(element)
print("Well, there's your array: " + str(NumbersArray))

# Functions
def isSorted(): # Returns True or False if the array is sorted or it isn't
    global Counter
    Counter = 0
    for element in NumbersArray: # [-5, 5, -10, 1, 25]
        if (Counter != len(NumbersArray) - 1): # For no "index out of range" exception
            if (NumbersArray[Counter] > NumbersArray[Counter + 1]): # Comparing of two numbers
                return False
                break
            else:
                Counter += 1
        elif (Counter == len(NumbersArray) - 1):
            return True
def iteration(): # A single shuffling of the array
    global IterationsCount
    IterationsCount += 1
    shuffle(NumbersArray)
    print("Iteration " + str(IterationsCount) + ". Your array is " + str(NumbersArray))
# Sorting condition
while(1==1):
    if (isSorted() == False):
        iteration()
    else:
        print("There's your sorted array, it took " + str(IterationsCount) + " iterations.")
        print(NumbersArray)
        break



