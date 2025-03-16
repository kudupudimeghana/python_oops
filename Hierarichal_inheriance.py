#hierarichal inheriance has one parent class and multiple child classes
class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"name:{self.name},age:{self.age}")
    def eat(self):
        print("I can eat")
class Male(Human):
    def __init__(self, name, age,location):
        Human.__init__(self,name,age,)
        self.location=location
    def sleep(self):
        print("I can sleep")
class Female(Human):
    def __init__(self, name, age,can_dance):
        super().__init__(name, age)
        self.can_dance=can_dance
    def display_f(self):
        Human.display(self)
        print(f"can_dance:{self.can_dance}")
    def work(self):
        print("I can code")
female_1=Female("AAA",23,"true")
female_1.display_f()
print(female_1.age)
#male_1=Male("aaa",20,"kkd")