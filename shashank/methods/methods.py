class Employee:
    def __init__(self):
        self.name="shahank"
        self.age=26
        self.sal=10000
    def work(self):
        print("shashank is teaching")
        print(self)
        print(self.age)
e1=Employee()
print(e1.name)
e1.work()
print(e1)

print(e1.age)