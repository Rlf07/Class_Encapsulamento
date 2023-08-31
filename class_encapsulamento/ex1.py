#Exercícios Básicos de Classes e Encapsulamento:
#1
#Crie uma classe chamada Person com atributos name e age, e um método display_info que imprime o nome e a idade da pessoa.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f'Seu nome é {self.name} e sua idade é {self.age}')

person1 = Person('Renan',26)
person2 = Person('Michael',26)

print(person1.display_info())
print(person2.display_info())
        