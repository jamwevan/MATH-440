

# This file was *autogenerated* from the file GaussSumTable.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1)
from sage.all import GF, e, pi, I, latex, is_prime  # Import required functions

class GaussSumTable:
    def __init__(self, q, additive_character_generator, multiplicative_character_generator):
        self.q = q
        self.additive_character_generator = additive_character_generator
        self.multiplicative_character_generator = multiplicative_character_generator

        self.finite_field = GF(q**_sage_const_2 )  # Corrected exponentiation syntax
        self.generator = self.finite_field.gen()
        self.finite_field_elements = list(self.finite_field)
        self.finite_field_multiplicative_group = [x for x in self.finite_field_elements if x != _sage_const_0 ]

        self.table = [[_sage_const_0  for _ in range(q - _sage_const_1 )] for _ in range(q**_sage_const_2  - _sage_const_1 )]
        self.compute_gauss_sum_table()

    def compute_gauss_sum_table(self):
        for theta in range(self.q**_sage_const_2  - _sage_const_1 ):
            for alpha in range(self.q - _sage_const_1 ):
                self.table[theta][alpha] = self.compute_gauss_sum(theta, alpha)

    def compute_gauss_sum(self, theta, alpha):
        total = _sage_const_0 
        for x in self.finite_field_multiplicative_group:
            additive_character_value = self.additive_character_generator ** self.trace(x)
            theta_character_value = self.multiplicative_character_generator ** (theta * self.log(x))
            alpha_character_value = self.multiplicative_character_generator ** (alpha * self.get_norm_log(x))
            total += additive_character_value * theta_character_value * alpha_character_value
        return total

    def get_norm_log(self, x):
        return (self.q + _sage_const_1 ) * self.log(x)

    def log(self, x):
        return x.log(self.generator) if x != _sage_const_0  else _sage_const_0 

    def trace(self, x):
        return x.trace()

def complex_gauss_sum_table(q):
    if not is_prime(q):  # Ensure q is a prime number
        raise ValueError("Expected a prime number!")
    return GaussSumTable(q, e ** (_sage_const_2  * pi * I / q), e ** (_sage_const_2  * pi * I / (q**_sage_const_2  - _sage_const_1 )))

def save_gauss_sum_table_as_html(table, filename="GaussSumTable.html"):
    """
    Saves the Gauss sum table in an HTML file with MathJax LaTeX rendering and uniquely highlights groups of matching rows.
    """
    # Generate a list of distinct colors for groups of matching rows
    colors = [
        "#d1ffd1", "#d1e7ff", "#ffd1d1", "#fff7d1", "#d1fff5", "#ffd1f9", "#e1d1ff", "#ffd9d1"
    ]  # Extend this list if needed

    # Identify unique row groups and assign a color to each
    unique_rows = list({tuple(row) for row in table})  # Get unique rows
    color_map = {unique_row: colors[i % len(colors)] for i, unique_row in enumerate(unique_rows)}

    with open(filename, "w") as f:
        f.write("<html><head><title>Gauss Sum Table</title>\n")
        f.write('<script type="text/javascript" async '
                'src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?'
                'config=TeX-AMS-MML_HTMLorMML"></script>\n')
        f.write('<style>table { border-collapse: collapse; width: 100%; }')
        f.write('th, td { border: 1px solid black; padding: 5px; text-align: center; font-size: 18px; }')
        f.write('th { background-color: #f2f2f2; }')
        # Generate CSS classes for each color
        for unique_row, color in color_map.items():
            f.write(f'.color-{color.replace("#", "")} {{ background-color: {color}; }}\n')
        f.write("</style>\n</head><body>\n")

        f.write("<h2>Gauss Sum Table</h2>\n")
        f.write('<div style="overflow-x:auto;">')  # Scrollable if needed
        f.write('<table>\n')

        # Header row
        f.write("<tr><th>\\( \\theta \\backslash \\alpha \\)</th>")
        for alpha in range(len(table[_sage_const_0 ])):
            f.write(f"<th>\\( \\alpha = {alpha} \\)</th>")
        f.write("</tr>\n")

        # Data rows with LaTeX rendering
        for theta, row in enumerate(table):
            # Get the color associated with the unique row
            row_color = color_map[tuple(row)]
            row_class = f"color-{row_color.replace('#', '')}"  # CSS class for the row

            f.write(f"<tr class='{row_class}'><td>\\( {theta} \\)</td>")
            for value in row:
                f.write(f"<td>\\( {latex(value)} \\)</td>")
            f.write("</tr>\n")

        f.write("</table>\n</div>\n</body></html>\n")

    print(f"Saved Gauss Sum Table as {filename}")

def main():
    # Ask the user for a prime number
    while True:
        try:
            user_input = int(input("Enter a prime number (q >= 2): "))
            if user_input < _sage_const_2  or not is_prime(user_input):  # Check if the number is prime
                raise ValueError("The number entered is not a prime number or is less than 2.")
            break
        except ValueError as e:
            print(e)
            print("Please enter a valid prime number (q >= 2).")

    # Generate the Gauss Sum Table using user input
    gauss_sum_table_object = complex_gauss_sum_table(user_input)
    table_of_gauss_sum = gauss_sum_table_object.table

    # Save as an HTML file
    save_gauss_sum_table_as_html(table_of_gauss_sum)

# Run the program
if __name__ == "__main__":
    main()

