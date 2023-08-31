#4
#Crie uma classe Student com atributos name, age e grades (uma lista). 
#Adicione métodos para adicionar notas, calcular a média das notas e exibir as informações do aluno.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self,grade):
        self.grades.append(grade)

    def c_avarage(self):
        total = sum(self.grades)
        average = total / len(self.grades)
        return average

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print("Grades:", *self.grades)
        print(f"Average Grade: {self.c_avarage()}")

student_name = input("Enter student's name: ")
student_age = int(input("Enter student's age: "))
student1 = Student(student_name, student_age)

for i in range(4):
    grade = float(input(f"Enter grade {i+1}: "))
    student1.add_grade(grade)

student1.show_info()



    