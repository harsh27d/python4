from datetime import date

birth_year = int(input("Enter birth year: "))
age = date.today().year - birth_year

print("Your age is:", age)