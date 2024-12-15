buffer = ""
with open("input.txt") as file:
    while line := file.readline():
        buffer += line
        
# E -> enable, D -> disable, INT -> mul instruction result
instructionBuffer = [""] * len(buffer)

def parseInstructionType(tokenList: str, instToken: str):
    instructionBufferIdx = 0
    tokenListIdx = 0
    
    mulLeft = 0
    mulRight = 0
    
    i = 0
    while i < len(buffer):
        c = buffer[i]
        if tokenList[tokenListIdx] == "0" or tokenList[tokenListIdx] == "1": # Look for number
            if not c.isdigit():
                tokenListIdx = 0
            else:
                number = c
                subBuffer = buffer[i+1:]
                for j in range(len(subBuffer)):
                    if subBuffer[j].isdigit():
                        number += subBuffer[j]
                    else:
                        break
                if len(number) < 4:
                    if tokenList[tokenListIdx] == "0":
                        mulLeft = int(number)
                    else:
                        mulRight = int(number)
                else:
                    tokenListIdx = 0
                tokenListIdx += 1
                i += j
        else:
            if tokenList[tokenListIdx] == c:
                tokenListIdx += 1
            else:
                tokenListIdx = 0
        
        if tokenListIdx == len(tokenList): # We've got a match
            if instToken == "INT":
                instructionBuffer[instructionBufferIdx] = str(mulLeft * mulRight)
            else:
                instructionBuffer[instructionBufferIdx] = instToken
            tokenListIdx = 0
            
        if tokenListIdx == 0:
            instructionBufferIdx = i + 1
        
        i += 1

parseInstructionType("mul(0,1)", "INT")
parseInstructionType("do()", "E")
parseInstructionType("don't()", "D")

sum = 0
enabled = True
for instr in instructionBuffer:
    if instr == "E":
        enabled = True
    elif instr == "D":
        enabled = False
    if instr.isdigit() and enabled:
        sum += int(instr)
    
print("Sum: ", sum)