class Students():
    no_of_total_students_in_BSSE=30

    def __init__(self,name,std_ID,Dep):
        self.name=name
        self.std_ID=std_ID
        self.dep=Dep

    def print_student_details(self):
        return f"Student Name is {self.name}\nStudent ID is {self.std_ID}\nStudent Department is {self.dep}"

    @staticmethod
    def print_some():
        return f"This is my Students"





Faiza=Students("Faiza",234,"BSCS")
Saad=Students("Saad",224,"BSSE")
Umair=Students("Umair",934,"BBA")

# print(Saad.print_student_details())
# print(Faiza.print_student_details())
print(Faiza.print_some(),"\n",Faiza.print_student_details())