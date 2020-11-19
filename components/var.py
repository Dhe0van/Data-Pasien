### JSON File ###
from json import load, dump
import platform

filePath = "components\data.json"


def readData():
    with open(filePath, "r") as docs:
        read = load(docs)
        return read


def writeData():
    with open(filePath, "w") as docs:
        write = dump(dataPasien, docs, indent=2)
        return write

#################

### Variabel utama ###


dataPasien = readData()

tableData = []

######################

### Variabel lain ###

merah = '\033[31m'
hijau = '\033[32m'
putih = '\033[37m'
reset = '\033[0m'


def platform_OS():
    user_OS = platform.system().lower()

    if user_OS == "linux":
        return "linux"
    else:
        return "windows"


container = []

peringatan = ""
