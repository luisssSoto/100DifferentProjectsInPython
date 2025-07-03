from prettytable import PrettyTable

my_pokemons = PrettyTable()
print(my_pokemons)

pokemons = ["Pikachu", "Squirtle", "Charmander"]
types_pokemons = ["Electric", "Water", "Fire"]
my_pokemons.add_column("Pokemon Name:", pokemons)
my_pokemons.add_column("Pokemon Type:", types_pokemons)
print(my_pokemons)

# Attributes
my_pokemons.align["Pokemon Name:"] = "l"
my_pokemons.align["Pokemon Type:"] = "r"
print(my_pokemons)