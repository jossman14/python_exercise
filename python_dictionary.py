import json
import difflib
from difflib import SequenceMatcher, get_close_matches

# lokasi file
lok_file = "files/3.1 data.json.json"
data = json.load(open(lok_file))

# algoritma cari arti


def cari_arti(kata):
    kata = cari_kesamaan(kata)
    kata = kata.lower()
    if kata in data:
        return data[kata]
    else:
        return ("kata yang anda cari tidak ditemukan, mohon cek lagi kata-kata anda?")


def cari_kesamaan(kata):
    kata = get_close_matches(kata, data.keys())[0]
    return kata


masuk = input("Masukkan kata : ")

print(cari_arti(masuk))
