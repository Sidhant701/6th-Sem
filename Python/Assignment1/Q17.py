print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')

species = "Global Species"

class Animal:
    species = "Class Species"

    def __init__(self, species):
        self.species = species

    def display_species(self):
        print(f"Instance species: {self.species}")
        print(f"Class species: {Animal.species}")
        print(f"Global species: {globals()['species']}")

a = Animal("Instance Species")
a.display_species() 

# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# Instance species: Instance Species
# Class species: Class Species
# Global species: Global Species

'''
Explaination:- (Scope Resolution Process, Step by Step)
In Python, scope resolution follows LEGB(Local, Enclosing, Global, Built-in) rule.
- Local scope: The local scope is the scope of the current function or method.
- Enclosing scope: The enclosing scope is the scope of the outer function or method.
- Global scope: The global scope is the scope of the global variables.
- Built-in scope: The built-in scope is the scope of the built-in functions and variables.
'''