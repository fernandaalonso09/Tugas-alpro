sa = 5000
dp = int(input('masukan jumlah deposit: '))
htng = 50000

if sa + dp >= htng:
    print('deposit diterima')
    ts = (sa + dp) - htng
    print("total saldo: ", ts)
else:
    print('deposit ditolak')