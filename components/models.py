from components import extra, var

# try:
from time import sleep
from tabulate import tabulate
# Jika belum terinstall --> $ pip3 install tabulate
from datetime import datetime


# Membuat id untuk pasien baru
def idPasien():
    # Memberikan tanggal, bulan, tahun hari ini
    idHariIni = datetime.now()
    tgl = idHariIni.day
    bulan = idHariIni.month
    tahun = idHariIni.year
    kodeId = len(var.dataPasien) + 1

    idBaru = ("%4d%2d%02d-A%03d" % (tahun, bulan, tgl, kodeId))
    # Akan memberikan value baru yaitu idBaru saja
    return idBaru


# Menampilkan data pasien
def tampilkanData():

    extra.clear()

    tableData = []
    if len(var.dataPasien) == 0:
        extra.dataKosong(var.dataPasien)
    else:
        for i in var.dataPasien:
            nama = var.dataPasien[i]["Nama"]
            gender = var.dataPasien[i]["Gender"]
            penyakit = var.dataPasien[i]["Penyakit"]
            ruangan = var.dataPasien[i]["Ruangan"]
            id = i
            lamaMenginap = var.dataPasien[i]["Lama menginap"]
            tableData.append([nama, gender, penyakit, ruangan, id, lamaMenginap + " Hari"])
        # Menampilkan data pasien dalam bentuk tabel
        print(tabulate(tableData, headers=["Nama", "Gender", "Penyakit", "Ruangan", "ID", "Lama menginap"], tablefmt="presto"))
    input("\nTekan ENTER untuk kembali.")


# Menambahkan data ke ke dalam var.dataPasien
def tambahkanData():
    extra.clear()
    nama = input("Tambahkan Nama: ")

    while True:
        if nama == "":
            print("Nama tidak boleh kosong!!!")
            nama = input("Tambahkan Nama: ")
        else:
            break

    for i in var.dataPasien:
        # Jika nama baru ada yang sama dengan nama pasien lain
        if nama == var.dataPasien[i]["Nama"]:
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
                int(lamaMenginap)
                break
            # Jika ternyata bukan angka maka akan muncul pesan ini dan akan diulang input nya.
            except ValueError:
                print("Maaf tetapi Lama menginap pasien harus dalam bentuk angka.")
                lamaMenginap = input("Tambahkan lama Pasien menginap: ")

        while True:
            userInput = extra.verifikasiUser("Menyimpan")
            if userInput == "Y":
                # memakai animasi extra.loading yang diulang sebanyak 4 kali
                extra.loading("Menyimpan data", 4)
                # Ini akan memasukkan data yang baru saja ditambahkan ke dalam var.dataPasien
                var.dataPasien[id] = {
                    "Nama": nama,
                    "Gender": gender,
                    "Penyakit": penyakit,
                    "Ruangan": ruangan,
                    "Lama menginap": lamaMenginap
                }
                extra.clear()
                var.tableData = []

                var.writeData()

                # Menampilkan data yang tadi ke dalam bentuk tabel
                var.tableData.append([nama, gender, penyakit, ruangan, id, lamaMenginap + " Hari"])

                print(tabulate(var.tableData, headers=["Nama", "Gender", "Penyakit", "Ruangan", "ID", "Lama menginap"], tablefmt="presto"))

                print("\nData berhasil disimpan.")

                break

            elif userInput == "N":
                break
            else:
                print(f"Silahkan Pilih {var.hijau}Y{var.reset} atau {var.merah}n{var.reset}.")

    input("\nTekan ENTER untuk kembali.")


# Fungsi untuk menghapus data Pasien
def hapusData():

    try:
        extra.clear()
        if len(var.dataPasien) == 0:
            extra.dataKosong(var.dataPasien)
        else:
            inputDelData = input("Silahkan masukkan nama pasien yang ingin dihapus:  ")

            extra.pencarian(inputDelData)

            idPasien = extra.mengambilIdPasien(inputDelData)

            if idPasien:
                persetujuan = extra.verifikasiUser("Menghapus")
                while True:
                    if persetujuan == "Y":
                        extra.loading("Menghapus", 3)
                        del var.dataPasien[idPasien]

                        var.writeData()

                        print("Data telah dihapus")
                        break
                    elif persetujuan == "N":
                        break
                    else:
                        print(f"Hanya Masukkan {var.hijau}Y{var.reset} atau {var.merah}n{var.reset}")
                        persetujuan = extra.verifikasiUser("Menghapus")

    except IndexError:
        print("Anda tidak boleh mengosongkannya!!!")

    finally:
        input("\nTekan ENTER untuk kembali.")


# Fungsi untuk mencari Pasien dalam var.dataPasien
def cariData():
    extra.clear()
    try:
        if len(var.dataPasien) == 0:
            extra.dataKosong(var.dataPasien)
        else:
            inputCariData = input(
                "Silahkan masukkan nama Pasien yang ingin dicari: ")

            # Yang disini mencari ID dan mencocokkan nya dengan data dari Pasien lain ada di Line 70-92.
            extra.pencarian(inputCariData)

    except IndexError:
        print("Maaf tetapi anda tidak boleh mengosongkannya.")

    finally:
        input("\nTekan ENTER untuk kembali.")


