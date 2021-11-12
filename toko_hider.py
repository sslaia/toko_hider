# coding=utf-8
import json
import datetime
import os

# fungsi untuk mengosongkan layar
def mengosongkan_layar():
   # untuk linux dan mac os
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # untuk windows os
      _ = os.system('cls')
      
# fungsi mencek entah satu berkas ada atau tidak
def cek(berkas):
    return os.path.exists(berkas)

# fungsi menayangkan data yang telah ada
def menayangkan_menu():
    # mendeklarasikan berbagai variable
    daftar_menu = []
    
    # mengosongkan layar
    mengosongkan_layar()
    
    # menampilkan header
    print("*" * 75)
    print("TOKO HIDER\n".center(75))
    print("Hilifalawu, Kec. Maniamölö, Kab. Nias Selatan (HP: 085 222 000 000)".center(75))
    print("*" * 75)

    # memuat data dari database
    # mencek dulu entah berkas data ada
    berkas = cek("toko_hider.json")
    if (berkas == False):
        print("Database kosong.")
    elif (berkas == True) and (os.stat("toko_hider.json").st_size == 0):
        print("Database kosong.")
    else:
        # memuat data yang lama dari database
        with open("toko_hider.json") as f:
            json_data = json.load(f)
            # memuat daftar nilai
            for i in json_data["menu"]:
                nama = i["nama"]
                harga = i["harga"]
                print(f"{nama} : Rp {harga}")
    
    print()
    # bagian berikut hanya untuk menunggu
    # supaya pesan sempat dibaca
    selesai = input("Tekan Enter untuk keluar ")
    if selesai == "y":
        print("Lau bale!")
    else:
        print("Bye!")

    mengosongkan_layar()

# fungsi memasukkan data baru
def menginput_menu():
    # mendeklarasikan berbagai variable
    daftar_menu = []
    
    # mengosongkan layar
    mengosongkan_layar()
    
    # menampilkan header
    print("*" * 75)
    print("TOKO HIDER\n".center(75))
    print("Hilifalawu, Kec. Maniamölö, Kab. Nias Selatan (HP: 085 222 000 000)".center(75))
    print("*" * 75)

    # memuat data dari database
    # mencek dulu entah berkas data ada
    berkas = cek("toko_hider.json")
    if (berkas == False):
        print("Database kosong.")
    elif (berkas == True) and (os.stat("toko_hider.json").st_size == 0):
        print("Database kosong.")
    else:
        # memuat data yang lama dari database
        with open("toko_hider.json") as f:
            json_data = json.load(f)
            # memuat daftar nilai
            for i in json_data["menu"]:
                nama = i["nama"]
                harga = i["harga"]
                daftar_menu.append({"nama": nama, "harga": harga})

    # fungsi loop memasukkan data menu makanan
    keluar = False
    
    while keluar == False:
        # menampilkan formulir isian
        nama_makanan = input("Masukkan nama makanan : ") 
        harga_makanan = int(input("Masukkan harga        : "))

        daftar_menu.append({"nama": nama_makanan, "harga": harga_makanan})
    
        # bagian berikut hanya memastikan entah masih ada data yang mau dimasukkan
        # bila ada, maka proses dimulai kembali dari atas
        # kalau tidak proses dihentikan dan data dimasukkan ke database
        masih_ada = input("Masih ada? (y/t) ")

        if masih_ada == "t":
            keluar = True
            mengosongkan_layar()
                
    # setelah data selesai dimasukkan, data disimpan ke dalam database        
    with open('toko_menu.json', 'w') as f:
        data = {"menu": daftar_menu}
        json.dump(data, f)

    print()
    # bagian berikut hanya untuk menunggu
    # supaya pesan sempat dibaca
    selesai = input("Tekan Enter untuk keluar ")
    if selesai == "y":
        print("Lau bale!")
    else:
        print("Bye!")

    mengosongkan_layar()

