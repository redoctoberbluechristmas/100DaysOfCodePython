################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


# Local Scope
# When creating a new variable or function inside a function, it is only accessible inside that function.
# Start thinking about global scope if you want it to be accessible outside the function.

def drink_potion():
    
# Global Scope

# Player health has global scope (available anywhere in file), because it was defined at top level of file.

# Namespace: Global and local scope applies to anything you name, due to a concept called namespace.
# Anything that you give a name to has a namespace.

def game():
    def drink_potion():
        potion_strength = 2
        print(potion_strength)
# drink_potion() will error out, because it is not defined globally. Now that it is nested inside a function, game,
# it has local namespace.

drink_potion()

############

# Does Python have Block Scope?  (NO) 
# If you were to create a variable inside a code block, it doesn't count as a "fence" in Python


game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)  # the new_enemy variable defined in the if block is still globally accessible
# But it won't be accessible inside a function.

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def make_enemy():
    if game_level < 5:
        new_enemy = enemies[0]
# This won't work
print(new_enemy)


# How to Modify a Global Variable

# This won't work, because you're actually creating two separate variables called "enemies."
# They're different because they have different namespaces; the one equal to 1 has global namespace,
# the one equal to 2 is local to the increase_enemies function.

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Modify a global variable

enemies = 1

def increase_enemies():
    global enemies         # <----- Let the program know there's a global variable named 'enemies' - that's the var you want to use.
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")4

# Avoid modifying global scope within a function with local scope (can introduce bugs)

# Instead, return the value from a function, then assign the global value the return value.

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()    # make sure to save the variable to the global variable.
print(f"enemies outside function: {enemies}")


# Global scope can be useful in defining constants.
# Global constants are values which you define, and never plan on changing again.

# Convention in Python is to denote constants by all caps var name
PI = 3.14159
URL = "https://www.google.com"

