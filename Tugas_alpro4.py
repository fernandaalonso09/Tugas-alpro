#Muhammad Fernanda Alonso Meilandri (2309076031)

import datetime
import os

mahasiswa_template = {
    'nama':'nama',
    'nim':"0000000000",
    'sks':'0',
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

os.system("cls")
print(f"{'SELAMAT DATANG':^20}")
print(f"{'DI DATA MAHASISWA':^20}")
print("-"*20)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
print(mahasiswa)
mahasiswa['nama'] = input("Nama Mahasiswa: ")
mahasiswa['nim'] = input("NIM Mahasiswa: ")
mahasiswa['sks'] = input("Jumlah SKS: ")
TAHUN_LAHIR = int(input("Tahun Lahir (YYYY): "))
BULAN_LAHIR = int(input("Bulan Lahir (1-12): "))
TANGGAL_LAHIR = int(input("Tanggal Lahir (1-31): "))
mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

data_mahasiswa.update({'key':mahasiswa})

print(f"{'KEY':<6} {'Nama':<17} {'NIM':<11} {'SKS':^10} {'Tanggal Lahir':<10}")
print('-'*60)
for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<17} {NIM:<11} {SKS:^10} {LAHIR:<10}")

print("\n")