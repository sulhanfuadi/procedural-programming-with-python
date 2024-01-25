# Kuis Coding: Format Jam
# January 25, 2024

# SOAL
# Bapak Fajar sedang bekerja di tempat proyek pembangunan rumah. 
# Seluruh karyawan melakukan presensi secara mandiri melalui check clock yang tersedia di proyek tersebut, 
# termasuk Bapak Fajar. Hal ini diwajibkan untuk mengetahui waktu kedatangan dan kepulangan setiap karyawan.
# Bapak Fajar datang pada pukul 09:23:57 dan pulang pada pukul 15:25:43. 
# Selama lebih dari 6 jam, beliau bekerja semaksimal mungkin untuk menyelesaikan tugas pada hari tersebut. 
# Sistem check clock akan mencatat waktu kedatangan dan kepulangan Bapak Fajar secara otomatis.
# Untuk mempermudah proses pencatatan, buatlah program sederhana yang mampu menyimpan waktu kedatangan 
# dan kepulangan ke dalam variabel bertipe data dictionary.

# TODO:
#  1. Buatlah variabel startTime bertipe data dictionary sebagai waktu datang dengan kriteria berikut.
#     - key "HH" bernilai angka 9
#     - key "mm" bernilai angka 23
#     - key "ss" bernilai angka 57
#  2. Buatlah variabel endTime bertipe data dictionary sebagai waktu pulang dengan kriteria berikut.
#     - key "HH" bernilai angka 15
#     - key "mm" bernilai angka 25
#     - key "ss" bernilai angka 43

# SOLUSI:
# SOLUSI 1 - Menggunakan type annotation
# 1. Buat variabel startTime bertipe data dictionary
startTime: dict[str, int] = {"HH": 9, "mm": 23, "ss": 57}
# 2. Buat variabel endTime bertipe data dictionary
endTime: dict[str, int] = {"HH": 15, "mm": 25, "ss": 43}