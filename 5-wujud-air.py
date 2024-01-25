# Kuis Coding: Menentukan Wujud Air
# January 26, 2024

# SOAL
# Setiap akhir pekan, Bima bekerja sebagai guru les mengajari anak SMP atau SD. 
# Pada saat itu, Bima mendapati anak SMP yang sedang belajar IPA (ilmu pengetahuan alam). 
# Dia bertanya kepada Bima terkait perubahan zat padat, cair, dan gas. Berikut pertanyaannya.
#  - Berapa derajat titik didih dan titik beku air?
#  - Apakah suhu air 120 derajat celsius dapat mengubahnya menjadi gas?
#  - Apakah suhu air -15,5 derajat celsius dapat mengubahnya menjadi padat?
# Bima pun menjelaskan dengan lengkap pengertian dari titik didih dan titik beku. 
# Titik didih adalah kondisi air yang mendidih dan berubah bentuk menjadi gas ketika suhu air 
# melebihi 100 derajat celsius, sedangkan titik beku adalah kondisi air yang berubah bentuk 
# menjadi padat ketika suhunya kurang dari 0 derajat celsius. 
# Pertanyaan pertama dari anak didik Bima sudah terjawab.
# Untuk pertanyaan kedua dan ketiga, Anda bisa membantu Bima dengan membuat program 
# yang fleksibel berfungsi untuk menentukan zat berubah menjadi gas atau padat melalui masukan suhu air.

# TODO:
#  1. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel temperature.
#  2. Ada pengecekan variabel temperature sesuai dengan kebutuhan.
#     2.1. Jika temperature lebih dari 100 akan mencetak teks "Air berubah menjadi gas."
#     2.2. Jika temperature di antara 0 dan 100 akan mencetak teks "Air tetap berupa cairan."
#     2.3. Jika temperature kurang dari 0 akan mencetak teks "Air berubah menjadi padat."

# SOLUSI:
# 1. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel temperature.
temperature: float = float(input("Masukkan suhu air: "))
# 2. Ada pengecekan variabel temperature sesuai dengan kebutuhan.
# 2.1. Jika temperature lebih dari 100 akan mencetak teks "Air berubah menjadi gas."
if temperature > 100:
    print("Air berubah menjadi gas.")
# 2.2. Jika temperature di antara 0 dan 100 akan mencetak teks "Air tetap berupa cairan."
elif 0 <= temperature <= 100:
    print("Air tetap berupa cairan.")
# 2.3. Jika temperature kurang dari 0 akan mencetak teks "Air berubah menjadi padat."
else:
    print("Air berubah menjadi padat.")