

def add(*args):
    print(args[0])

    my_sum = 0
    for n in args:
        my_sum += n
    return my_sum


def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    # By filtering by input name, you can find the input you want, and do something to it.
    #print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]


my_car = Car(make="Nissan", model="GT-R")

print(my_car.model)