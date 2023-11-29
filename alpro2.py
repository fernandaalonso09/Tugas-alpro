import random

# Membuat list angka acak dari 1-200
numbers = random.sample(range(1, 201), 20)

# Menulis angka-angka ke dalam file
with open('angka_acak.txt', 'w') as file:
    for number in numbers:
        file.write(str(number) + '\n')
# Membaca file
with open('angka_acak.txt', 'r') as file:
    lines = file.readlines()

# Menampilkan hanya angka ganjil
for line in lines:
    number = int(line.strip())
    if number % 2 != 0:
        print(number)
