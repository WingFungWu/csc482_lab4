import os

def createList(lstName):
    try:
        f=open(lstName+".txt","x")
        f.close()
        return "List " + lstName + " has been created"
    except:
        return "List " + lstName + " already exists"

def addToList(lstName,item):
    if not checkIfFileExists(lstName):
        return "List " + lstName + " does not exist"
    f = open(lstName + ".txt", "a") 
    f.write(item+"\n")
    f.close()
    return item + " added to " + lstName

def removeFromList(lstName,item):
    if not checkIfFileExists(lstName):
        return "List " + lstName + " does not exist"
    f = open(lstName+ ".txt", "r")
    lines = f.readlines()
    f.close()
    w= open(lstName+ ".txt", "w")
    removed=False
    for l in lines:
        if l != item+"\n":
            w.write(l)
        else:
            removed=True
    w.close()   
    if removed:
        return item + " has been removed from " + lstName
    return item + " was not in " + lstName

def deleteList(lstName):
    if not checkIfFileExists(lstName):
        return "List " + lstName + " does not exist"
    os.remove(lstName +".txt")
    return lstName + " has been deleted"

def readList(lstName):
    if not checkIfFileExists(lstName):
        return "List " + lstName + " does not exist"
    f = open(lstName + ".txt", "r")
    a = f.readlines()
    f.close()
    if len(a) ==0:
        return "There is nothing in " + lstName
    else:
        return ''.join([str(item) for item in a])

def clearList(lstName):
    if not checkIfFileExists(lstName):
        return "List " + lstName + " does not exist"
    deleteList(lstName)
    createList(lstName)
    return "List " + lstName + " has been cleared" 

def checkIfFileExists(lstName):
    if os.path.exists(lstName + ".txt"):
        return True
    return False

def main():
    print(createList("toDo"))
    print(addToList("toDo", "get george from football"))
    print(addToList("toDo", "rev up that Bugattii weea"))
    print(removeFromList("toDo", "rev up that Bugattii weea"))
    print(readList("toDo"))
    print(deleteList("hello"))
    print(clearList("hello"))
    print(deleteList("toDo"))

