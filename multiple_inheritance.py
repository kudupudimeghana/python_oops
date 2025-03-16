#Multiple Inheritance:Inherits properties and behaviour from multiple parent  classes
class Human:
    def __init__(self,heart):
        self.eyes=2
        self.nose=1
        self.heart=heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male():
    def __init__(self,name):
        self.name=name
    def sleep(self):
        print("I can sleep")
    def work(self):
        print("I can code")
class Boy(Human,Male):
    def __init__(self,name,heart,lang):
        Human.__init__(self,heart)
        Male.__init__(self,name)# we are specifying this function to call attributes from male class  otherwise it calls from human class based on mro order
        self.lang=lang
    def wake(self):
        print("I can wake")
    def work(self):
        print("I can test")
    def display(self):
        print(f"I am {self.name} and i teach {self.lang}")
boy_1=Boy("aaa",1,"python")
boy_1.work()# it can access the method from Boy class(MRO,method resolution order)
Male.work(boy_1)#to access the method from another parent(Male) class
print(boy_1.nose)
print(boy_1.name)#aaa
print(boy_1.lang)#python
(boy_1.display())#output:I am aaa and i teach python
