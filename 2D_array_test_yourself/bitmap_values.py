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
                arrayname[row_counter][col_counter] = int(items[col_counter])

                # increment the column counter
                col_counter += 1

            # increment the row counter
            row_counter += 1
            line = readfile.readline().rstrip("\n")

        return arrayname


bitmap_values = initArray(8, 8)
bitmap_values = populateArray(bitmap_values, "bitmap.csv")
