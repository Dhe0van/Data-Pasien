# tugas akhir 
# Nama  : Dheovan Winata Alvian 
# Kelas : 10 Komputer 1
# Program Data Pasien 


from os import system
from time import sleep
# Jika belum terinstall --> $ pip3 install tabulate
from tabulate import tabulate
from datetime import datetime

# Kumpulan kode warna
# Hiraukan saja
putih = "\033[97m"
biruBG = "\033[44m"
merah = "\033[91m"
normal = "\033[0m"
hijau = "\033[92m"


dataPasien = {
    "20201021-A001":{
        "Nama":"orang",
        "Gender":"cowo",
        "Penyakit":"Pneumonia",
        "Ruangan":"VIP",
        "Lama menginap":"5"
    }
}

# Membuat id untuk pasien baru
def idPasien():
    # Memberikan tanggal, bulan, tahun hari ini
    idHariIni = datetime.now()
    idTgl = idHariIni.day
    idBulan = idHariIni.month
    idTahun = idHariIni.year
    kodeId = len(dataPasien) + 1

    idBaru  = ("%4d%2d%02d-A%03d" % (idTahun, idBulan, idTgl, kodeId))
    # Akan memberikan value baru yaitu idBaru saja
    return idBaru


def verifikasiUser(char):
    verifikasiUser = input(f"\nApakah anda yakin ingin {char} data Pasien ini? [{hijau}Y{normal}/{merah}n{normal}]: ").upper()
    return verifikasiUser


# Menampilkan tampilan menu
def displayMenu():
    print(f"""
    *** Program Data Pasien ***
    Selamat datang {inputUserName}.
    Silahkan pilih salah satu pilihan berikut:
    [1] {putih}Menampilkan data pasien.{normal}
    [2] {putih}Menambahkan data pasien.{normal}
    [3] {putih}Menghapus data pasien.{normal}
    [4] {putih}Mencari data pasien.{normal}
    [5] {putih}Perbarui data pasien.{normal}
    [?] {putih}Tentang program ini.{normal}
    [{merah}Q{normal}] {putih}Keluar dari program.{normal}
    """)


def dataKosong(char):
    # Diberi variabel kosong supaya bisa menampung data yg diberikan
    tableData = []
    if len(char) == 0:
        tableData.append(["Maaf Tetapi data saat ini masih kosong."])
        print(tabulate(tableData))
    else:
        pass

# Menampilkan data pasien
def tampilkanData():
    system("clear")
    # Jika data pasien kosong.
    tableData = []
    if len(dataPasien) == 0:
        dataKosong(dataPasien)
    # Jika ada sesuatu di dalam data pasien
    else:
        # Looping dilakukan untuk mencari semua data pasien
        for i in dataPasien:
            nama = dataPasien[i]["Nama"]
            gender = dataPasien[i]["Gender"]
            penyakit = dataPasien[i]["Penyakit"]
            ruangan = dataPasien[i]["Ruangan"]
            id = i
            lamaMenginap = dataPasien[i]["Lama menginap"]
            # Gunakan .append() untuk memasukkan variablenya ke tabel
            tableData.append([nama, gender, penyakit, ruangan, id, lamaMenginap + " Hari"])
        # Menampilkan data pasien dalam bentuk tabel
        print(tabulate(tableData, headers=["Nama", "Gender", "Penyakit", "Ruangan", "ID", "Lama menginap"], tablefmt="presto"))
    input("\nTekan ENTER untuk kembali.")

# Fungsi yang memuat animasi loading
def loading(char, jumlahUlang):
    system("clear")
    for i in range(jumlahUlang):
        print(char + " -")
        sleep(0.2)
        system("clear")
        print(char + " |")
        sleep(0.2)
        system("clear")
        print(char + " /")
        sleep(0.2)
        system("clear")


