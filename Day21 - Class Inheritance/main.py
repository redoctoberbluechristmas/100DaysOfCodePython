
# Inheriting and modifying existing classes allows us to modify without reinventing the wheel.add

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()      # The call to super() in the initializer is recommended, but not strictly required.

    def breathe(self):
        # Extend an inherited method. Running this will produce "Inhale, exhale" \n "doing this underwater." Wont' totally override the method.
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()

# Inherit methods.
nemo.breathe()

# Inherit attributes.
print(nemo.num_eyes)