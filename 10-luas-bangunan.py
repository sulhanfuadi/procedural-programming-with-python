# Kuis Coding: Luas Bangunan
# January 26, 2024


# SOAL
# Ketika melakukan survei lapangan, Bapak Fajar mendapatkan data terkait pembangunan rumah. 
# Mulai dari luas tanah, ketinggian tanah, kontur tanah, dan lainnya sudah didapatkan oleh Bapak. 
# Rencana yang akan Bapak lakukan selanjutnya adalah mendesain rumah yang sesuai dengan keinginan pemilik.
# Setelah melakukan rekap, luas tanah yang akan dibangun rumah adalah 96 meter persegi. 
# Dalam proses mendesain atau membangun rumah, luas bangunan tidak boleh lebih dari luas tanah. 
# Untuk itu, Bapak Fajar bertanya ke pemilik rumah tentang ukuran rumah yang diinginkan. 
# Alhasil, pemilik rumah menginginkan rumah dengan ukuran 11 x 8 meter persegi.
# Bapak Fajar perlu mendesain rumah dengan luas bangunan berdasarkan keinginan pemilik rumah. 
# Timbul pertanyaan dari Bapak, “Apakah ukuran rumah yang diinginkan pemilik rumah dapat dibangun pada tanah tersebut?”
# Bantulah Bapak untuk membuatkan program yang fleksibel digunakan oleh siapa pun dalam menentukan mampu atau tidaknya rumah 
# dibangun berlandaskan panjang dan lebar rumah beserta luas tanah. 
# Dengan begitu, setiap orang dapat mengetahui bisa atau tidaknya mendesain rumah berdasarkan ukuran yang diminta.


# TODO:
#  1. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel landArea.
#  2. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel width.
#  3. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel length.
#  4. Buatlah fungsi bernama checkArea yang memiliki parameter landArea, width, dan length.
#     4.1. Hitung luas bangunan dengan mengalikan variabel width dan length serta simpan pada variabel buildingArea.
#     4.2. Periksa nilai buildingArea dan landArea dengan kriteria berikut.
#          4.2.1. Apabila nilai buildingArea lebih besar dari landArea, kembalikan nilai False.
#          4.2.2. Apabila nilai buildingArea kurang dari atau sama dengan landArea, kembalikan nilai True.
#     4.3. Fungsi ini mengembalikan nilai boolean yang menyatakan bisa atau tidak bangunan dibangun berdasarkan ketiga nilai tersebut.
#     4.4. Simpan hasil fungsi pada variabel check.
#  5. Buatlah pengondisian dari variabel check dengan kriteria berikut.
#     5.1. Apabila bernilai False, cetaklah teks "Rumah tidak dapat dibangun berdasarkan ketiga nilai tersebut."
#     5.2. Apabila bernilai True, cetaklah teks "Rumah dapat dibangun berdasarkan ketiga nilai tersebut."


# SOLUSI:
# 1. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel landArea.
landArea: float = float(input("Masukkan luas lahan (meter): "))

# 2. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel width.
width: float = float(input("Masukkan lebar bangunan (meter): "))

# 3. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel length.
length: float = float(input("Masukkan panjang bangunan (meter): "))

# 4. Buatlah fungsi bernama checkArea yang memiliki parameter landArea, width, dan length.
def checkArea(landArea: float, width: float, length: float) -> bool:
#   4.1. Hitung luas bangunan dengan mengalikan variabel width dan length serta simpan pada variabel buildingArea.
    buildingArea = width * length
#   4.2. Periksa nilai buildingArea dan landArea dengan kriteria berikut.
#   4.2.1. Apabila nilai buildingArea lebih besar dari landArea, kembalikan nilai False.
    if buildingArea > landArea:
        return False
#   4.2.2. Apabila nilai buildingArea kurang dari atau sama dengan landArea, kembalikan nilai True.
    else:
        return True
#   4.3. Fungsi ini mengembalikan nilai boolean yang menyatakan bisa atau tidak bangunan dibangun berdasarkan ketiga nilai tersebut.

#   4.4. Simpan hasil fungsi pada variabel check.
check: bool = checkArea(landArea, width, length)

# 5. Buatlah pengondisian dari variabel check dengan kriteria berikut.
#   5.1. Apabila bernilai False, cetaklah teks "Rumah tidak dapat dibangun berdasarkan ketiga nilai tersebut."
#   5.2. Apabila bernilai True, cetaklah teks "Rumah dapat dibangun berdasarkan ketiga nilai tersebut."
if check:
    print("Rumah dapat dibangun berdasarkan ketiga nilai tersebut.")
else:
    print("Rumah tidak dapat dibangun berdasarkan ketiga nilai tersebut.")