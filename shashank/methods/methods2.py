class dog:
    def __init__(self):
        self.name="charlie"
        self.breed="huskey"
    def bark(self):
        print("dog is barking")
        self.color="black"
d1=dog()
print(d1.breed)
d1.bark()
print(d1.color)
d1.age=10
print(d1.age)