# fungsi menayangkan data yang telah ada
def menayangkan_transaksi():
    # mendeklarasikan berbagai variable
    daftar_transaksi = []
    
    # mengosongkan layar
    mengosongkan_layar()
    
    # menampilkan header
    print("*" * 75)
    print("TOKO HIDER\n".center(75))
    print("Hilifalawu, Kec. Maniamölö, Kab. Nias Selatan (HP: 085 222 000 000)".center(75))
    print("*" * 75)

    # memuat data dari database
    # mencek dulu entah berkas data ada
    berkas = cek("toko_hider.json")
    if (berkas == False):
        print("Database kosong.")
    elif (berkas == True) and (os.stat("toko_hider.json").st_size == 0):
        print("Database kosong.")
    else:
        # memuat data yang lama dari database
        with open("toko_hider.json") as f:
            json_data = json.load(f)
            # memuat daftar nilai
            for i in json_data["transaksi"]:
                kasir = i["kasir"]
                waktu = i["waktu"]
                item = i["item"]
                jumlah = i["jumlah"]
                total = i["total"]
                daftar_transaksi.append({"kasir": kasir, "waktu": waktu, "item": item, "jumlah": jumlah, "total": total})
                print(f"{waktu}: {item} ({jumlah}) ({total}) ({kasir})")
    
    print()
    # bagian berikut hanya untuk menunggu
    # supaya pesan sempat dibaca
    selesai = input("Tekan Enter untuk keluar ")
    if selesai == "y":
        print("Lau bale!")
    else:
        print("Bye!")

    mengosongkan_layar()

# fungsi menginput data
def menginput_transaksi():
    # mendeklarasikan berbagai variable
    daftar_transaksi = []

    # mengosongkan layar
    mengosongkan_layar()
    
    # menampilkan header
    print("*" * 75)
    print("TOKO HIDER\n".center(75))
    print("Hilifalawu, Kec. Maniamölö, Kab. Nias Selatan (HP: 085 222 000 000)".center(75))
    print("*" * 75)

    # mengambil tanggal secara otomatis
    waktu_umum = datetime.datetime.now()
    waktu = waktu_umum.strftime("%Y-%m-%d %H:%M:%S")
 
    # memuat data dari database
    # mencek dulu entah berkas data ada
    berkas = cek("toko_transaksi.json")
    if (berkas == False):
        print("Database kosong.")
    elif (berkas == True) and (os.stat("toko_transaksi.json").st_size == 0):
        print("Database kosong.")
    else:
        # memuat data yang lama dari database
        with open("toko_transaksi.json") as f:
            json_data = json.load(f)
            # memuat daftar nilai
            for i in json_data["transaksi"]:
                kasir = i["kasir"]
                waktu = i["waktu"]
                item = i["item"]
                jumlah = i["jumlah"]
                total = i["total"]
                daftar_transaksi.append({"kasir": kasir, "waktu": waktu, "item": item, "jumlah": jumlah, "total": total})

    print()
    
    # memasukkan nama kasir
    kasir =  input("Nama kasir            : ")
    print()
    
    # fungsi loop memasukkan transaksi baru
    keluar = False
    
    while keluar == False:

        # menampilkan daftar menu
        print("1. Gore Gae -> Rp 1.000")
        print("2. Gado-Gado -> Rp 1.500")
        print("3. Kopi susu -> Rp 2.000")
        print("4. Teh Manis -> Rp 2.500")
        print("-" * 25)
        print()
        
        # memasukkan transaksi    
        item =   input("Makanan (1/2/3/4)     : ") 
        jumlah = int(input("Masukkan jumlah       : "))
        anggota = input("Anggota? (y/t)        : ")
    
        item_menu = ""

        harga = 0
        if item == "1":
            item_menu = "Gore Gae"
            harga = jumlah * 1000
        elif item == "2":
            item_menu = "Gado-Gado"
            harga = jumlah * 1500
        elif item == "3":
            item_menu = "Kopi Susu"
            harga = jumlah * 2000
        else:
            item_menu = "Teh Manis"
            harga = jumlah * 2500
            
        total = 0.00
        if harga >= 100000:
            if anggota == "y":
                total = harga * 0.20
            else:
                total = harga * 0.15
        elif harga >= 75000:
            if anggota == "y":
                total = harga * 0.10
            else:
                total = harga * 0.075
        elif harga >= 50000:
            if anggota == "y":
                total = harga * 0.05
            else:
                total = harga * 0.025
        else:
            total = harga

        print(f"Item: {item}, Harga: {harga}, Jumlah: {jumlah}, Total: {total}")
    
        daftar_transaksi.append({"kasir": kasir, "waktu": waktu, "item": item_menu, "jumlah": jumlah, "total": total})

        mau_keluar = input("Mau keluar? (y/t) ")

        if mau_keluar == "y":
            keluar = True
        
    # setelah data selesai dimasukkan, data disimpan ke dalam database        
    # with open('toko_transaksi.json', 'a') as f:
    #     f.write(str(daftar_transaksi))
    with open('toko_transaksi.json', 'w') as f:
        data_transaksi = {"transaksi": daftar_transaksi}
        json.dump(data_transaksi, f)

    print()
    # bagian berikut hanya untuk menunggu
    # supaya pesan sempat dibaca
    selesai = input("Tekan Enter untuk keluar ")
    if selesai == "y":
        print("Lau bale!")
    else:
        print("Bye!")

    mengosongkan_layar()
