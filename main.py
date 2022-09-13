# from abc import ABC, abstractmethod
import SortingAlgorithm
from SortingAlgorithm import fib

def show_name(*names):
    for x in range(len(names)):
        if type(names[x]) is str:
            print(f"{names[x]}")
        else:
            print('Element not is string')

def multriple_params(**params) -> ():
    if type(params['first_name']) is str:
        return params['first_name'], True
    else:
        return type(params['first_name']), False

def producer():
    for num in range(0, 10, 1):
        if num % 2 == 0:
            yield num

def recursion(number):
    if number == 0:
        return 0
    return number + recursion(number - 1)

class People:
    __cor = 'green'

    def __init__(self, name, age, cpf):
        self.name = name
        self.age = age
        self.cpf = cpf

    def show_name_and_age(self):
        return f'My name is {self.name} and I\'m {self.age} old.'

    def get_color(self):
        return self.__cor

class Person(People):
    person_list_parent = []

    def __init__(self, name, age, cpf):
        super().__init__(name, age, cpf)
        self.person_list_parent = []

    def add_person_parent(self, **parent):
        self.person_list_parent.append(parent)

    def get_list_person_parent(self):
        return self.person_list_parent

    def __str__(self):
        return f"My family(father: {self.get_list_person_parent()[0]['father']})"

    def __eq__(self, other):
        if self.age == other.age:
            if self.name == other.name:
                return True

    def __lt__(self, other):
        return self.age < other.age

if __name__ == '__main__':
    person = Person('Kaio', 27, '112')
    person1 = Person('Kaio', 27, '112')
    print(person > person1)


'''
def recursion(5):
    if number == 0:
        return 0
    return 5 + 10
    
    def recursion(4):
    if number == 0:
        return 0
    return 4 + 6
    
    def recursion(3):
    if number == 0:
        return 0
    return 3 + 3
    
    def recursion(2):
    if number == 0:
        return 0
    return 2 + 1
    
    def recursion(1):
    if number == 0:
        return 0
    return 1 + 0
    
    def recursion(0):
    if number == 0:
        return 0
'''