# Python doesn't use classes as extensively as other languages, for example Java/C# where you HAVE to create a class, even if all it does is contain a collection of methods, and objects created from that class aren't especially meaningful as objects. For example, main() has to be in a class in C# and Java. Python classes are typically only created if you need to keep data, or data+methods together.
# A function is (usually) a standalone thing. A method is (usually) a function that is part of a class. If you call everything functions or call everything methods I'll know what you mean. 
class Student:
    def __init__(self, name, schoolId,gpa ):
        self.name = name
        self.schoolId = schoolId
        self.gpa = gpa
#self == this, refers to the object that is being intialized
    def __str__(self) -> str:
        return f'Student name: {self.name}, ID: {self.schoolId}, GPA: {self.gpa}.'
alex = Student('Alex','abs',4.0)
print(alex.name, alex.schoolId, alex)
sam=Student('Sam', 'qwerty',3.99)
print(sam)

import random
class Dice:
    def __init__(self,sides=6): #default
        self.sides = sides
    
    def roll(self):
        return random.randint(1,self.sides)

dice=Dice() #range dice(6)
print(dice.roll())

class Author:
    def __init__(self,name):
        self.name = name
        self.books= [] 
    def publish(self, title):
        if title not in self.books:
            self.books.append(title)
        else:
            print('This title already exists!')
    def __str__(self) -> str:
        # if self.books:
        #     book_list = ', '.join(self.books)
        # else:
        #     book_list='No books'
        book_list = ', '.join(self.books) or 'No published books'
        return f'{self.name}, books: {book_list}'
asimov = Author('Isaac Asimov')
asimov.publish('Foundation')
asimov.publish('Foundation')
asimov.publish('Something Else')
print(asimov)
class Example: 
    def __str__(self) -> str:
        pass #if you don't know what you will put in it yet
from dataclasses import dataclass #dataclass is a decorator
@dataclass
class Student:
    name: str
    schoolId: str
    gpa:float

    def __str__(self) -> str:
        return f'Name {self.name}, GPA: {self.gpa}.'
def main():        
    alex = Student('Alex','abs',3.00)
    print(alex.name, alex.schoolId, alex.gpa) #prints Alex abs 3.0
    sam=Student('Sam', 'qwerty',4.00)
    print(sam) #prints Student(name='Sam', schoolId='qwerty', gpa=4.0)
if __name__ == '__main__':
    main() #if we have multiple python files, this is helpful
