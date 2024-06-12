import random 

rows = 4
cols = 5

def initArray():
    # declares and initialises a 4 by 5 2D array 
    newArray = [[None]*cols for i in range(rows)]
    return newArray

def populateArray(arrayname):
    for x in range(rows):
        for y in range(cols):
            arrayname[x][y] = random.randint(1,20)
    
    return arrayname

def print2dArray(arrayname):
    # prints out each row at a time with commas 
    # doesn't need to know the rows / cols 
    row = ""
    for x in range(len(arrayname)):
        for y in range(len(arrayname[x])):
            row += str(arrayname[x][y]) + ","

        # removes the last comma by extracting all minus the last char 
        row = row[:-1]
        print(row)
        row = ""
    print()

def linearSearch(arrayname): 
    num = int(input("Enter num to find:"))
    num_cols = len(arrayname) 
    count = 0 
    found = False
    
    while found == False and count < num_cols: 
        for y in range(len(arrayname[count])):
            if num == arrayname[count][y]:
                print("Position of number is at:", count, ",", y)
                found = True 
        count += 1 

ticketArray = initArray() 
ticketArray = populateArray(ticketArray)
print2dArray(ticketArray)
linearSearch(ticketArray)