class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def display_info(self):
        print(f"Name: {self._name}")
        print(f"Salary: ${self._salary:.2f}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self._department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self._department}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self._programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self._programming_language}")

# Criando instâncias de diferentes tipos de funcionários
manager = Manager("Alice Manager", 75000, "Human Resources")
developer = Developer("Bob Developer", 60000, "Python")

# Exibindo informações dos funcionários
manager.display_info()
print("\n")
developer.display_info()
