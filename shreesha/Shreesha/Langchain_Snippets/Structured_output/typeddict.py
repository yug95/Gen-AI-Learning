from typing import TypedDict

class Person(TypedDict):
#define keys and their datatype
    name: str  
    age: int

#create new dic : type of person dic 
new_person: Person = {'name':'shree', 'age':'22'}

print(new_person)