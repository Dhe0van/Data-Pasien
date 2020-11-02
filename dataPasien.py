# tugas akhir
# Nama  : Dheovan Winata Alvian
# Kelas : 10 Komputer 1
# Program Data Pasien

import os
import platform
from getpass import getpass


# Fungsi ini untuk mengetahui OS apa yang digunakan oleh user? hanya mendukung windows dan linux
def platform_OS():
    user_OS = platform.system().lower()

    if user_OS == "linux":
        return "linux"
    else:
        return "windows"


####################################################

# variabel penting untuk program

os.system("")

# Kumpulan Warna (Hasil copas internet)
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'



dataPasien = {
    "20201029-A001":{
        "Nama":"Lol",
        "Gender":"Cewe",
        "Penyakit":"OK",
        "Ruangan":"Reg",
        "Lama menginap":"2"
    },
    "20201029-A002":{
        "Nama":"lopi",
        "Gender":"Cewe",
        "Penyakit":"OK",
        "Ruangan":"Reg",
        "Lama menginap":"2"
    }
}

####################################################

# Dicoba terlebih dahulu apakah ada error atau tidak.
try:
    from time import sleep
    from tabulate import tabulate
    # Jika belum terinstall --> $ pip3 install tabulate
    from datetime import datetime

    ####################################################

    # Fungsi ekstra


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
            sleep(0.2)
            clear()
            print(char + " |")
            sleep(0.2)
            clear()
            print(char + " /")
            sleep(0.2)
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
        persetujuan = input(f"\nApakah anda yakin ingin {char} data Pasien ini? [{style.GREEN}Y{style.RESET}/{style.RED}n{style.RESET}]: ").upper()
        return persetujuan

    # Ini untuk menampilkan Tabel
    def tampilkanTable(char):
        clear()
        tableData = []
        nama = dataPasien[char]["Nama"]
        gender = dataPasien[char]["Gender"]
        penyakit = dataPasien[char]["Penyakit"]
        ruangan = dataPasien[char]["Ruangan"]
        id = char
        lamaMenginap = dataPasien[char]["Lama menginap"]

        # Memasukkan data-data di atas ke dalam variabel tableData
        tableData.append([nama, gender, penyakit, ruangan, id, lamaMenginap + " Hari"])

        clear()

        # print("Data telah ditemukan.\n")
        # Menampilkan Tabel nya
        hasil = print(tabulate(tableData, headers=["Nama", "Gender", "Penyakit", "Ruangan", "ID", "Lama menginap"], tablefmt="presto"))
        # DISCLAIMER : tidak tahu kenapa kalau dimasukkan dalam variabel berhasil sedangkan tanpa variabel tidak.


    # Ini akan mengambil id ketika menyebutkan nama.
    def mengambilIdDariNama(char):
        # Looping seluruh dataPasien.
        for i in dataPasien:
            if char == dataPasien[i]["Nama"]:
                loading("Mencari", 3)
                # Akan menampilkan tabel Pasien jika ada.
                tampilkanTable(i)
                return i
                break
            # Tetapi jika tidak ada akan muncul ini.
            else:
                # Jika huruf paling depan dari inputUser sama pada saat looping dataPasien.
                if char[0] == dataPasien[i]["Nama"][0]:
                    loading("Mencari", 2)
                    print(f"Nama Pasien {char} tidak ditemukan, Tetapi ditemukan yang mendekati:")
                    # Looping lagi untuk menampilkan nama-nama Pasien yang mendekati

                    # NOTE : Kalau tidak diberi for-loop maka print yang nama pasien ... di atas akan tercetak sebanyak jumlah pasien di dalam dataPasien (Begitulah)

                    for j in dataPasien:
                        # Sekali lagi jika ada huruf paling depan dari inputCariData dengan huruf paling depan dari nama Pasien

                        if char[0] == dataPasien[j]["Nama"][0]:
                            print(dataPasien[j]["Nama"])
                    # Lalu berhenti agar tidak terjadi tidak tercetak dua kali langkah-langkah yang di atas
                    break





    ####################################################






    ####################################################

    # Fungsi-fungsi yang penting/crusial

    # Membuat id untuk pasien baru
    def idPasien():
        # Memberikan tanggal, bulan, tahun hari ini
        idHariIni = datetime.now()
        tgl = idHariIni.day
        bulan = idHariIni.month
        tahun = idHariIni.year
        kodeId = len(dataPasien) + 1

        idBaru  = ("%4d%2d%02d-A%03d" % (tahun, bulan, tgl, kodeId))
        # Akan memberikan value baru yaitu idBaru saja
        return idBaru


    # Menampilkan tampilan menu
    def displayMenu():
        print(f"""
        *** Program Data Pasien ***
        Selamat datang {inputUserName}.
        Silahkan pilih salah satu pilihan berikut:
        [1] {style.WHITE}Menampilkan data pasien.{style.RESET}
        [2] {style.WHITE}Menambahkan data pasien.{style.RESET}
        [3] {style.WHITE}Menghapus data pasien.{style.RESET}
        [4] {style.WHITE}Mencari data pasien.{style.RESET}
        [5] {style.WHITE}Perbarui data pasien.{style.RESET}
        [?] {style.WHITE}Tentang program ini.{style.RESET}
        [{style.RED}Q{style.RESET}] {style.WHITE}Keluar dari program.{style.RESET}
        """)


    # Menampilkan data pasien
    def tampilkanData():
        clear()
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



    # Menambahkan data ke ke dalam dataPasien
    def tambahkanData():
        clear()
        nama = input("Tambahkan Nama: ")

        while True:
            if nama == "":
                print("Nama tidak boleh kosong!!!")
                nama = input("Tambahkan Nama: ")
            else:
                break

        # Looping untuk mengecek semua jumlah data di pasien
        for i in dataPasien:
            # Jika nama baru ada yang sama dengan nama pasien lain
            if nama == dataPasien[i]["Nama"]:
                print("Maaf tetapi terdapat nama Pasien yang sama.")
                break
        # Jika nama pasien baru/berbeda
        else:
            gender = input("Tambahkan Gender: ")
            penyakit = input("Tambahkan Penyakit: ")
            ruangan = input("Tambahkan tipe Ruangan: ")
            id = idPasien()

            lamaMenginap = input("Tambahkan lama Pasien menginap: ")

            # Bagian ini untuk mengecek apakah lama menginap yang dimasukkan angka atau bukan
            while True:
                try:
                    # Coba terlebih dahulu di konversi ke angka
                    converted = int(lamaMenginap)
                    # Jika yang dimasukkan adalah angka
                    break
                # Jika ternyata bukan angka maka akan muncul pesan ini dan akan diulang input nya.
                except ValueError:
                    print("Maaf tetapi Lama menginap pasien harus dalam bentuk angka.")
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
                    clear()
                    tableData= []
                    # Menampilkan data yang tadi ke dalam bentuk tabel
                    tableData.append([nama, gender, penyakit, ruangan, id, lamaMenginap + " Hari"])
                    print(tabulate(tableData, headers=["Nama", "Gender", "Penyakit", "Ruangan", "ID", "Lama menginap"], tablefmt="presto"))
                    print("\nData berhasil disimpan.")
                    break
                elif userInput == "N":
                    break
                else:
                    print(f"Silahkan Pilih {style.GREEN}Y{style.RESET} atau {style.RED}n{style.RESET}.")

        input("\nTekan ENTER untuk kembali.")


    # Fungsi untuk menghapus data Pasien
    def hapusData():

        # Coba eksekusi terlebih dahulu.
        try:
            clear()
            # Jika data pasien kosong
            if len(dataPasien) == 0:
                dataKosong(dataPasien)
            # Jika terdapat data di dalam dataPasien
            else:
                inputDelData = input("Silahkan masukkan nama pasien yang ingin dihapus\n(Jika tidak menampilkan apa-apa maka itu berarti pencarian tidak ada yang mendekati):  ")
                idBaru = mengambilIdDariNama(inputDelData)

                if inputDelData == "":
                    print("Tidak boleh kosong!")
                else:
                    # Jika nama yang dicari ada di dalam dataPasien
                    if idBaru:
                        persetujuan = verifikasiUser("Menghapus")
                        while True:
                            if persetujuan == "Y":
                                loading("Menghapus", 3)
                                del dataPasien[idBaru]
                                print("Data telah dihapus")
                                break
                            elif persetujuan == "N":
                                break
                            else:
                                print(f"Hanya Masukkan {style.GREEN}Y{style.RESET} atau {style.RED}n{style.RESET}")
                                persetujuan = verifikasiUser("Menghapus")

        # Jika input dari user kosong (Langsung Enter) maka akan muncul pesan ini
        except IndexError:
            print("Anda tidak boleh mengosongkannya!!!")

        finally:
            input("\nTekan ENTER untuk kembali.")


    # Fungsi untuk mencari Pasien dalam dataPasien
    def cariData():
        clear()
        # Coba eksekusi dulu.
        try:
            # Jika tidak ada apa-apa di dalam dataPasien.
            if len(dataPasien) == 0:
                dataKosong(dataPasien)
            # Jika ada sesuatu di dalam dataPasien.
            else:
                inputCariData = input("Silahkan masukkan nama Pasien yang ingin dicari.\n(Jika pencarian tidak menampilkan apa-apa berarti tidak ada yang mendekati): ")

                # Yang disini mencari ID dan mencocokkan nya dengan data dari Pasien lain ada di Line 70-92.
                idPasien = mengambilIdDariNama(inputCariData)


        # Jika user memasukkan input kosong.
        except IndexError:
            print("Maaf tetapi anda tidak boleh mengosongkannya.")

        finally:
            input("\nTekan ENTER untuk kembali.")


    # Bagian cakupan dari perbarui data


    # Membuat template agar dapat dipakai berulang-ulang di pengkondisian perbaruiData
    def templatePerbarui(idPasien, char, dataPasienSebelumnya):
        clear()

        # Mengubah data
        inputUbah = input(f"Silahkan ubah {char} pasien sesuai yang anda inginkan: ")

        # Jika data yang baru saja dimasukkan sama dengan data yang sebelumnya
        if inputUbah == dataPasienSebelumnya:
            print(f"Maaf tetapi {char} Pasien tidak boleh sama dengan sebelumnya.")

        # Jika data yang baru saja dimasukkan berbeda dengan data yang sebelumnya
        else:

            # Infinite loop agar verifikasi user dapat dilakukan berulang kali jika ada kesalahan dalam mengetik
            while True:
                # Jika user memeberi input kosong.
                if inputUbah == "":
                    print(f"{char} Pasien tidak boleh kosong!!!")
                    inputUbah = input(f"Silahkan ubah {char} pasien sesuai yang anda inginkan: ")
                # Jika user memberikan input selain input Kosong
                else:
                    # Meminta verifikasi/persetujuan dari User
                    persetujuan = verifikasiUser("Mengubah Nama")

                    # Jika User Setuju
                    if persetujuan == "Y":
                        # Animasi Loading
                        loading("Mengubah", 3)

                        # Mengubah data sebelumnya menjadi data baru
                        dataPasien[idPasien][f"{char}"] = inputUbah

                        tampilkanTable(idPasien)

                        print(f"\n{style.GREEN}{char}{style.RESET} Pasien telah diubah.")
                        # Keluar dari loop
                        break

                    # Jika user tidak setuju
                    elif persetujuan == "N":
                        print("Data batal diubah")
                        # Keluar dari loop
                        break

                    # Jika user memberikan input selain [Y/n]
                    else:
                        print(f"Silahkan Pilih {style.GREEN}Y{style.RESET} atau {style.RED}n{style.RESET}.")
                        # Akan kembali lagi ke proses while-loop karena infinite sampai user memberikan input [Y/n]
        input("\nTekan ENTER untuk kembali.")

    def templatePerbaruiLamaMenginap(idPasien, char, dataPasienSebelumnya):
        clear()

        inputUbah = input("Ubah lama Pasien menginap: ")

        # Mengubah data
        # Terpaksa dibuat berulang karena kalau dimasukkan ke dalam fungsi maka nilainya akan muncul yang salah pertama kali.
        while True:
            try:
                # Coba terlebih dahulu di konversi ke angka
                converted = int(inputUbah)
                # Jika yang dimasukkan adalah angka
                break
            # Jika ternyata bukan angka maka akan muncul pesan ini dan akan diulang input nya.
            except ValueError:
                print("Maaf tetapi Lama menginap pasien harus dalam bentuk angka.")
                inputUbah = input("Ubah lama Pasien menginap: ")

        # Jika data yang baru saja dimasukkan sama dengan data yang sebelumnya
        if inputUbah == dataPasienSebelumnya:
            print(f"Maaf tetapi {char} Pasien tidak boleh sama dengan sebelumnya.")

        # Jika data yang baru saja dimasukkan berbeda dengan data yang sebelumnya
        else:

            # Infinite loop agar verifikasi user dapat dilakukan berulang kali jika ada kesalahan dalam mengetik
            while True:
                # Jika user memeberi input kosong.
                if inputUbah == "":
                    print(f"{char} Pasien tidak boleh kosong!!!")
                    inputUbah = input(f"Silahkan ubah {char} pasien sesuai yang anda inginkan: ")
                # Jika user memberikan input selain input Kosong
                else:
                    # Meminta verifikasi/persetujuan dari User
                    persetujuan = verifikasiUser("Mengubah Nama")

                    # Jika User Setuju
                    if persetujuan == "Y":
                        # Animasi Loading
                        loading("Mengubah", 3)

                        # Mengubah data sebelumnya menjadi data baru
                        dataPasien[idPasien][f"{char}"] = inputUbah

                        tampilkanTable(idPasien)

                        print(f"\n{style.GREEN}{char}{style.RESET} Pasien telah diubah.")
                        # Keluar dari loop
                        break

                    # Jika user tidak setuju
                    elif persetujuan == "N":
                        print("Data batal diubah")
                        # Keluar dari loop
                        break

                    # Jika user memberikan input selain [Y/n]
                    else:
                        print(f"Silahkan Pilih {style.GREEN}Y{style.RESET} atau {style.RED}n{style.RESET}.")
                        # Akan kembali lagi ke proses while-loop karena infinite sampai user memberikan input [Y/n]
        input("\nTekan ENTER untuk kembali.")

    # Fungsi untuk memperbarui data Pasien
    def perbaruiData():
        clear()

        # Jika tidak ada apa-apa di dalam dataPasien
        if len(dataPasien) == 0:
            dataKosong(dataPasien)

        # Jika ada sesuatu
        else:
            inputPerbaruiData = input("Masukkan nama Pasien yang ingin anda ubah datanya: ")

            # Mengambil id pasien.
            idPasien = mengambilIdDariNama(inputPerbaruiData)

            # Jika idPasien meng-return sesuatu maka akan masuk ke kondisi ini.
            if idPasien:
                while True:
                    tampilkanTable(idPasien)
                    # Opsinya
                    print(f"""\n Opsi
                    [1] Nama
                    [2] Gender
                    [3] Penyakit
                    [4] Ruangan
                    [5] Lama menginap
                    [{style.RED}Q{style.RESET}] Kembali ke menu utama
                    """)

                    inputPilihanUser = input("Silahkan pilih opsi di atas yang ingin anda ubah dari Pasien ini: ").upper()
                    # Kondisi untuk Nama
                    if inputPilihanUser == "1":
                        templatePerbarui(idPasien, "Nama", inputPerbaruiData)

                    # Kondisi untuk Gender
                    elif inputPilihanUser == "2":
                        templatePerbarui(idPasien, "Gender", dataPasien[idPasien]["Gender"])

                    # Kondisi untuk Penyakit
                    elif inputPilihanUser == "3":
                        templatePerbarui(idPasien, "Penyakit", dataPasien[idPasien]["Penyakit"])

                    # Kondisi untuk Ruangan
                    elif inputPilihanUser == "4":
                        templatePerbarui(idPasien, "Ruangan", dataPasien[idPasien]["Ruangan"])

                    # Kondisi untuk Lama menginap
                    elif inputPilihanUser == "5":
                        templatePerbaruiLamaMenginap(idPasien, "Lama menginap", dataPasien[idPasien]["Lama menginap"])

                    elif inputPilihanUser == "Q":
                        break

                    else:
                        print("Hanya masukkan angka 1-5 atau huruf Q ")

                        inputPilihanUser = input("Silahkan pilih opsi di atas yang ingin anda ubah dari Pasien ini: ")

        input("\nTekan ENTER untuk kembali.")


    # Bagian ini cuma menampilkan informasi program ini.
    def tentang():
        clear()
        print("""
    Dibuat oleh:
    Nama : Dheovan Winata Alvian
    Kelas: 10 Komputer 1
    \nTerima kasih telah memakai program ini!!!
        """)
        input("\nTekan ENTER untuk kembali.")


    # Keseluruhan proses dari progra,
    def proses():
        while True:
            clear()
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
                cariData()
            elif inputPilihanUser == "5":
                perbaruiData()
            elif inputPilihanUser == "?":
                tentang()
            # Jika user menginput selain 1-5, Q, ?
            else:
                clear()
                print("Hanya masukkan kata kunci sesuai di tampilan menu.")
                input("\nTekan ENTER untuk kembali.")


    inputUserName = input("Masukkan Nama Anda: ")
    # Disini password apapun akan benar kecuali Kosong
    inputUserPasswd = getpass(prompt="Masukkan Password Anda: ")
    # User login dan memverifikasi password
    while inputUserPasswd == "":
        loading("Mengecek Password", 2)
        print(f"Maaf Password tidak boleh {style.RED}KOSONG{style.RESET}.")
        inputUserPasswd = getpass(prompt="Masukkan Password Anda: ")
    else:
        loading("Mengecek Password", 3)
        print("Baiklah silahkan masuk.")
        sleep(0.7)
        proses()

