input = "input.txt"

calList = []
top = 3

with open(input) as f:
    currentCal = 0
    for line in f:
        if line.strip() == "":
            calList.append(currentCal)
            currentCal = 0
        else:
            currentCal += int(line)
    if currentCal > 0:
        calList.append(currentCal)

sortedCalList = sorted(calList, reverse=True)
print(sortedCalList)

sumTop = 0
for i in range(0, top):
    print(sortedCalList[i])
    sumTop += sortedCalList[i]

print("Calories of top three elves: ", str(sumTop))