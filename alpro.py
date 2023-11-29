def hitung_luas_persegi(sisi):
    return sisi*sisi

file = open ('luas_persegi.txt', 'w')
for i in range (1, 6):
    luas = hitung_luas_persegi(i)
    file.write(f"Sisi: {i}, luas: {luas}\n")

file.close()

data_list = [10, 20, 30, 40, 50,]
file = open('data_list.txt', 'w')
for data in data_list:
    file.write(str(data) + '\n')

file.close()    