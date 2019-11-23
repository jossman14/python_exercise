import json
import difflib
from difflib import SequenceMatcher, get_close_matches
import random


# lokasi file
lok_file = "files/3.1 data.json.json"
data = json.load(open(lok_file))

# algoritma cari arti


def cari_arti(kata):
    kata = kata.lower()
    kata = cari_kesamaan(kata)
    if kata in data:
        rand = random.randint(0, len(data[kata]) - 1)
        return data[kata][rand]
    else:
        return("mohon maaf kata anda tidak ditemukan, silahkan cek kembali kata-kata anda")


def cari_kesamaan(kata):
    if kata in data:
        return kata

    else:
        kata = get_close_matches(kata, data.keys())
        for i in range(0, len(kata)):
            try:
                cek = input(
                    f"apakah kata yang anda maksud adalah {kata[i]} ? ketik ya atau tidak : ")
                cek = cek.lower()
                cek = get_close_matches(cek, ['ya', "tidak"])[0]
                if cek == "ya":
                    return kata[i]
                else:
                    pass
            except:
                return("NONONO")
                break


masuk = input("Masukkan kata : ")

print(cari_arti(masuk))
