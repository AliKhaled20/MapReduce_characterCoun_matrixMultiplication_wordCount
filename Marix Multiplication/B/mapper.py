# Read a file to determine the number of rows in matrix A, number of cols in matrix B
cache = open("cache.txt").readlines()[0].split(",")
row_a, col_b = map(int, cache)

#  Create an empty text file
mapperOutput = open("mapperOutput.txt", "w")
for line in open("input.txt"):
    matrix_index, row, col, value = line.rstrip().split(",")
    # Pair the key and value then store them in the text file (mapperOutput.txt) with a corresponding row or column
    if matrix_index == "A":
        for i in range(0, col_b):
            # Generate the key as the position in matrix C
            key = row + "," + str(i)
            mapperOutput.write("%s\t%s\t%s" % (key, col, value) + "\n")
    else:
        for j in range(0, row_a):
            # Generate the key as the position in matrix C
            key = str(j) + "," + col
            mapperOutput.write("%s\t%s\t%s" % (key, row, value) + "\n")
mapperOutput.close()
