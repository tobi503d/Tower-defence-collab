

#       ------------------------------ Example u need ------------------------------

#       --- class ---
class example:
    def __init__(self, ID_):
        self.ID = ID_   #self.variable means u can use the variable outside of the class, if u substitute self with the object

    def heal():
        pass

#       --- stores the objects
objectList = []

#       --- Makes x_ amount of objects of example ---
x_ = 5
for x in range(X_):
    newID = objectList[-1].ID + 1 #objectList[x] is the object here
    exampleObject = example(newID) #creates a new oblect by calling example (the class/blueprint) and class is like "wtf is it's ID?"
    objectList.append(exampleObject) #now the new object gets added to a list of objects

#       --- Makes object when called ---
def makeObject():
    newID = objectList[-1].ID + 1 # this all does the same as the previous function but only once
    exampleObject = example(newID) # this all does the same as the previous function but only once
    objectList.append(exampleObject) # this all does the same as the previous function but only once

makeObject() # calls the function that makes an object

#       --- Use objects ---
for x in range(len(objectList)):
    objectList[x].heal() #loops through the list of objects and calls the function heal

#       --- Differentiate between different objects ---
def onContact(obj): # obj is just a placeholder right here
    print(f"Hit object with the ID: {obj.ID}") # the object could be a zombie but bc it comes from a class, we know the ID, otherwise it wouldn't exist

Temp_basicEnemy = example(1)
Temp_speedEnemy = example(2)

onContact(Temp_basicEnemy) # this is the obj hit

onContact(Temp_speedEnemy) # this is the obj hit
