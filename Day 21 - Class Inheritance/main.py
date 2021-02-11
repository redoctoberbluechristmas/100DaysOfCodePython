
# Inheriting and modifying existing classes allows us to modify without reinventing the wheel.add

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        # Modify an inherited method.
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