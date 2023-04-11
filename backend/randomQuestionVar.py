import random
import re
import string

def generate_equation():
    num_terms = random.randint(3, 4)
    terms = []

    for _ in range(num_terms):
        term = random.randint(1, 9) if random.randint(0, 1) else -random.randint(1, 9)
        terms.append(term)

    equation = f"{terms[0]}X"

    for i in range(1, num_terms - 1):
        equation += f" {'+' if terms[i] >= 0 else '-'} {abs(terms[i])}"

    equation += f" = {terms[-1]}X"

    answer = solve_equation(equation)
    return {"problem": equation, "answer": answer}

def solve_equation(equation):

    left_x_values = []
    right_x_values = []
    left_constants = []
    right_constants = []
    left_test = []

    # Split the equation into left and right sides
    left, right = equation.split("=")

    #gets values split up into different lists
    left_x_values = [int(x_val) for x_val in re.findall("(-?\d*)X", left)]
    #left_constants = [int(constant) for constant in re.findall("([+-]?\d+)(?!\s*\d*X)", left)]
    left_test = re.findall("(\W+\d+)(?!\s*\d*X)(?!\D+\d*X)", left)
    left_constants = [int(s.translate({ord(c): None for c in string.whitespace})) for s in left_test]

    #groups x values together
    right_x_values = [int(x_val) for x_val in re.findall("(-?\d*)X", right)]

    #group constants together
    left_constant_total = 0
    for x in left_constants:
        left_constant_total += x

    #print("Left X values:", left_x_values)
    #print("Right X values:", right_x_values)
    #print("Left constants:", left_constants)
    
    #print("Right constants:", right_constants)
    #print("Left test:", integer_array)

    x_values_total = right_x_values[0] - left_x_values[0]
    #print(left_constant_total)
    #print(x_values_total)

    #divide constants by X values to get answer
    answer = left_constant_total / x_values_total
    return round(answer,2) #Return answer rounded to 2 decimal places

if __name__ == "__main__":
    print(generate_equation())