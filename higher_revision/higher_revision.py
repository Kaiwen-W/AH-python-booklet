class Data():
    email: str = ""
    forename: str = ""
    surname: str = ""
    percent: float = 0.0
 
def getData():
    arrayPupils = [Data() for x in range(62)]
    i = 0
    with open("rawpupildata.csv") as readfile:
        line = readfile.readline().rstrip('\n')
        while line:
            items = line.split(",")
            arrayPupils[i].email = items[0]
            arrayPupils[i].forename = items[1]
            arrayPupils[i].surname = items[2]
            arrayPupils[i].percent = float(items[3])
            line = readfile.readline().rstrip('\n')
            i += 1
    return arrayPupils

arrayPupils = getData()