def parse_equation(equation):
    equation = equation.replace(' ', '')
    if '=' not in equation:
        equation += "=0"
    lhs, rhs = equation.split('=')
    lhs = lhs.replace('-', '+-')
    a, b = 0, 0
    for term in lhs.split('+'):
        if 'x' in term:
            a = float(term.replace('x', ''))
        elif 'y' in term:
            b = float(term.replace('y', ''))
    c = float(rhs)
    return (a, b, c)

def substitution_method(eq1, eq2):
    a1, b1, c1 = eq1
    a2, b2, c2 = eq2
    
    # Solve for y in terms of x from the first equation
    y_expr = (c1 - a1 * 'x') / b1
    print(f"Step 1: Solve the first equation for y: y = {y_expr}")
    
    # Substitute y in the second equation
    substituted_eq = a2 * 'x' + b2 * y_expr
    print(f"Step 2: Substitute y in the second equation: {substituted_eq} = {c2}")
    
    # Solve for x
    x_solution = (c2 - b2 * y_expr) / a2
    print(f"Step 3: Solve for x: x = {x_solution}")
    
    # Solve for y using the value of x
    y_solution = y_expr
    print(f"Step 4: Substitute x back into the y equation to find y: y = {y_solution}")
    
    return x_solution, y_solution

def elimination_method(eq1, eq2):
    a1, b1, c1 = eq1
    a2, b2, c2 = eq2
    
    # Eliminate y
    factor = b2 / b1
    new_eq2 = [a2 - factor * a1, b2 - factor * b1, c2 - factor * c1]
    print(f"Step 1: Multiply equations to align coefficients: {new_eq2}")
    
    # Solve for x
    x_solution = new_eq2[2] / new_eq2[0]
    print(f"Step 2: Solve for x: x = {x_solution}")
    
    # Solve for y using the value of x
    y_solution = (c1 - a1 * x_solution) / b1
    print(f"Step 3: Substitute x back into one of the original equations to solve for y: y = {y_solution}")
    
    return x_solution, y_solution

def solve_linear_systems(method, eq1, eq2):
    if method == 'substitution':
        return substitution_method(eq1, eq2)
    elif method == 'elimination':
        return elimination_method(eq1, eq2)
    else:
        raise ValueError("Invalid method. Choose 'substitution' or 'elimination'.")

def main():
    # Explain standard form
    print("Standard form of a linear equation is Ax + By = C, where:")
    print("A is the coefficient of x")
    print("B is the coefficient of y")
    print("C is the constant term")
    
    # Explain the distributive property
    print("Distributive property: a(b + c) = ab + ac")
    
    # Get user input for method choice
    method = input("Choose method (substitution/elimination): ").strip().lower()
    
    # Get user input for equations
    eq1_input = input("Enter the first equation: ").strip()
    eq2_input = input("Enter the second equation: ").strip()
    
    # Parse equations
    eq1 = parse_equation(eq1_input)
    eq2 = parse_equation(eq2_input)
    
    # Solve the system
    try:
        x, y = solve_linear_systems(method, eq1, eq2)
        print(f"Solution: x = {x}, y = {y}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
