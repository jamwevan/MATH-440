

# This file was *autogenerated* from the file converse_theorem.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_3 = Integer(3); _sage_const_5 = Integer(5); _sage_const_80 = Integer(80)# Import necessary components from Sage
from sage.all import *

class GaussSumTable:
    def __init__(self, q, additive_character_generator, multiplicative_character_generator):
        self.q = q
        self.additive_character_generator = additive_character_generator
        self.multiplicative_character_generator = multiplicative_character_generator
        
        self.finite_field = GF(q**_sage_const_2 )
        self.generator = self.finite_field.gen()
        self.finite_field_elements = list(self.finite_field)
        self.finite_field_multiplicative_group = [x for x in self.finite_field_elements if x != _sage_const_0 ]
        
        self.table = [[_sage_const_0  for i in range(q - _sage_const_1 )] for j in range(q**_sage_const_2  - _sage_const_1 )]
        self.compute_gauss_sum_table()

    def compute_gauss_sum_table(self):
        for theta in range(self.q**_sage_const_2  - _sage_const_1 ):
            for alpha in range(self.q - _sage_const_1 ):
                self.table[theta][alpha] = self.compute_gauss_sum(theta, alpha)

    def compute_gauss_sum(self, theta, alpha):
        total = _sage_const_0 
        for x in self.finite_field_multiplicative_group:
            additive_character_value = self.additive_character_generator**self.trace(x)
            theta_character_value = self.multiplicative_character_generator**(theta * self.log(x))
            alpha_character_value = self.multiplicative_character_generator**(alpha * self.get_norm_log(x))
            total += additive_character_value * theta_character_value * alpha_character_value
        return total

    def get_norm_log(self, x):
        return (self.q + _sage_const_1 ) * self.log(x)

    def log(self, x):
        return x.log(self.generator) if x != _sage_const_0  else _sage_const_0   # Using the logarithm in finite fields

    def trace(self, x):
        return x.trace()  # Using the field trace function from GF(q^2) to GF(q)
    
    def find_identical_rows(self):
        """
        Find groups of rows that have identical values in the Gauss sum table.
        """
        row_patterns = {}
        
        for i, row in enumerate(self.table):
            row_tuple = tuple(row)
            if row_tuple in row_patterns:
                row_patterns[row_tuple].append(i)
            else:
                row_patterns[row_tuple] = [i]
        
        identical_groups = [indices for indices in row_patterns.values()]
        # Sort by size (descending), then by first theta value (ascending) for groups of same size
        return sorted(identical_groups, key=lambda x: (-len(x), min(x)))

    def print_mod_table(self):
        """
        Print table showing the groups of theta values with identical Gauss sums.
        """
        # Get the groups of identical rows
        identical_groups = self.find_identical_rows()
        
        # Determine the mod column header based on q
        if self.q == _sage_const_3 :
            mod_header = "Mod 2"
        elif self.q == _sage_const_5 :
            mod_header = "Mod 4"
        else:
            mod_header = f"Mod {self.q-_sage_const_1 }"
        
        # Print header
        print("-" * _sage_const_80 )
        print(f"{'Theta':<20} {mod_header:<20} {'Size':<20}")
        print("-" * _sage_const_80 )

        # Print each group
        for group in identical_groups:
            # Format the theta set
            theta_str = "{" + ", ".join(map(str, sorted(group))) + "}"
            # Get the size of the group
            size = len(group)
            print(f"{theta_str:<20} {'True':<20} {size:<20}")
        
        print("-" * _sage_const_80 )

def complex_gauss_sum_table(q):
    # Convert to Sage Integer
    q = Integer(q)
    if not q.is_prime():
        raise ValueError("The number must be prime!")
    return GaussSumTable(q, exp(_sage_const_2 *pi*I/q), exp(_sage_const_2 *pi*I/(q**_sage_const_2  - _sage_const_1 )))

if __name__ == "__main__":
    # Get user input for prime number
    while True:
        try:
            q = int(input("Enter a prime number (q >= 2): "))
            if q < _sage_const_2 :
                print("Please enter a number >= 2")
                continue
            
            # Create and display the table
            gauss_sum_table_object = complex_gauss_sum_table(q)
            gauss_sum_table_object.print_mod_table()
            break
            
        except ValueError as e:
            if "must be prime" in str(e):
                print(f"Error: {q} is not a prime number. Please enter a prime number.")
            else:
                print("Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

