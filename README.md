# Python Exercise

Kumpulan latihan Python kecil.

## Isi

- `basic.py`: program input teks interaktif (menambah tanda baca, mengurutkan kata).
- `map_python/`: peta interaktif gunung berapi dan populasi dunia dengan Folium (data `vol.txt` / `files/map/Volcanoes.txt` dan `world.json`). `peta.html` adalah contoh hasil peta.
- `python_dictionary/`: kamus bahasa Inggris dari berkas JSON (`files/*.json`) dengan saran kata mirip memakai `difflib`; juga contoh koneksi MySQL (`mysql-connector`).
- `Hosts_blocker/`, `website_host_blocker/`: skrip pemblokir situs web pada jam kerja dengan mengubah berkas `hosts`.
- `*.csv`: berkas data contoh (nama bayi, buku terlaris NYT Kids).
- `flask_web_python/web`: tercatat sebagai submodule tanpa `.gitmodules`, jadi isinya tidak ada di repo ini.

## Cara menjalankan

```bash
pip install folium pandas mysql-connector-python
python basic.py
python map_python/map_python.py
python python_dictionary/python_dictionary.py
```

Jalankan dari root repo karena path data bersifat relatif. Skrip pemblokir memakai path `hosts` lokal/Windows yang perlu disesuaikan dulu.
