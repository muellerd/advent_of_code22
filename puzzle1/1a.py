input = "input.txt"

maxCal = 0

with open(input) as f:
    currentCal = 0
    for line in f:
        if line.strip() == "":
            if currentCal > maxCal:
                maxCal = currentCal
            currentCal = 0
        else:
            currentCal += int(line)

print("Max. calories: ", str(maxCal))
