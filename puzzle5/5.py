import math

input = "input.txt"

stackDesc = []
moveDesc = []
inMove = False

stacks = []

with open(input) as f:
    for line in f:
        if line.strip() == "":
            continue
        if line.strip()[0] == '1':
            inMove = True
            continue
        if inMove:
            moveDesc.append(line)
            continue
        stackDesc.append(line)

for line in stackDesc:
    if line.strip()[0] == '1':
        break
    l = len(line)
    stacksInLine = math.floor(l / 3)
    for i in range(0, stacksInLine):
        firstIndex = i*4
        secondIndex = (i+1)*4-1
        item = line[firstIndex:secondIndex]

        if len(stacks) < i+1:
            stacks.append([])

        if item.strip() != "":
            stacks[i].insert(0, item.strip())

for move in moveDesc:
    move = move.strip()
    moveSplit = move.split(' ')
    number = int(moveSplit[1])
    start = int(moveSplit[3])-1
    end = int(moveSplit[5])-1

    for i in range(0, number):
        item = stacks[start].pop()
        stacks[end].append(item)

message = ''
for i in range(0, len(stacks)-1):
    if len(stacks[i]) != 0:
        message += stacks[i].pop()

print(message.replace('[', '').replace(']', ''))
