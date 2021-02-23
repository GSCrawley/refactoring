# by Kami Bigdely
# Inline method.
# TODO: Refactor this program to improve its readability.

class Person():
    def __init__(self, age):
        Person.age = age
        
    def enterClub(age):
        if Person.age > 18:
            print("Come on in!")
        else: 
            print("Sorry, no minors allowed.")
    
    enterClub(17.9)
    

print(Person.age)