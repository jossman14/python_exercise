def loop():
    daftar_kata = []
    jumlah = 0
    hasil_akhir = ''
    pertanyaan = ("bagaimana", "apa", "kapan")
    print("program katakan sesuatu, ketik keluar untuk berhenti!, have fun!!")
    while T]
    rue:
        masuk = input("katakan sesuatu : ")
        if masuk != "keluar":
            masuk.lower()
            if masuk.startswith(pertanyaan):
                masuk = masuk + "?"
                print(masuk)
            else:
                masuk += "."
            masuk = masuk.capitalize()
            daftar_kata.append(masuk)
            print(f"ini kata anda ke- {jumlah}")
            jumlah += 1
        else:
            print("")
            print(f"anda telah memasukkan sebanyak {jumlah} kata")
            print("berikut seluruh kata anda: ")
            daftar_kata = sorted(daftar_kata)
            for kata in daftar_kata:
                hasil_akhir = hasil_akhir + " " + kata
            print(" ".join(daftar_kata))
            return daftar_kata
            break

loop()
