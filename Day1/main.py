# Read in line by line
# Split by space and place into two lists

leftList = []
rightList = []

with open("input.txt") as file:
    while line := file.readline():
        parts = line.split()
        leftList.append(parts[0])
        rightList.append(parts[1])
        
leftList.sort()
rightList.sort()

distance = 0
for l, r in zip(leftList, rightList):
    distance += abs(int(l) - int(r))
    
print(distance)