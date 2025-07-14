class laptop:
    def __init__(self):
        self.brand="HP"
        self.cost="60k"
    def on(self):
        print("laptop is on")

    @staticmethod
    def game():
        print("playing game in laptop")
    @classmethod
    def off(cls):
        print("laptop is off")

l1=laptop()
print(l1.brand)
l1.on()
l1.game()
l1.off()
laptop.game()
laptop.off()