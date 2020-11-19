# tugas akhir
# Nama  : Dheovan Winata Alvian
# Kelas : 10 Komputer 1
# Program Data Pasien

import os
import platform
from getpass import getpass

# Module Sendiri
from components import var, extra, models


# Menampilkan tampilan menu
def displayMenu():
    print(f"""
    *** Program Data Pasien ***
    Selamat datang {inputUserName}.
    Silahkan pilih salah satu pilihan berikut:
    [1] {var.putih}Menampilkan data pasien.{var.reset}
    [2] {var.putih}Menambahkan data pasien.{var.reset}
    [3] {var.putih}Menghapus data pasien.{var.reset}
    [4] {var.putih}Mencari data pasien.{var.reset}
    [5] {var.putih}Perbarui data pasien.{var.reset}
    [?] {var.putih}Tentang program ini.{var.reset}
    [{var.merah}Q{var.reset}] {var.putih}Keluar dari program.{var.reset}
    """)


# Dicoba terlebih dahulu apakah ada error atau tidak.
try:
    from time import sleep
    from tabulate import tabulate
    # Jika belum terinstall --> $ pip3 install tabulate

    # Keseluruhan proses dari progra,

    def proses():
        while True:
            extra.clear()
            displayMenu()
            inputPilihanUser = input("Masukkan pilihan anda: ")
            inputPilihanUser = inputPilihanUser.upper()
            if inputPilihanUser == "Q":
                print("Terima kasih telah menggunakan program ini.")
                break
            elif inputPilihanUser == "1":
                models.tampilkanData()
            elif inputPilihanUser == "2":
                models.tambahkanData()
            elif inputPilihanUser == "3":
                models.hapusData()
            elif inputPilihanUser == "4":
                models.cariData()
            elif inputPilihanUser == "5":
                models.perbaruiData()
            elif inputPilihanUser == "?":
                models.tentang()
            else:
                extra.clear()
                print("Hanya masukkan kata kunci sesuai di tampilan menu.")
                input("\nTekan ENTER untuk kembali.")

    inputUserName = input("Masukkan Nama Anda: ")
    # Disini password apapun akan benar kecuali Kosong
    inputUserPasswd = getpass(prompt="Masukkan Password Anda: ")
    # User login dan memverifikasi password
    while inputUserPasswd == "":
        extra.loading("Mengecek Password", 2)
        print(f"Maaf Password tidak boleh {var.merah}KOSONG{var.reset}.")
        inputUserPasswd = getpass(prompt="Masukkan Password Anda: ")
    else:
        extra.loading("Mengecek Password", 3)
        print("Baiklah silahkan masuk.")
        sleep(0.7)
        proses()

# Jika terjadi error yang dimana errornya adalah adanya module yang belum terpasang di sistem operasi User
except ModuleNotFoundError:
    pass
