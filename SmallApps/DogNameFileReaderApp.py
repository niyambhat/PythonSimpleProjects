# Python function to select a random name from a text file by converting it into a list

import random
f= open("names.txt","r")
dogNamesList = f.read()
dogNamesList = dogNamesList.split("\n")
randomName = random.choice(dogNamesList)
print(randomName)