import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

b = []

for pass_letters in range(1, nr_letters + 1):
    x = letters[random.randint(0, nr_letters)]
    b.extend(x)

for pass_symbols in range(1, nr_symbols + 1):
    y = symbols[random.randint(0, nr_symbols)]
    b.extend(y)

for pass_numbers in range(1, nr_numbers + 1):
    z = numbers[random.randint(0, nr_numbers)]
    b.extend(z)

c = []

for elements in range(0, len(b)):
    n = b[random.randint(0, len(b)) - 1]
    c.append(n)
    b.remove(n)

d = str()

for things in c:
    d += str(things)
    

print(d)



