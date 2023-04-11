import random

#Order of Operations equations

 #vars for solving the equation
termsSolve = [0, 0, 0, 0]
operationsSolve = ['P', 'P', 'P', 'P']
terms = random.randrange(3)+2
#random amount of terms to multiply

def generate_equation():

    operations = ['x', '-', '+'] #add back division later

    equation = ""
    
    for x in range(terms):
        termsSolve[x] = random.randrange(100)
        #print(termsSolve[x], end = " ")
        equation += str(termsSolve[x]) + " " #added 
        random.shuffle(operations)
        operationsSolve[x] = operations[0]
        if x < terms -1:
            #print(operations[0], end = " ")
            equation += str(operations[0]) + " "


    return equation
#solve the equation
#need to fix order of operations

def solve_equation(equation):
    currentSolution = 0
    if operationsSolve[0] == 'x':
        currentSolution = termsSolve[0] * termsSolve[1]
    elif operationsSolve[0] == '-':
        currentSolution = termsSolve[0] - termsSolve[1]
    elif operationsSolve[0] == '+':
        currentSolution = termsSolve[0] + termsSolve[1]

    for x in range(1, terms-1):
        if operationsSolve[x] == 'x':
            currentSolution = currentSolution * termsSolve[x+1]
        elif operationsSolve[x] == '-':
            currentSolution = currentSolution - termsSolve[x+1]
        elif operationsSolve[x] == '+':
            currentSolution = currentSolution + termsSolve[x+1]
        #print(currentSolution)
    return currentSolution
#print(currentSolution)


def main():
    equation = generate_equation()
    xValue = solve_equation(equation)
    #xValueRound = round(xValue, 2)

    print(equation)
    print(xValue)
    #print(xValueRound)

    

if __name__ == "__main__":
    main()