# Menambahkan data ke ke dalam dataPasien
def tambahkanData():
    system("clear")
    nama = input("Tambahkan Nama: ")
    for i in dataPasien:
        if nama == dataPasien[i]["Nama"]:
            print("Maaf tetapi terdapat nama Pasien yang sama.")
            break
    else:
        gender = input("Tambahkan Gender: ")
        penyakit = input("Tambahkan Penyakit: ")
        ruangan = input("Tambahkan tipe Ruangan: ")
        id = idPasien()
        lamaMenginap = input("Tambahkan lama Pasien menginap: ")
        # Membuat loop infinite untuk supaya input verifikasiUser dapat berjalan terus jika yang ditekan selain Y/n
        while True:
            userInput = verifikasiUser("Menyimpan")
            if userInput == "Y":
                # memakai animasi loading yang diuolang sebanyak 4 kali
                loading("Menyimpan data", 4)
                # Ini akan memasukkan data yang baru saja ditambahkan ke dalam dataPasien
                dataPasien[id] = {
                    "Nama":nama,
                    "Gender":gender,
                    "Penyakit":penyakit,
                    "Ruangan":ruangan,
                    "Lama menginap":lamaMenginap
                } 
                system("clear")
                tableData= []
                # Menampilkan data yang tadi ke dalam bentuk tabel
                tableData.append([nama, gender, penyakit, ruangan, id, lamaMenginap + " Hari"])
                print(tabulate(tableData, headers=["Nama", "Gender", "Penyakit", "Ruangan", "ID", "Lama menginap"], tablefmt="presto"))
                print("\nData berhasil disimpan.")
                break
            elif userInput == "N":
                break
            else:
                print(f"Silahkan Pilih {hijau}Y{normal} atau {merah}n{normal}.")
            
    input("\nTekan ENTER untuk kembali.")
    

def hapusData():
    system("clear")
    # Jika data pasien kosong
    if len(dataPasien) == 0:
        dataKosong(dataPasien)
    # Jika terdapat data di dalam dataPasien
    else:
        inputDelData = input("Silahkan masukkan nama pasien yang ingin dihapus: ")
        # Looping untuk mencari semua data pasien
        for i in dataPasien:
            # Jika nama yang dicari ada di dalam dataPasien
            if inputDelData == dataPasien[i]["Nama"]:
                tableData = []
                nama = dataPasien[i]["Nama"]
                gender = dataPasien[i]["Gender"]
                penyakit = dataPasien[i]["Penyakit"]
                ruangan = dataPasien[i]["Ruangan"]
                id = i
                lamaMenginap = dataPasien[i]["Lama menginap"]

                tableData.append([nama, gender, penyakit, ruangan, id, lamaMenginap + " Hari"])

                system("clear")
                # Menampilkan data yang ingin dihapus ke dalam bentuk tabel
                print(tabulate(tableData, headers=["Nama", "Gender", "Penyakit", "Ruangan", "ID", "Lama menginap"], tablefmt="presto"))

                # loop infinite untuk verifikasi user
                while True:
                    inputUser = verifikasiUser("Menghapus")

                    if inputUser == "Y":
                        loading("Menghapus data", 3)
                        dataPasien.pop(i)
                        print("Data telah dihapus.")
                        break
                    elif inputUser == "N":
                        break
                    else:
                        print(f"Silahkan Pilih {hijau}Y{normal} atau {merah}n{normal}.")
                
                break
            # Jika nama pasien yang dicari tidak ditemukan  dalam looping
            else:
                print("Maaf tetapi pasien tersebut tidak ada di dalam data.")
    input("Tekan ENTER untuk kembali.")


# Keseluruhan proses dari progra,
def proses():
    while True:
        system("clear")
        displayMenu()
        inputPilihanUser = input("Masukkan pilihan anda: ")
        inputPilihanUser = inputPilihanUser.upper()
        if inputPilihanUser == "Q":
            print("Terima kasih telah menggunakan program ini.")
            break
        elif inputPilihanUser == "1":
            tampilkanData()
        elif inputPilihanUser == "2":
            tambahkanData()
        elif inputPilihanUser == "3":
            hapusData()
        elif inputPilihanUser == "4":
            pass
        elif inputPilihanUser == "5":
            pass
        elif inputPilihanUser == "?":
            pass
        # Jika user menginput selain 1-5, Q, ?
        else:
            system("clear")
            print("Hanya masukkan kata kunci sesuai di tampilan menu.")
            input("\nTekan ENTER untuk kembali.")


inputUserName = input("Masukkan Nama Anda: ")
inputUserPasswd = input("Masukkan Juga Password Anda (Hint: Passwordnya a): ")
# User login dan memverifikasi password
while inputUserPasswd != "a":
    loading("Mengecek Password", 2)
    print(f"Maaf tetapi password yang anda masukkan {merah}SALAH{normal}. Harap coba lagi...")
    inputUserPasswd = input("Masukkan Juga Password Anda (Hint: Passwordnya a): ")
else:
    loading("Mengecek Password", 3)
    print("Baiklah silahkan masuk.")
    sleep(0.7)
    proses()
