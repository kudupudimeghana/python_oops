#multilevel_inheritance:child class inherits properties from parent class ,parent class inherits properties from another parent class
class Human:
    def __init__(self,heart):
        self.eyes=2
        self.heart=heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male(Human):
    def __init__(self,name):
        self.name=name
    def sleep(self):
        print("I can sleep")
    def work(self):
        print("I can code")
class Boy(Male):
    def __init__(self,heart,name,can_dance):
        Human.__init__(self,heart)
        Male.__init__(self,name)
        self.know_dancing=can_dance
    def work(self):
        #Human.work(self)
        print("I can test")
boy_1=Boy(1,"aaa","true")
boy_1.work()
print(boy_1.name)
print(boy_1.know_dancing)
    