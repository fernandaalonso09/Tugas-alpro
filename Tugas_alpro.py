# Muhammad Fernanda Alonso Meilandri (2309076031)
# Membuat program untuk mengetahui bilangan ganjil atau genap dan mengalikan dengan bilangan terdekatnya

bilangan = int(input("Masukan Bilangan: "))
def cek_dan_perkalian(bilangan):
    if bilangan % 2 == 0:  # Jika bilangan genap
        print(f"{bilangan} adalah bilangan genap")
    else:  # Jika bilangan ganjil
        print(f"{bilangan} adalah bilangan ganjil")
    return bilangan

bilangan_setelahnya = bilangan + 1
hasil = bilangan*bilangan_setelahnya
print(f"Hasil perkalian dari {bilangan} dengan bilangan setelahnya({bilangan_setelahnya}) adalah {hasil}")