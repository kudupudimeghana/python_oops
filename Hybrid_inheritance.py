#combination of two or more inheritance is said to be hybrid inheritance
class A:
    def display(self):
        print("dispaly from A class")
class B(A):
    def display(self):
        print("dispaly from A class")
class C:
    def show(self):
        print("Hi from C class")
class D(B,C):
    def display(self):
        
        print("display from D class")
        
d1=D()
d1.display()
        
        