# fungsi menayangkan data yang telah ada
def menayangkan_anggota():
    # mendeklarasikan berbagai variable
    daftar_anggota = []
    
    # mengosongkan layar
    mengosongkan_layar()
    
    # menampilkan header
    print("*" * 75)
    print("TOKO HIDER\n".center(75))
    print("Hilifalawu, Kec. Maniamölö, Kab. Nias Selatan (HP: 085 222 000 000)".center(75))
    print("*" * 75)

    # memuat data dari database
    # mencek dulu entah berkas data ada
    berkas = cek("toko_hider.json")
    if (berkas == False):
        print("Database kosong.")
    elif (berkas == True) and (os.stat("toko_hider.json").st_size == 0):
        print("Database kosong.")
    else:
        # memuat data yang lama dari database
        with open("toko_hider.json") as f:
            json_data = json.load(f)
            # memuat daftar nilai
            for i in json_data["anggota"]:
                nama = i["nama"]
                nomor = i["nomor"]
                daftar_anggota.append({"nama": nama, "nomor": nomor})
                print(f"{nama}: {nomor}")
    
    print()
    # bagian berikut hanya untuk menunggu
    # supaya pesan sempat dibaca
    selesai = input("Tekan Enter untuk keluar ")
    if selesai == "y":
        print("Lau bale!")
    else:
        print("Bye!")

    mengosongkan_layar()

# fungsi memasukkan data
def menginput_anggota():
    # mendeklarasikan berbagai variable
    daftar_anggota = []

    # memuat data dari database
    # mencek dulu entah berkas data ada
    berkas = cek("toko_hider.json")
    if (berkas == False):
        print("Database kosong.")
    elif (berkas == True) and (os.stat("toko_hider.json").st_size == 0):
        print("Database kosong.")
    else:
        # memuat data yang lama dari database
        with open("toko_hider.json") as f:
            json_data = json.load(f)
            # memuat daftar nilai
            for i in json_data["anggota"]:
                nama = i["nama"]
                nomor = i["nomor"]
                daftar_anggota.append({"nama": nama, "nomor": nomor})

    # fungsi loop untuk memasukkan data baru    
    keluar = False

    while keluar == False: 
        # mengosongkan layar
        mengosongkan_layar()
        
        # menampilkan header
        print("*" * 75)
        print("TOKO HIDER\n".center(75))
        print("Hilifalawu, Kec. Maniamölö, Kab. Nias Selatan (HP: 085 222 000 000)".center(75))
        print("*" * 75)

        # menampilkan formulir isian
        print()
        nama = input("Masukkan nama  : ") 
        nomor = input("Masukkan nomor : ")

        daftar_anggota.append({"nama": nama, "nomor": nomor})

        masih_ada = input("Masih ada? (y/t) ")

        if masih_ada == "t":
            keluar = True
        
    with open('toko_anggota.json', 'w') as json_file:
        data = {"anggota": daftar_anggota}
        json.dump(data, json_file)

    print()
    # bagian berikut hanya untuk menunggu
    # supaya pesan sempat dibaca
    selesai = input("Tekan Enter untuk keluar ")
    if selesai == "y":
        print("Lau bale!")
    else:
        print("Bye!")

    mengosongkan_layar()

