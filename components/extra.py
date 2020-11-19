# Kumpulan fungsi pendamping.

from components import var
import platform
import os
import time

# agar dapat menggunakan ANSI code di Windows
os.system("")

# fungsi menangani error


def moduleError():
    print(f"Maaf tetapi anda memiliki 1 module yang belum terpasang\nDibutuhkan module yang lengkap agar program dapat berjalan dengan optimal.\n")

    persetujuan = input(
        f"Apakah anda ingin menginstall module yang dibutuhkan sekarang? (Module yang dibutuhkan = Tabulate) [{var.hijau}Y{var.reset}/{var.merah}n{var.reset}]: ").upper()

    while True:
        if persetujuan == "Y":
            # Akan execute command line pip3 install tabulate jika sistem operasi user adalah Linux
            if var.platform_OS() == "linux":
                commandBash = os.popen("pip3 install tabulate")
                print(commandBash.read())
                break
            # Akan execute command line cmd /k pip3 install tabulate jika sistem operasi user adalah windows
            else:
                os.system('cmd /k "pip3 install tabulate"')
                os.system('cmd /k "exit"')
                break
        elif persetujuan == "N":
            break
        else:
            print(
                f"Silahkan Pilih {var.hijau}Y{var.reset} atau {var.merah}n{var.reset}.")

            persetujuan = input(
                f"Apakah anda ingin menginstall module yang dibutuhkan sekarang? (Module yang dibutuhkan = Tabulate) [{var.hijau}Y{var.reset}/{var.merah}n{var.reset}]: ").upper()


try:
    from tabulate import tabulate

    # Fungsi ini untuk mengganti command clear screen sesuai OS masing-masing

    def clear():
        OS = platform.system().lower()

        if OS == "linux":
            linux = os.system("clear")
            return linux
        else:
            windows = os.system("cls")
            return windows

    # Fungsi yang memuat animasi loading (Biar Keren)

    def loading(char, jumlahUlang):
        clear()
        for i in range(jumlahUlang):
            print(char + " -")
            time.sleep(0.2)
            clear()
            print(char + " |")
            time.sleep(0.2)
            clear()
            print(char + " /")
            time.sleep(0.2)
            clear()

    # Jika data pasien kosong

    def dataKosong(char):
        # Diberi variabel kosong supaya bisa menampung data yg diberikan
        tableData = []
        if len(char) == 0:
            tableData.append(["Maaf Tetapi data saat ini masih kosong."])
            print(tabulate(tableData))
        else:
            pass

    def verifikasiUser(char):
        persetujuan = input(
            f"\nApakah anda yakin ingin {char} data Pasien ini? [{var.hijau}Y{var.reset}/{var.merah}n{var.reset}]: ").upper()
        return persetujuan

    # Ini untuk menampilkan Tabel

    def tampilkanTable(char):
        clear()
        tableData = []
        nama = var.dataPasien[char]["Nama"]
        gender = var.dataPasien[char]["Gender"]
        penyakit = var.dataPasien[char]["Penyakit"]
        ruangan = var.dataPasien[char]["Ruangan"]
        id = char
        lamaMenginap = var.dataPasien[char]["Lama menginap"]

        tableData.append([nama, gender, penyakit, ruangan,
                          id, lamaMenginap + " Hari"])

        print(tabulate(tableData, headers=[
              "Nama", "Gender", "Penyakit", "Ruangan", "ID", "Lama menginap"], tablefmt="presto"))

    def templatePencarian(char, color1, color2):
        nama = var.dataPasien[char]["Nama"]
        gender = var.dataPasien[char]["Gender"]
        penyakit = var.dataPasien[char]["Penyakit"]
        ruangan = var.dataPasien[char]["Ruangan"]
        id = char
        lamaMenginap = var.dataPasien[char]["Lama menginap"]

        # Memasukkan data-data di atas ke dalam variabel tableData
        var.container.append([f"{color1}{nama}{color2}", f"{gender}",
                              f"{penyakit}", f"{ruangan}", f"{id}", f"{lamaMenginap} " + "Hari"])

    # Ini akan mengecek id ketika menyebutkan nama.

    def pencarian(char):
        clear()

        for i in var.dataPasien:
            if char == var.dataPasien[i]["Nama"]:
                var.container = []
                var.peringatan = ""
                templatePencarian(i, '', '')
                break

            else:
                if char[0] == var.dataPasien[i]["Nama"][0]:
                    templatePencarian(i, '', '')
                    var.peringatan = f"{char} tidak ditemukan.Tetapi ada yang mendekati."
                else:
                    pass

        loading("Mencari", 3)

        print(f"{var.peringatan}\n")
        print(tabulate(var.container, headers=[
            "Nama", "Gender", "Penyakit", "Ruangan", "ID", "Lama menginap"], tablefmt="presto"))

        var.container = []
        var.peringatan = ""

    def mengambilIdPasien(char):
        for i in var.dataPasien:
            if char == var.dataPasien[i]["Nama"]:
                return i
            else:
                pass

except ModuleNotFoundError:
    moduleError()
