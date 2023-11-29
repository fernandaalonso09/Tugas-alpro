#Muhammad Fernanda Alonso Meilandri (2309076031)

def susun_bilangan():
    bilangan = [16, 20, 3, 78, 29, 84, 43, 78, 11]
    return bilangan

# Ascending(Terkecil ke terbesar)
bilangan = susun_bilangan()
bilangan_terurut = sorted(bilangan)
print("Bilangan yang masih teracak : ", bilangan)
print("Bilangan setelah disusun secara ascending:", bilangan_terurut)

# Descending (Terbesar ke terkecil)
bilangan_terurut = sorted(bilangan, reverse=True)
print("Bilangan setelah disusun secara descending:", bilangan_terurut)