class Attraction():
    attraction: str = ""
    type: str = ""
    visitors: int = 0 
    length: int = 0 
    height: str = ""
 
def initialise():
    arrayAttractions = [Attraction() for i in range(26)]
    return arrayAttractions
 
def getValues(arrayAttractions):
    i = 0
    
    with open("attractions.csv") as readfile:
        line = readfile.readline(). rstrip ('\n')
        while line:
            items = line.split(",")
            
            arrayAttractions[i].attraction = items[0]
            arrayAttractions[i].type = items[1]
            arrayAttractions[i].visitors = int(items[2])
            arrayAttractions[i].length = int(items[3])
            arrayAttractions[i].height = items[4]
            
            line = readfile.readline(). rstrip('\n')
            i += 1

    return arrayAttractions

def bubbleSort(arrayAttractions):
    n = len(arrayAttractions)
    
    # traverse through all arrayAttractions elements
    for i in range(n):
        # last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the arrayAttractions 
            # swap if the element is greater than the next element
            if arrayAttractions[j].visitors < arrayAttractions[j+1].visitors:
                arrayAttractions[j], arrayAttractions[j+1] = arrayAttractions[j+1], arrayAttractions[j]
    for i in range(n):
        print(arrayAttractions[i].visitors)            
    

arrayAttractions = initialise()
arrayAttractions = getValues(arrayAttractions)
bubbleSort(arrayAttractions)