# fungsi membuat backup
def membuat_backup():
    print()
    print("Sebentar yah... sedang membuat backup")

    # mendeklarasikan berbagai variable
    daftar_anggota = []
    daftar_menu = []
    daftar_transaksi = []

    # mencek entah berkas data ada
    toko_hider = cek("toko_hider.json")
    if (toko_hider == False):
        print(toko_hider)
        print("Belum ada database. Saya akan menciptakannya.")
    elif (toko_hider == True) and (os.stat("toko_hider.json").st_size == 0):
        print("Belum ada database. Saya akan menciptakannya.")
    else:
        # memuat daftar menu yang lama dari database
        with open("toko_hider.json") as f:
            json_data = json.load(f)
            # memuat daftar anggota
            for i in json_data["anggota"]:
                nama = i["nama"]
                nomor = i["nomor"]
                daftar_anggota.append({"nama": nama, "nomor": nomor})
            # memuta daftar menu
            for i in json_data["menu"]:
                nama = i["nama"]
                harga = i["harga"]
                daftar_menu.append({"nama": nama, "harga": harga})
            # membuat daftar transaksi
            for i in json_data["transaksi"]:
                kasir = i["kasir"]
                waktu = i["waktu"]
                item = i["item"]
                jumlah = i["jumlah"]
                total = i["total"]
                daftar_transaksi.append({"kasir": kasir, "waktu": waktu, "item": item, "jumlah": jumlah, "total": total})

    # memuat daftar menu yang baru
    toko_anggota = cek("toko_anggota.json")
    if (toko_anggota == False):
        print("Data anggota kosong. Tak ada yang perlu di-backup.")
    elif (toko_anggota == True) and (os.stat("toko_anggota.json").st_size == 0):
        print("Data anggota kosong. Tak ada yang perlu di-backup.")
    else:
        with open("toko_anggota.json") as f:
            data_anggota = json.load(f)

            # membuat daftar anggota
            for i in data_anggota["anggota"]:
                nama = i["nama"]
                nomor = i["nomor"]
                daftar_anggota.append({"nama": nama, "nomor": nomor})

    toko_menu = cek("toko_menu.json")
    if (toko_menu == False):
        print("Data menu kosong. Tak ada yang perlu di-backup.")
    elif (toko_menu == True) and (os.stat("toko_menu.json") == 0):
        print("Data menu kosong. Tak ada yang perlu di-backup.")
    else:
        with open("toko_menu.json", "r") as f:
            data_menu = json.load(f)

            # membuat daftar anggota
            for i in data_menu["menu"]:
                nama = i["nama"]
                harga = i["harga"]

                daftar_menu.append({"nama": nama, "harga": harga})

    toko_transaksi = cek("toko_transaksi.json")
    if (toko_transaksi == False):
        print("Database transaksi kosong. Tak ada yang perlu di-backup.")
    elif (toko_transaksi == True) and (os.stat("toko_transaksi.json") == 0):
        print("Database transaksi kosong. Tak ada yang perlu di-backup.")
    else:
        with open("toko_transaksi.json") as f:
            data_transaksi = json.load(f)
            f.close()

            # membuat daftar transaksi
            for i in data_transaksi["transaksi"]:
                kasir = i["kasir"]
                waktu = i["waktu"]
                item = i["item"]
                jumlah = i["jumlah"]
                total = i["total"]
                daftar_transaksi.append({"kasir": kasir, "waktu": waktu, "item": item, "jumlah": jumlah, "total": total})

    # membuat backup
    with open("toko_hider.json", "w") as f:
        data_toko = {"anggota": daftar_anggota, "menu": daftar_menu, "transaksi": daftar_transaksi}
        json.dump(data_toko, f)

    print()
    print("Selesai. Saohagölö!!!!!!")
    print("Kembali ke layar pilihan!")
    print()
    # bagian berikut hanya untuk menunggu
    # supaya pesan backup sempat dibaca
    selesai = input("Tekan Enter untuk keluar ")
    if selesai == "y":
        print("Lau bale!")
    else:
        print("Bye!")

    mengosongkan_layar()

    
#    
#
# program mulai dari sini
#

keluar = False

while keluar == False:
    # Menampilkan pilihan operasi
    print("*" * 40)
    print("TOKO HIDER\n".center(40))
    print()
    print("Hilifalawu, Maniamölö, Nias Selatan".center(40))
    print()
    print("*" * 40)
    print("Silakan memilih:")
    print("1. Menayangkan daftar transaksi yang ada")
    print("2. Memasukkan transaksi baru")
    print("3. Menayangkan daftar menu yang ada")
    print("4. Memasukkan menu makanan baru")
    print("5. Menayangkan daftar anggota yang ada")
    print("6. Memasukkan anggota baru")
    print("7. Membuat backup data")
    print("8. Keluar")
    print("*" * 40)
    print()

    pilihan = input("Pilihan Anda: ")

    if pilihan == "7":
        membuat_backup()   
    elif pilihan == "6":
        menginput_anggota()
    elif pilihan == "5":
        menayangkan_anggota()
    elif pilihan == "4":
        menginput_menu()
    elif pilihan == "3":
        menayangkan_menu()
    elif pilihan == "2":
        menginput_transaksi()
    elif pilihan == "1":
        menayangkan_transaksi()
    else:
        keluar = True    