# Jika terjadi error yang dimana errornya adalah adanya module yang belum terpasang di sistem operasi User
except ModuleNotFoundError:
    print(f"Maaf tetapi anda memiliki 1 module yang belum terpasang\nDibutuhkan module yang lengkap agar program dapat berjalan dengan optimal\nHarap menginstall \"pip\" terlebih dahulu.\n")

    persetujuan = input(f"Apakah anda ingin menginstall module yang dibutuhkan sekarang? (Module yang dibutuhkan = Tabulate) [{style.GREEN}Y{style.RESET}/{style.RED}n{style.RESET}]: ").upper()

    while True:
        if persetujuan == "Y":
            # Akan execute command line pip3 install tabulate jika sistem operasi user adalah Linux
            if platform_OS() == "linux":
                commandBash = os.popen("pip3 install tabulate")
                print(commandBash.read())
                break
            # Akan execute command line cmd /k pip3 install tabulate jika sistem operasi user adalah windows
            else:
                os.system('cmd /k "pip3 install tabulate"')
                break
        elif persetujuan == "N":
            break
        else:
            print(f"Silahkan Pilih {style.GREEN}Y{style.RESET} atau {style.RED}n{style.RESET}.")

            persetujuan = input(f"Apakah anda ingin menginstall module yang dibutuhkan sekarang? (Module yang dibutuhkan = Tabulate) [{style.GREEN}Y{style.RESET}/{style.RED}n{style.RESET}]: ").upper()
