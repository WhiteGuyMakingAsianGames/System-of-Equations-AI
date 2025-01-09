def substitution_method(eq1, eq2):
    # Extract coefficients and constants
    a1, b1, c1 = eq1
    a2, b2, c2 = eq2
    
    # Solve for y in terms of x from the first equation
    y = (c1 - a1 * 'x') / b1
    
    # Substitute y in the second equation
    substituted_eq = a2 * 'x' + b2 * y
    
    # Solve for x
    x_solution = solve(substituted_eq - c2, 'x')
    
    # Solve for y
    y_solution = solve(eq1.subs('x', x_solution), 'y')
    
    return x_solution, y_solution

def elimination_method(eq1, eq2):
    # Extract coefficients and constants
    a1, b1, c1 = eq1
    a2, b2, c2 = eq2
    
    # Eliminate y
    factor = b2 / b1
    new_eq2 = eq2 - factor * eq1
    
    # Solve for x
    x_solution = solve(new_eq2[0] * 'x' + new_eq2[2], 'x')
    
    # Solve for y
    y_solution = solve(eq1.subs('x', x_solution), 'y')
    
    return x_solution, y_solution

def solve_linear_systems(method, eq1, eq2):
    if method == 'substitution':
        return substitution_method(eq1, eq2)
    elif method == 'elimination':
        return elimination_method(eq1, eq2)
    else:
        raise ValueError("Invalid method. Choose 'substitution' or 'elimination'.")

def main():
    # Get user input for method choice
    method = input("Choose method (substitution/elimination): ").strip().lower()
    
    # Get user input for equations
    eq1 = list(map(float, input("Enter coefficients and constant for first equation (a1 b1 c1): ").split()))
    eq2 = list(map(float, input("Enter coefficients and constant for second equation (a2 b2 c2): ").split()))
    
    # Solve the system
    try:
        x, y = solve_linear_systems(method, eq1, eq2)
        print(f"Solution: x = {x}, y = {y}")
        print("Steps:")
        # Print steps based on method
        if method == 'substitution':
            substitution_method(eq1, eq2)
        elif method == 'elimination':
            elimination_method(eq1, eq2)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
