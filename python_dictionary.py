import json

lok_file = "files/3.1 data.json.json"
data = json.load(open(lok_file))


def cari_arti(kata):
    if kata in data:
        return data[kata]
    else:
        print("kata yang anda cari tidak ditemukan, mohon cek lagi kata-kata anda?")


print(cari_arti{"rain"})



