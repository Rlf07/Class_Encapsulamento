#5
#Defina uma classe Car com atributos make, model e year. 
#Crie um método start_engine que imprime uma mensagem indicando que o motor foi iniciado.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print(f'O carro {self.make} do modelo {self.model} do ano {self.year} foi iniciado.')

def main():
    make = input('Say the car make: ')
    model = input('Say the car model: ')
    year =input('Say the car year: ')

    car1 = Car(make, model, year)

    car1.start_engine()

main()
