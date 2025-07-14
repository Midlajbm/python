class animal:
    def eat(self):
        print("Animal is eating")
    def sleep(self):
        print("Animal is sleeping")
    def drink(self):
        print("Animal is drinking")
        


class dog(animal):
    pass
class lion(animal):
    pass 
class tiger(animal):
    pass

d1=dog()
l1=lion()
t1=tiger()

d1.eat()
d1.sleep()
d1.drink()

l1.eat()
l1.sleep()
l1.drink()

t1.eat()
t1.sleep()
t1.drink()


