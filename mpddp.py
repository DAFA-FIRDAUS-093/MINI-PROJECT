print("nama = Dafa Firdaus")
print("nim = 2409116093")
print("kelas = c")

user = str(input("masukan nama : "))
password = str(input("masukan password : "))

while True:
    nama = str(input("masukan nama : "))
    kata_sandi = str(input("masukan password : "))

    if user == nama and password == kata_sandi:
        print("anda berhasil login")
        jam_kerja = int(input("masukan jam kerja : "))
        gaji = int(input("masukan gaji : "))
        total = jam_kerja * gaji
        if jam_kerja > 160:
            bonus = total * 0.1
            gaji = gaji + bonus
            print("bonus anda adalah",gaji)
        else:
            print("anda tidak mendapat bonus")
        print ("silahkan pilih menu dibawah ini")
        print("1. hitung gaji lagi \n 2. keluar")
        pilihan = int(input("masukan pilihan : "))
        if pilihan == 1:
            print("program menghitung gaji diulang")
        elif pilihan == 2:
            print("program keluar")
            break
        else:
            print("anda salah memasukan pilihan")
    else:
        print("anda salah memasukan nama atau kata sandi") 
        