#7
#Crie uma classe Employee com atributos name, position e salary. Adicione um método apply_raise que aumenta o salário do 
#funcionário em uma determinada porcentagem.

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def apply_raise(self, percent):
        self.percent = percent / 100
        self.newsalary = (self.salary * self.percent) + self.salary
        return self.newsalary
    
    def show(self):
        show = print(f'{self.name}, {self.position}, que ganhava {self.salary} agora ganha {self.newsalary}')

employ1 = Employee('Renan', 'estagiário',1200)

employ1.apply_raise(10)
employ1.show()
