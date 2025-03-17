class Instructor:
    followers=0
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def display(self,subject_name):
        print(f"HI, I am {self.name} and i teach subject_name")   
instructor_1=Instructor("jenny","kkd")
print(instructor_1.name)
instructor_1.display("python")
        
            