fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie.")
    else:
        print(f"{fruit} Pie.")

make_pie(int(input("What kind of pie do you want? Apple=0, Pear=1, Orange=2: ")))