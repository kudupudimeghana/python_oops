# single Inheritance : one child  class inherits properties from one parent class
class Human:
    def __init__(self,heart):
        self.eyes=2
        self.nose=1
        self.heart=heart
    def eat(self):
        print("I can eat")
    def work(self):
        print(" I can work")
class Male(Human):
    def __init__(self,name,heart):
        super().__init__(heart)# we have to  call this superfunction to access the attributes from parent class ,in case of own __init__ function
        self.name=name
    def sleep(self):
        print("male can sleep")
    def work(self):
        super().work() #this super function is used to access the methods and attributes from parentclass
        print("I can code")
    def display(self):
        print(f"Hi, I am {self.name} and I have {self.heart},heart")
male_1=Male("xyz",1)
male_1.eat() #we can access eat method from human class by using male class object this is single inheritance
male_1.work()#over ridding method ,output:I can work (this is from super class)
print(male_1.eyes) #output:2,we haven't define any attribute in male but it accessing from parent class
print(male_1.name)# output:aaaa
print(male_1.heart)#output:1
print(male_1.display())#output:Hi, I am xyz and I have 1,heart