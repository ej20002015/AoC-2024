def isSafe(report: list, final=False):
    safe = True
    prevValue = int(report[0])
    alwaysGT = True
    alwaysLT = True
    for i in range(1, len(report)):
        alwaysGT &= prevValue < int(report[i])
        alwaysLT &= prevValue > int(report[i])
        if not alwaysGT and not alwaysLT:
            # safe = isSafe(report[:i] + report[i+1:], True) if not final else False
            safe = False
            break
        
        diff = abs(int(prevValue) - int(report[i]))
        prevValue = int(report[i])
        if diff < 1 or diff > 3:
            # safe = isSafe(report[:i] + report[i+1:], True) if not final else False
            safe = False
            break
    
    # Try removing each value
    if not final:
        i = 0
        while not safe and i < len(report):
            safe = isSafe(report[:i] + report[i+1:], True)
            i += 1
    
    return safe
    

numReportsSafe = 0

with open("input.txt") as f:
    while line := f.readline():
        report = line.split()
        if isSafe(report):
            numReportsSafe += 1
        
print(numReportsSafe)
                
        