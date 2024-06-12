def initArray(cols, rows):
    # declares and initialises a 2D array
    newArray = [[None] * cols for i in range(rows)]
    return newArray


def populateArray(arrayname, filename):
    row_counter = 0
    col_counter = 0

    with open(filename) as readfile:
        line = readfile.readline().rstrip("\n")
        while line:
            # read the lie of a file
            items = line.split(",")
            print("Items = ", items)

            # reset the col_counter to ensure first item is placed at first position of the 2D array
            col_counter = 0

            # loop for the length of the array
            for x in range(len(items)):
                # place the new values into the array a row at a time
                arrayname[row_counter][col_counter] = str(items[col_counter])

                # increment the column counter
                col_counter += 1

            # increment the row counter
            row_counter += 1
            line = readfile.readline().rstrip("\n")

        return arrayname


def calculatePercentages(array):
    # init new array for percentages
    test_percentages = initArray(14, 5)

    for x in range(1, len(array)):
        for y in range(1, len(array[x])):
            test_percentages[x - 1][y - 1] = int(array[x][y]) / int(array[0][y]) * 100

    return test_percentages


def calculateAverages(array):
    test_averages = [0] * len(array)
    total = 0

    for x in range(len(array)):
        for y in range(len(array[x])):
            total += array[x][y]
        test_averages[x] = total / len(array[x])
        total = 0

    return test_averages


test_scores = initArray(15, 6)
test_scores = populateArray(test_scores, "testscores.txt")

test_percentages = calculatePercentages(test_scores)
test_averages = calculateAverages(test_percentages)
