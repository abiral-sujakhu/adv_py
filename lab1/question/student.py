# student class 
#  attribute name, roll,marks( make dictionary ) 
# method-->display

class student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks  #must be in dictionary{"math":90}
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        for key, value in self.marks.items():
            print(f"{key}: {value}")