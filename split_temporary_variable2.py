
def name_and_age(info):
    print("saved into databse")


user_input = input('Please enter your username: ')
name_and_age(user_input)
user_input = int(input('Please enter your birth year: '))
age = 2020 - user_input
print("You are",age, "years old.")
