# Kuis Coding: Perhitungan Faktorial Rekursif
# January 26, 2024


# SOAL
# Saat Bima sedang belajar matematika, dia menemukan materi faktorial. 
# Bima mempelajarinya dengan tekun sehingga dia mendapatkan beberapa fakta tentang faktorial. 
# Berikut adalah fakta terkait materi faktorial.
# Faktorial adalah hasil perkalian dari semua bilangan bulat positif dari 1 hingga bilangan tertentu.
# Faktorial dilambangkan dengan tanda seru “!” setelah bilangan tertentu. 
# Contohnya 5 faktorial dapat ditulis menjadi 5!.
# Berdasarkan pengertiannya, faktorial dapat dihitung dengan rumus berikut.
# n! = 1 x 2 x … x (n-2) x (n-1) x n
# Berdasarkan sifat komutatif (pertukaran), perhitungan faktorial dapat ditulis menjadi seperti berikut.
# n! = n x (n-1) x (n-2) x … x 2 x 1
# Perhitungan 5 faktorial dapat dihitung dengan rumus di atas.
# 5! = 5 x 4 x 3 x 2 x 1 = 120
# Faktorial hanya berlaku untuk bilangan bulat positif. 
# Jadi, bilangan bulat negatif tidak dapat dihitung nilai faktorialnya.
# Khusus bilangan 0 faktorial bernilai 1.
# Setelah dipelajari lebih dalam, Bima menyadari bahwa proses perhitungan faktorial dilakukan secara berulang, 
# tidak serta-merta dihitung secara keseluruhan dengan mengalikan angka 1 hingga nilai yang diinginkan. 
# Ada proses perkalian dua angka yang nantinya akan dikalikan dengan angka berikutnya. 
# Pada akhir perkalian tersebut didapatkan hasil akhir faktorial yang diinginkan.
# Sayangnya, Bima akan kesulitan untuk menghitung nilai faktorial dengan bilangan yang besar. 
# Perkalian dengan angka besar secara manual membuat waktu perhitungan semakin lama. 
# Bahkan, bisa saja dia kurang teliti yang mengakibatkan salah perhitungan.
# Bantulah Bima untuk membuat program faktorial yang fleksibel digunakan oleh siapa pun. 
# Dengan begitu, setiap orang dapat mengetahui nilai faktorial berdasarkan nilai yang diinginkan.


# TODO:
#  1. Buatlah perintah untuk meminta masukan pengguna yang bertipe data integer dan simpan pada variabel n.
#  2. Buatlah fungsi rekursif bernama hitung_faktorial yang memiliki parameter n untuk mendapatkan hasil akhir perhitungan faktorial.
#     2.1. Gunakan jenis linear, direct, dan tail recursion untuk membuat fungsi rekursif.
#     2.2. Terapkan konsep decrement atau pengurangan satu demi satu setiap memanggil fungsi rekursif.
#     2.3. Jika nilai n bernilai 0, hentikan proses rekursif dengan mengembalikan nilai 1.
#     2.4. Selain itu, kembalikan nilai n dikali dengan fungsi rekursif dengan nilai decrement n.
#     2.5. Simpan hasil fungsi pada variabel hasil_hitung_faktorial.
#  3. Cetak pada akhir program dengan format "{n}! = {hasil_hitung_faktorial}".


# SOLUSI:
#  1. Buatlah perintah untuk meminta masukan pengguna yang bertipe data integer dan simpan pada variabel n.
n: int = int(input("Masukkan angka untuk menghitung faktorial: "))

#  2. Buatlah fungsi rekursif bernama hitung_faktorial yang memiliki parameter n untuk mendapatkan hasil akhir perhitungan faktorial.
def hitung_faktorial(n: int) -> int:
#   2.1. Gunakan jenis linear, direct, dan tail recursion untuk membuat fungsi rekursif.
#   2.2. Terapkan konsep decrement atau pengurangan satu demi satu setiap memanggil fungsi rekursif.
#   2.3. Jika nilai n bernilai 0, hentikan proses rekursif dengan mengembalikan nilai 1.
    if n == 0:
        return 1
#   2.4. Selain itu, kembalikan nilai n dikali dengan fungsi rekursif dengan nilai decrement n.
    else:
        return n * hitung_faktorial(n - 1)

#   2.5. Simpan hasil fungsi pada variabel hasil_hitung_faktorial.
hasil_hitung_faktorial: int = hitung_faktorial(n)

#  3. Cetak pada akhir program dengan format "{n}! = {hasil_hitung_faktorial}".
print(f"{n}! = {hasil_hitung_faktorial}.")