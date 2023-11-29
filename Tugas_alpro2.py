import random
import os

def main():
    outfile = open("bilangan_random.txt", "w")
    for i in range(100):
        outfile.write(str(random.randint(0, 1000)) + " ")
    outfile.close()

    infile = open("bilangan_random.txt", "r")
    nums = infile.read()
    print(nums,"\n")

    os.system("cls")
    numbers = [int(x) for x in nums.split()]
    num_printed = 0

    bilangan_genap_count = 0
    bilangan_ganjil_count = 0

    for x in numbers:
        num_printed += 1
        print(format(x, "3d"), end=" ")

        if x % 2 == 0:
            bilangan_genap_count += 1
        else:
            bilangan_ganjil_count += 1

        if num_printed == 10:
            print()
            num_printed = 0
        else:
            print(" ", end=" ")
    infile.close()
    print("-"*60)
    print("\n")

    #sortir
    bilangan_genap = [x for x in numbers if x % 2 == 0]
    bilangan_ganjil = [x for x in numbers if x % 2 != 0]

    bilangan_genap = sorted(bilangan_genap)
    bilangan_ganjil = sorted(bilangan_ganjil)

    print("Bilangan Genap:")
    print_numbers(bilangan_genap)

    # Print the sorted odd numbers
    print("\nBilangan Ganjil:")
    print_numbers(bilangan_ganjil)


    print(f"\nJumlah Bilangan Genap: {bilangan_genap_count}")
    print(f"Jumlah Bilangan Ganjil: {bilangan_ganjil_count}")

def print_numbers(numbers):
    num_printed = 0
    for x in numbers:
        num_printed += 1
        print(format(x, "3d"), end=" ")
        if num_printed == 10:
            print()
            num_printed = 0
        else:
            print(" ", end=" ")

main()