def templatePerbarui(idPasien, char, dataPasienSebelumnya, lamaMenginap=None, nama=None):
    extra.clear()

    inputUbah = input(f"Silahkan ubah {char} pasien sesuai yang anda inginkan: ")

    if lamaMenginap == True:
        while True:
            try:
                # Coba terlebih dahulu di konversi ke angka
                int(inputUbah)
                break
            # Jika ternyata bukan angka maka akan muncul pesan ini dan akan diulang input nya.
            except ValueError:
                print("Maaf tetapi Lama menginap pasien harus dalam bentuk angka.")
                inputUbah = input(f"Silahkan ubah {char} pasien sesuai yang anda inginkan: ")
    else:
        pass

    if inputUbah == dataPasienSebelumnya:
        print( f"Maaf tetapi {char} Pasien tidak boleh sama dengan sebelumnya.")

    else:

        while True:

            if nama == True:

                var.container = []

                for i in var.dataPasien:
                    var.container.append(var.dataPasien[i]["Nama"])

                while True:
                    if inputUbah in var.container:
                        print("Maaf tetapi nama pasien tidak boleh sama dengan nama pasien lainnya.\n")
                        inputUbah = input(f"Silahkan ubah {char} pasien sesuai yang anda inginkan: ")
                    else:
                        break

            if inputUbah == "":
                print(f"{char} Pasien tidak boleh kosong!!!\n")
                inputUbah = input(f"Silahkan ubah {char} pasien sesuai yang anda inginkan: ")
            else:

                persetujuan = extra.verifikasiUser("Mengubah Nama")

                if persetujuan == "Y":
                    # Animasi extra.loading
                    extra.loading("Mengubah", 3)

                    var.dataPasien[idPasien][f"{char}"] = inputUbah

                    extra.tampilkanTable(idPasien)

                    var.writeData()

                    print(
                        f"\n{var.hijau}{char}{var.reset} Pasien telah diubah.")
                    break

                elif persetujuan == "N":
                    print("Data batal diubah")
                    break

                else:
                    print(f"Silahkan Pilih {var.hijau}Y{var.reset} atau {var.merah}n{var.reset}.")

    input("\nTekan ENTER untuk kembali.")

# Fungsi untuk memperbarui data Pasien


def perbaruiData():
    extra.clear()

    if len(var.dataPasien) == 0:
        extra.dataKosong(var.dataPasien)

    else:
        inputPerbaruiData = input("Masukkan nama Pasien yang ingin anda ubah datanya: ")

        extra.pencarian(inputPerbaruiData)

        idPasien = extra.mengambilIdPasien(inputPerbaruiData)

        if idPasien:
            while True:
                extra.tampilkanTable(idPasien)
                # extra.tampilkanTable(idPasien)
                print(f"""\n Opsi
                [1] Nama
                [2] Gender
                [3] Penyakit
                [4] Ruangan
                [5] Lama menginap
                [{var.merah}Q{var.reset}] Kembali ke menu utama
                """)

                inputPilihanUser = input("Silahkan pilih opsi di atas yang ingin anda ubah dari Pasien ini: ").upper()
                # Kondisi untuk Nama
                if inputPilihanUser == "1":
                    templatePerbarui(idPasien, "Nama",inputPerbaruiData, nama=True)

                # Kondisi untuk Gender
                elif inputPilihanUser == "2":
                    templatePerbarui(idPasien, "Gender", var.dataPasien[idPasien]["Gender"])

                # Kondisi untuk Penyakit
                elif inputPilihanUser == "3":
                    templatePerbarui(idPasien, "Penyakit", var.dataPasien[idPasien]["Penyakit"])

                # Kondisi untuk Ruangan
                elif inputPilihanUser == "4":
                    templatePerbarui(idPasien, "Ruangan", var.dataPasien[idPasien]["Ruangan"])

                # Kondisi untuk Lama menginap
                elif inputPilihanUser == "5":
                    templatePerbarui(idPasien, "Lama menginap", var.dataPasien[idPasien]["Lama menginap"], lamaMenginap=True)

                elif inputPilihanUser == "Q":
                    break

                else:
                    extra.clear()
                    print("Hanya masukkan angka 1-5 atau huruf Q ")
                    input("\nTekan ENTER untuk kembali.")

    input("\nTekan ENTER untuk kembali.")

# Bagian ini cuma menampilkan informasi program ini.


def tentang():
    extra.clear()
    print("""
Dibuat oleh:
Nama : Dheovan Winata Alvian
Kelas: 10 Komputer 1

https://github.com/Dhe0van/Data-Pasien
\nTerima kasih telah memakai program ini!!!
    """)
    input("\nTekan ENTER untuk kembali.")
