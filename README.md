# Project-UAS-PBO
# MyFavMovies

**MyFavMovies** adalah aplikasi Python sederhana berbasis OOP (Object-Oriented Programming) yang memungkinkan pengguna mencatat daftar film favorit mereka. Aplikasi ini terinspirasi dari hobi saya menonton film dan keinginan untuk menyimpan data film yang pernah ditonton lengkap dengan review-nya.

## Fitur Utama

- Menambahkan film favorit (yang sudah ditonton atau belum)
- Menyimpan ulasan dan tanggal menonton untuk film yang sudah ditonton
- Menampilkan seluruh daftar film
- Menghapus film dari daftar
- Menyimpan dan memuat data film dalam file `JSON`

## Struktur Project

myfavmovies/
├── main.py # Program utama (CLI)
├── models/
│ ├── movie.py # Definisi kelas Movie & WatchedMovie
│ └── manager.py # Manajemen daftar film
├── data/
│ └── movies.json # Data film tersimpan
└── README.md # Dokumentasi proyek

## Cara Menjalankan

1. Pastikan Python 3 sudah terinstall.
2. Buat virtual environment (opsional tapi disarankan):
Bourne Again Shell (Bash)
   python -m venv env
   source env/bin/activate  # di Linux/Mac
   .\\env\\Scripts\\activate  # di Windows
