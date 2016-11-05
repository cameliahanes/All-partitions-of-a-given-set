import copy

def readElement():
    while True:
        try:
            number = int(input(""))
            return number
        except ValueError:
            print("Invalid input.")

def readArray():
    arr = []
    print("Give the number of elements: ")
    numberOfElements = int(readElement())
    print("Now give the elements: ")
    for i in range(0, numberOfElements):
        arr.append(readElement())
    return arr
'''
def everyElemIsPresent(part, arr):
    for i in range(0, len(part)):
    
        if part[i] not in arr:
            return False
    return True
'''
def partitioning(length, part, index, array):
    print (part)
    if index == len(array):
        if(length==0):
            return part;
        else:
            return [];
        

    element = array[index];
    finalR =[]
    for i in range(len(part)):
        if length > 0:
            cloneNew = copy.deepcopy(part);
            cloneNew[i].append( [element] );
            finalR.extend( partitioning( length-1, cloneNew, index+1, array ) );
        
    for elemAct in range(len(part[i])):
        cloneNew = copy.deepcopy( part );
        cloneNew[i][elemAct].append( element )
        finalR.extend( partitioning( length, cloneNew, index+1, array ) );
    return finalR

array = readArray()
print (partitioning(len(array), [[]], 0, array));
