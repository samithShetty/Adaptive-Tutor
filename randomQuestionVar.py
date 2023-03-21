import random
import re

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

    return equation

def solve_equation(equation):
    # Split the equation into left and right sides
    left, right = equation.split("=")

    # Define regular expressions to find coefficients and constants
    coef_pattern = re.compile(r"([+\-]?[0-9]?)X")
    const_pattern = re.compile(r"([+\-]?[0-9]+)")

    # Extract coefficients and constants
    left_coefs = [int(x) if x != "" else 1 for x in coef_pattern.findall(left)]
    left_consts = [int(x) for x in const_pattern.findall(left)]

    right_coefs = [int(x) if x != "" else 1 for x in coef_pattern.findall(right)]
    right_consts = [int(x) for x in const_pattern.findall(right)]

    # Calculate the final coefficients and constants
    final_coef = sum(left_coefs) - sum(right_coefs)
    final_const = sum(right_consts) - sum(left_consts)

    # Check if the equation has a unique solution, no solution or infinite solutions
    if final_coef == 0 and final_const == 0:
        return("Infinite solutions")
    elif final_coef == 0:
        return("No solution")
    else:
        x = final_const / final_coef
        return(x)

def main():
    equation = generate_equation()
    xValue = solve_equation(equation)

    print(equation)
    print(xValue)

    

if __name__ == "__main__":
    main()
