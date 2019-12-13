import time
from datetime import datetime as dt

path = r"C:\Windows\System32\drivers\etc\hosts"
temp = r"hosts"
redirect = "127.0.0.1"
web = ["facebook.com", 'www.facebook.com']

while True:
    if 8 <= dt.now().hour < 16:
        print("jam bekerja gan")
        with open(temp, 'r+') as data:
            isi = data.read()
            for i in web:
                if i in isi:
                    pass
                else:
                    data.write(f"{redirect}          {i} \n")
    else:
        print("rampung gan")
        with open(temp, 'r+') as data:
            isi = data.readlines()
            data.seek(0)
            for line in isi:
                if not any(i in line for i in web):
                    data.write(line)
            data.truncate()
    time.sleep(5)
