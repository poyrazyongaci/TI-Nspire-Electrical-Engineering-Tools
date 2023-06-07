from sympy import symbols, Function

# Define the symbols for the variables
x = symbols('x')
f = Function('f')(x)

# Create a list of x values
x_values = [1, 2, 3, 4, 5]

# Calculate the corresponding f(x) values
f_values = [2*x**2 - 3*x + 1 for x in x_values]

# Create a table
table = [[x, f] for x, f in zip(x_values, f_values)]

# Display the table
table_header = ["x", "f(x)"]
table_data = [table_header] + table

# Print the table
for row in table_data:
    print("\t".join(str(cell) for cell in row))
