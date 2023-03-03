# Initialize the lists that will be used this reducer
listMultiply1 = list()
listMultiply2 = list()
listAdd1 = list()
listAdd2 = list()
reducerTemp = list()
reducerOutput = list()

for line in open("mapperOutput.txt"):
    key, index, value = line.rstrip().split("\t")
    index, value = map(int, [index, value])
    # Convert my mapperOutput to a list
    listMultiply1.append((key, index, value))
# Reduplicate the list for the following comparison
listMultiply2 = listMultiply1
# for i in listMultiply1:
#     print(i)
# Summarize the values that need to be multiplied by each other
for i in listMultiply1:
    for j in listMultiply2:
        # Check if both lists are not in the same position
        if i != j:
            # Check if the keys are same
            if i[0] == j[0]:
                # Check if the columns are same
                if i[1] == j[1]:
                    # If the two elements have the same key and index, make and store the product of the elements
                    listAdd1.append([i[0], i[2] * j[2]])
# Remove the duplicated elements in the list
for sublist in listAdd1:
    if sublist not in listAdd2:
        listAdd2.append(sublist)
# Reduplicate the list for the following comparison
listAdd1 = listAdd2

# Summarize the values that need to be added by each other
for i in listAdd1:
    for j in listAdd2:
        # Check if both lists are not in the same position
        if i != j:
            # Check if the keys are same
            if i[0] == j[0]:
                # If the two elements have the same key, make and store the addition of the elements
                reducerTemp.append([i[0], i[1] + j[1]])
# Remove the duplicated elements in the list
for sublist in reducerTemp:
    if sublist not in reducerOutput:
        reducerOutput.append(sublist)
# Print the result of this reducer
for i in reducerOutput:
    print(i)
