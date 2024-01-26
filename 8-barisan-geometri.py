# Kuis Coding: Perhitungan Barisan Geometri
# January 26, 2024

# SOAL
# Suatu saat Bima mendapati guru sedang mengajar matematika, khususnya tentang barisan geometri. 
# Bima duduk di barisan paling depan karena merasa sangat antusias. 
# Dia mencatat segala materi yang diberikan oleh guru dan mulai melihat pola dalam angka-angka tersebut. 
# Ketika sang guru jeda sejenak dari menjelaskan pelajaran, Bima mengajukan pertanyaan, 
# “Apa bedanya barisan aritmatika dengan barisan geometri” Sang guru pun menjelaskannya kembali 
# dengan penjelasan yang mudah dimengerti. Berikut adalah penjelasan sang guru.
# Barisan geometri adalah barisan bilangan dengan pola perbandingan atau rasio tetap antar sukunya.
# Contoh barisan geometri adalah 3, 6, 12, 24, …, dst.
# Berdasarkan contoh di atas,
#     angka 3 adalah suku pertama atau disebut U1;
#     angka 6 adalah suku kedua atau disebut U2;
#     angka 12 adalah suku ketiga atau disebut U3; dst.
# Antar suku memiliki beda rasio bernilai 2 karena U2 / U1 = U3 / U2 = Un / Un-1 = 2.
# Menentukan suku ke-n dapat dihitung melalui persamaan Un = a * r(n-1)dan
#     a adalah suku pertama atau U1;
#     n adalah jumlah suku yang ingin dicari; 
#     r adalah rasio antar suku; serta
#     Un adalah suku ke n.
# Apabila ditanya nilai suku ke-5 dari contoh barisan geometri di atas, cara menghitungnya sebagai berikut.
#     Nilai a = 3, r = 2, dan n = 5.
#     Nilai U20 = 3 * 2(5-1) atau setara dengan 48.
# Di akhir kelas, guru memberikan soal yang cukup menyulitkan kepada seluruh siswa kelas, 
# yaitu membuat barisan geometri. Bilangan ini meliputi angka 4, 12, 36, 108, …, dst. Soalnya adalah 
# tentukan suku ke-8 dengan mencetak seluruh suku dari 1 hingga terakhir.
# Bantulah Bima untuk membuat program yang fleksibel digunakan oleh siapa pun dalam 
# menjabarkan dan menghitung suku pada barisan geometri. Dengan begitu, setiap orang dapat mengetahui 
# suku barisan geometri mulai awal hingga akhir.


# TODO:
#  1. Buatlah variabel a bertipe data integer yang bernilai 4 untuk menyimpan nilai suku pertama.
#  2. Buatlah variabel r bertipe data integer yang bernilai 3 untuk menyimpan nilai rasio antar suku.
#  3. Buatlah perintah untuk meminta masukan pengguna yang bertipe data integer dan simpan pada variabel n sebagai nilai suku yang ingin diketahui.
#  4. Lakukan perulangan mulai dari 1 hingga n+1 dengan
#     4.1. state i;
#     4.2. menghitung suku ke-n berdasarkan state i dan simpan pada variabel Un; dan
#     4.3. mencetak setiap variabel Un menggunakan perintah print dan parameter end.
#  5. Lakukan pemberhentian mencetak teks dengan perintah print tanpa isi.

# SOLUSI:
# 1. Buatlah variabel a bertipe data integer yang bernilai 4 untuk menyimpan nilai suku pertama.
a: int = 4

# 2. Buatlah variabel r bertipe data integer yang bernilai 3 untuk menyimpan nilai rasio antar suku.
r: int = 3

# 3. Buatlah perintah untuk meminta masukan pengguna yang bertipe data integer dan simpan pada variabel n sebagai nilai suku yang ingin diketahui.
n: int = int(input("Masukkan nilai suku yang ingin diketahui: "))

# 4. Lakukan perulangan mulai dari 1 hingga n+1 dengan
# 4.1. state i;
for i in range(1, n + 1):
    # 4.2. Menghitung suku ke-n berdasarkan state i
    Un: int = a * r ** (i - 1)

    # 4.3. Mencetak setiap variabel Un menggunakan perintah print dan parameter end.
    print(Un, end=" ")

# 5. Lakukan pemberhentian mencetak teks dengan perintah print tanpa isi.
print()