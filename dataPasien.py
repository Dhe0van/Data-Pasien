# tugas akhir 
# Nama  : Dheovan Winata Alvian 
# Kelas : 10 Komputer 1
# Program Data Pasien 

from os import system
from time import sleep
# Jika belum terinstall --> $ pip3 install tabulate
from tabulate import tabulate

# Kumpulan kode warna
# Hiraukan saja
putih = "\033[97m"
biruBG = "\033[44m"
merah = "\033[91m"
normal = "\033[0m"
hijau = "\033[92m"


dataPasien = {
    "Buaya":{
        "Gender":"Laki-laki",
        "Penyakit":"Sakit hati",
        "Ruangan":"VIP",
        "ID":"001",
        "Lama menginap":"5"
    }
}

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


# Menampilkan data pasien
def tampilkanData():
    system("clear")
    # Variabel kosong untuk dimasukkan nilainya pada saat looping
    tableData = []
    # Jika dataPasien kosong maka akan menampilkan pesan berikut
    if len(dataPasien) == 0:
        tableData.append(["Maaf tetapi data pasien saat ini sedang kosong."])
        print(tabulate(tableData)) 
    # Jika ada sesuatu di dalam data pasien
    else:
        # Looping dilakukan untuk mencari semua data pasien
        for i in dataPasien:
            nama = i
            gender = dataPasien[i]["Gender"]
            penyakit = dataPasien[i]["Penyakit"]
            ruangan = dataPasien[i]["Ruangan"]
            id = dataPasien[i]["ID"]
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
    inputTambahNamaData = input("Tambahkan Nama: ")
    inputTambahGenderData = input("Tambahkan Gender: ")
    inputTambahPenyakitData = input("Tambahkan Penyakit: ")
    inputTambahRuanganData = input("Tambahkan tipe Ruangan: ")
    inputTambahIdData = input("Tambahkan ID: ")
    inputTambahLamaMenginapData = input("Tambahkan lama Pasien menginap: ")
    # Membuat loop infinite untuk supaya input verifikasiUser dapat berjalan terus jika yang ditekan selain Y/n
    while True:
        verifikasiUser = input(f"Apakah anda yakin ingin menyimpan data ini? [{hijau}Y{normal}/{merah}n{normal}]: ").upper()
        if verifikasiUser == "Y":
            # memakai animasi loading yang diuolang sebanyak 4 kali
            loading("Menyimpan data", 4)
            # Ini akan memasukkan data yang baru saja ditambahkan ke dalam dataPasien
            dataPasien[inputTambahNamaData] = {
                "Gender":inputTambahGenderData,
                "Penyakit":inputTambahPenyakitData,
                "Ruangan":inputTambahRuanganData,
                "ID":inputTambahIdData,
                "Lama menginap":inputTambahLamaMenginapData
            } 
            system("clear")
            tableData= []
            # Menampilkan data yang tadi ke dalam bentuk tabel
            tableData.append([inputTambahNamaData, inputTambahGenderData, inputTambahNamaData, inputTambahRuanganData, inputTambahIdData, inputTambahLamaMenginapData + " Hari"])
            print(tabulate(tableData, headers=["Nama", "Gender", "Penyakit", "Ruangan", "ID", "Lama menginap"], tablefmt="presto"))
            print("\nData berhasil disimpan.")
            break
        elif verifikasiUser == "N":
            break
        else:
            print(f"Silahkan Pilih {hijau}Y{normal} atau {merah}n{normal}.")
    input("\nTekan ENTER untuk kembali.")
    


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
            pass
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