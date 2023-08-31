#6
#Desenvolva uma classe Book com atributos title, author e year. Implemente um método get_age que retorna quantos anos o 
#livro tem desde o ano atual.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_age(self):
        return print(f'The {self.title}, write by {self.author} in {self.year}, have {2023 - self.year} years.')
    
def main():
    title = input('Write the book title: ')
    author = input('Write the book author: ')
    year = int(input('Write the book year: '))

    book1 = Book(title, author, year)
    book1.get_age()

main()