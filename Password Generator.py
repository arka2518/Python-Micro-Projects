import random

print("Welcome to the Password Generator!")
Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

x = int(input("How many letters would you like in your password: "))
y = int(input("How many numbers would you like in your password: "))
z = int(input("How many symbols would you like in your password: "))
password_list = []

for i in range(0, x):
    password_list.append(random.choice(Letters))
for i in range(0, y):
    password_list.append(random.choice(Numbers))
for i in range(0, z):
    password_list.append(random.choice(Symbols))
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for i in password_list:
    password += str(i)
print(f"Your new Password: {password}")