#8
#Defina uma classe TemperatureConverter com métodos para converter de Celsius para Fahrenheit e vice-versa. 
#Mantenha os atributos e métodos privados.

  
class TemperatureConverter:
    def __init__(self):
        pass

    def __cel_to_fa(self, celsius):
        return (celsius * 9/5) + 32

    def __fa_to_cel(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

    def convert_to_fahrenheit(self, celsius):
        return self.__cel_to_fa(celsius)

    def convert_to_celsius(self, fahrenheit):
        return self.__fa_to_cel(fahrenheit)

converter = TemperatureConverter()

def main():
    celsius_temp = float(input("Say in Celsius: "))
    fahrenheit_result = converter.convert_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp}°C is {fahrenheit_result}°F")

    fahrenheit_temp = float(input("Say in Fahrenheit: "))
    celsius_result = converter.convert_to_celsius(fahrenheit_temp)
    print(f"{fahrenheit_temp}°F is {celsius_result}°C")

main()
