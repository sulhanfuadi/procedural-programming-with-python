# Kuis Coding: Cat Dinding
# January 26, 2024


# SOAL
# Pemilik rumah meminta Bapak Fajar untuk merenovasi rumahnya dengan menambahkan ruang satu kamar tidur. 
# Lalu, Bapak telah menyusun rencana dan pendanaan dalam proses renovasi rumah tersebut. 
# Bapak mulai mendesain tata ruang, menganggarkan biaya furnitur, bahan material, dekorasi, dll. 
# Bapak perlu menyelesaikan konsep desain dan anggaran tersebut supaya proses renovasi segera terlaksana.
# Salah satu anggaran yang Bapak Fajar susun adalah anggaran jumlah cat yang dibutuhkan untuk mengecat dinding ruang. 
# Bapak merasa kebingungan untuk menyusun anggaran tersebut karena tidak tahu berapa liter cat yang harus dibeli. 
# Di sisi lain, Bapak perlu menyelesaikan anggaran ini secepat mungkin agar dapat menyerahkannya ke pemilik rumah.
# Bapak mendapatkan informasi dari rekan kerja bahwa ada cara menghitung jumlah cat berdasarkan ukuran dan tinggi ruangan. 
# Berikut adalah informasi yang didapatkan oleh Bapak.
# Standar pemakaian cat dengan luas dinding 12 meter persegi adalah 1 liter cat untuk satu kali pelapisan.
# Untuk mengetahui luas dinding ruangan, hitunglah keliling dan tinggi ruangan.
# Proses menghitung keliling ruangan (persegi panjang) sebagai berikut.
#     kelilingRuang = 2 * (panjangRuang + lebarRuang)
# Apabila untuk menghitung jumlah cat, perhitungannya sebagai berikut.
#     jumlahLiter = kelilingRuang * tinggiRuang / 12
# Bantulah Bapak Fajar untuk membuat program yang fleksibel digunakan oleh siapa pun untuk mencari jumlah liter cat
# yang diperlukan saat mengecat dinding. Dengan begitu, setiap orang dapat mengetahui jumlah liter cat yang akan dibeli.


# TODO:
#  1. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel panjangRuang.
#  2. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel lebarRuang.
#  3. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel tinggiRuang.
#  4. Buatlah fungsi bernama hitungCat yang memiliki parameter panjangRuang, lebarRuang, dan tinggiRuang.
#     4.1. Hitung keliling ruangan dengan rumus keliling persegi panjang dan simpan pada variabel kelilingRuang.
#     4.2. Hitung jumlah liter cat yang akan dipakai dengan rumus di atas.
#     4.3. Fungsi ini mengembalikan nilai float yang menyatakan jumlah liter cat berdasarkan ketiga nilai tersebut.
#     4.4. Simpan hasil fungsi pada variabel jumlahLiter.
#  5. Cetak nilai jumlahLiter pada teks "Jumlah cat yang Anda perlukan adalah {jumlahLiter} liter."


# SOLUSI:
#  1. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel panjangRuang.
panjangRuang: float = float(input("Masukkan panjang ruangan (meter): "))

#  2. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel lebarRuang.
lebarRuang: float = float(input("Masukkan lebar ruangan (meter): "))

#  3. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel tinggiRuang.
tinggiRuang: float = float(input("Masukkan tinggi ruangan (meter): "))

#  4. Buatlah fungsi bernama hitungCat yang memiliki parameter panjangRuang, lebarRuang, dan tinggiRuang.
def hitungCat(panjangRuang: float, lebarRuang: float, tinggiRuang: float) -> float:
#   4.1. Hitung keliling ruangan dengan rumus keliling persegi panjang dan simpan pada variabel kelilingRuang.
    kelilingRuang = 2 * (panjangRuang + lebarRuang)
#   4.2. Hitung jumlah liter cat yang akan dipakai dengan rumus di atas.
    jumlahLiter = kelilingRuang * tinggiRuang / 12
#   4.3. Fungsi ini mengembalikan nilai float yang menyatakan jumlah liter cat berdasarkan ketiga nilai tersebut.
    return jumlahLiter
#   4.4. Simpan hasil fungsi pada variabel jumlahLiter.
jumlahLiter: float = hitungCat(panjangRuang, lebarRuang, tinggiRuang)

#  5. Cetak nilai jumlahLiter pada teks "Jumlah cat yang Anda perlukan adalah {jumlahLiter} liter."
print(f"Jumlah cat yang Anda perlukan adalah {jumlahLiter} liter.")