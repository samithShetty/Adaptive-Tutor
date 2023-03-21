import random

#Order of Operations equations

operations = ['x', '-', '+'] #add back division later

#vars for solving the equation
termsSolve = [0, 0, 0, 0]
operationsSolve = ['P', 'P', 'P', 'P']



#random amount of terms to multiply
terms = random.randrange(3)+2
for x in range(terms):
    termsSolve[x] = random.randrange(100)
    print(termsSolve[x], end = " ")
    random.shuffle(operations)
    operationsSolve[x] = operations[0]
    if x < terms -1:
        print(operations[0], end = " ")

#solve the equation
#need to fix order of operations

currentSolution = 0
if operationsSolve[0] == 'x':
    currentSolution = termsSolve[0] * termsSolve[1]
elif operationsSolve[0] == '-':
    currentSolution = termsSolve[0] - termsSolve[1]
#elif operationsSolve[0] == '/':
#    currentSolution = termsSolve[0] / termsSolve[1]
elif operationsSolve[0] == '+':
    currentSolution = termsSolve[0] + termsSolve[1]

for x in range(1, terms-1):
    if operationsSolve[x] == 'x':
        currentSolution = currentSolution * termsSolve[x+1]
    elif operationsSolve[x] == '-':
        currentSolution = currentSolution - termsSolve[x+1]
    #elif operationsSolve[x] == '/':
    #    currentSolution = currentSolution / termsSolve[x+1]
    elif operationsSolve[x] == '+':
        currentSolution = currentSolution + termsSolve[x+1]
    print(currentSolution)

print(currentSolution)