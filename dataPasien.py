# tugas akhir 
# Nama  : Dheovan Winata Alvian 
# Kelas : 10 Komputer 1
# Program Data Pasien 


from os import system
from time import sleep
# Jika belum terinstall --> $ pip3 install tabulate
from tabulate import tabulate
from datetime import datetime

####################################################

# Fungsi ekstra

# Fungsi yang memuat animasi loading (Biar Keren)
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

# Jika data pasien kosong
def dataKosong(char):
    # Diberi variabel kosong supaya bisa menampung data yg diberikan
    tableData = []
    if len(char) == 0:
        tableData.append(["Maaf Tetapi data saat ini masih kosong."])
        print(tabulate(tableData))
    else:
        pass


# Ini untuk memverifikasi apakah user yakin dengan pilihannya tersebut.
def verifikasiUser(char):
    userInput = input(f"\nApakah anda yakin ingin {char} data Pasien ini? [{hijau}Y{normal}/{merah}n{normal}]: ").upper()

    return userInput


# Ini untuk menampilkan Tabel
def tampilkanTable(char):
    system("clear")
    tableData = []
    nama = dataPasien[char]["Nama"]
    gender = dataPasien[char]["Gender"]
    penyakit = dataPasien[char]["Penyakit"]
    ruangan = dataPasien[char]["Ruangan"]
    id = char
    lamaMenginap = dataPasien[char]["Lama menginap"]

    # Memasukkan data-data di atas ke dalam variabel tableData
    tableData.append([nama, gender, penyakit, ruangan, id, lamaMenginap + " Hari"])

    system("clear")

    print("Data telah ditemukan.\n")
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
        # Tetapi jika tidak ada akan muncul ini.
        else:
            loading("Mencari", 2)
            # Jika huruf paling depan dari inputUser sama pada saat looping dataPasien.
            if char[0] == dataPasien[i]["Nama"][0]:
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

# variabel penting untuk program

putih = "\033[97m"
biruBG = "\033[44m"
merah = "\033[91m"
normal = "\033[0m"
hijau = "\033[92m"
lumut = "\033[42m"


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
    system("clear")
    nama = input("Tambahkan Nama: ")
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


# Fungsi untuk menghapus data Pasien
def hapusData():

    # Coba eksekusi terlebih dahulu.
    try:
        system("clear")
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
                    verifikasiUser("Menghapus")
                    if verifikasiUser:
                        loading("Menghapus", 3)
                        del dataPasien[idBaru]
                        print("Data telah dihapus")
                    else:
                        print("Batal menghapus data.")

    # Jika input dari user kosong (Langsung Enter) maka akan muncul pesan ini
    except IndexError:
        print("Anda tidak boleh mengosongkannya!!!")                

    finally:
        input("Tekan ENTER untuk kembali.")


# Fungsi untuk mencari Pasien dalam dataPasien
def cariData():
    system("clear")
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
    system("clear")

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

                    print(f"{char} Pasien telah diubah.")
                    # Keluar dari loop
                    break

                # Jika user tidak setuju
                elif persetujuan == "N":
                    print("Data batal diubah")
                    # Keluar dari loop
                    break
                
                # Jika user memberikan input selain [Y/n]
                else:
                    print(f"Silahkan Pilih {hijau}Y{normal} atau {merah}n{normal}.")
                    # Akan kembali lagi ke proses while-loop karena infinite sampai user memberikan input [Y/n]


# Fungsi untuk memperbarui data Pasien
def perbaruiData():
    system("clear")

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
            # Opsinya
            print("""\n Opsi
            [1] Nama
            [2] Gender
            [3] Penyakit
            [4] Ruangan
            [5] Lama menginap
            """)

            inputPilihanUser = input("Silahkan pilih opsi di atas yang ingin anda ubah dari Pasien ini: ")

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
                templatePerbarui(idPasien, "Lama menginap", dataPasien[idPasien]["Lama menginap"])
            
    
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
            hapusData()
        elif inputPilihanUser == "4":
            cariData()
        elif inputPilihanUser == "5":
            perbaruiData()
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
