# Kuis Coding: Perhitungan Angka Ganjil
# January 26, 2024


# SOAL
# Saat belajar di sekolah, Bima mendapati guru mengajar mata pelajaran matematika yang membahas tentang barisan aritmetika. 
# Dalam pembahasannya, Bima belajar banyak hal tentang barisan aritmetika, mulai dari pengertiannya, contohnya, 
# menentukan beda antar suku, hingga mencari nilai suku ke-n. Berikut adalah ringkasan materi terkait barisan aritmetika.
# Barisan aritmetika adalah barisan bilangan dengan beda atau selisih yang tetap/sama untuk setiap suku yang berurutan.
# Contoh barisan aritmetika adalah 3, 7, 11, 15, …, dst.
# Berdasarkan contoh di atas,
#     angka 3 adalah suku pertama atau disebut U1;
#     angka 7 adalah suku kedua atau disebut U2;
#     angka 11 adalah suku ketiga atau disebut U3; dst.
# Antar suku memiliki beda bernilai 4 karena U2 - U1 = U3 - U2 = Un - Un-1 = 4.
# Menentukan suku ke-n dapat dihitung melalui persamaan Un= a + (n - 1) * b dan
#     a adalah suku pertama atau U1;
#     n adalah jumlah suku yang ingin dicari; 
#     b adalah beda antar suku; serta
#     Un adalah suku ke n.
# Apabila ditanya nilai suku ke-20 dari contoh barisan aritmetika di atas, cara menghitungnya sebagai berikut.
#     Nilai a = 3, b = 4, dan n = 20.
#     Nilai U20 = 3 + (20 - 1) * 4 atau setara dengan 79.
# Di akhir kelas, guru memberikan soal yang mudah kepada seluruh siswa kelas, yaitu 
# membuat barisan aritmetika bilangan ganjil positif. Bilangan ini meliputi angka 1, 3, 5, 7, …, dst. 
# Soalnya adalah tentukan suku ke-24 dengan mencetak seluruh suku dari 1 hingga terakhir.
# Bantulah Bima untuk membuat program yang fleksibel digunakan oleh siapa pun dalam mencari suku ke-n dari 
# barisan aritmetika bilangan ganjil positif. Dengan begitu, setiap orang dapat mengetahui 
# bilangan ganjil mulai dari 1 hingga suku ke-n.
# Catatan:
# Gunakan perintah print dengan parameter end untuk mengubah karakter terakhir menjadi karakter tertentu.


# TODO:
#  1. Buatlah variabel a bertipe data integer yang bernilai 1 untuk menyimpan nilai suku pertama.
#  2. Buatlah variabel b bertipe data integer yang bernilai 2 untuk menyimpan nilai beda antar suku.
#  3. Buatlah perintah untuk meminta masukan pengguna yang bertipe data integer dan simpan pada variabel n sebagai nilai suku yang ingin diketahui.
#  4. Lakukan perulangan mulai dari 1 hingga n+1 dengan
#     4.1. state i;
#     4.2. menghitung suku ke-n berdasarkan state i dan simpan pada variabel Un; dan
#     4.3. mencetak setiap variabel Un menggunakan perintah print dan parameter end.
#  5. Lakukan pemberhentian mencetak teks dengan perintah print tanpa isi.


# SOLUSI:
# 1. Buatlah variabel a bertipe data integer yang bernilai 1 untuk menyimpan nilai suku pertama.
a: int = 1

# 2. Buatlah variabel b bertipe data integer yang bernilai 2 untuk menyimpan nilai beda antar suku.
b: int = 2

# 3. Buatlah perintah untuk meminta masukan pengguna yang bertipe data integer dan simpan pada variabel n sebagai nilai suku yang ingin diketahui.
n: int = int(input("Masukkan nilai suku yang ingin diketahui: "))

# 4. Lakukan perulangan mulai dari 1 hingga n+1 dengan
# 4.1. state i;
for i in range(1, n + 1):
    # 4.2. Menghitung suku ke-n berdasarkan state i
    Un: int = a + (i - 1) * b

    # 4.3. Mencetak setiap variabel Un menggunakan perintah print dan parameter end.
    print(Un, end=" ")

# 5. Lakukan pemberhentian mencetak teks dengan perintah print tanpa isi.
print()