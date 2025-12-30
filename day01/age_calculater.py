name = input("enter your name please: ")
birth_year = int(input("enter the birth year: "))

current_year = 2025

age = current_year - birth_year

result = f"{name} is {age} year old."

print(result)

with open("result.txt","w") as file:
    file.write(result)