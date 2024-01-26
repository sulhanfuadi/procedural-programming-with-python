# Kuis Coding: Total Harga
# January 25, 2024

# SOAL
# Saat di kantin sekolah, Bima ingin membelikan teman-temannya jajanan. 
# Sebab satu kelas berjumlah 30 anak, Bima memilih jajanan ringan, seperti chocolate bar. 
# Dia langsung menuju ke penjual camilan dan berkata, “Coklat ini harganya berapa, bu?” 
# Dibalas oleh sang pemilik kedai, “Harga satuannya 3500 rupiah.” 
# Bima segera bertanya, “Saya mau beli ini sebanyak 30, total harganya berapa, ya?” 
# Sang penjual kebingungan karena mendapatkan pesanan banyak dan tidak tahu total yang harus dibayar oleh Bima. 
# Berdasarkan cerita di atas, kita bisa membantu penjual dalam menyelesaikan permasalahan perhitungan total harga. 
# Buatkan program yang fleksibel digunakan oleh penjual dalam menghitung 
# total harga chocolate bar dengan bantuan harga, input, output, dan ekspresi.

# TODO:
#  1. Buatlah variabel chocolateBarPrice bertipe data integer yang bernilai 3500.
#  2. Tambahkan perintah untuk meminta masukan pengguna yang bertipe data integer dan simpan pada variabel chocolateBarCount.
#  3. Gunakan ekspresi yang tepat untuk menghitung total harga snack dan simpan pada variabel chocolateBarTotalPrice bertipe data integer.
#  4. Tampilkan hasil perhitungan pada console dengan teks "Harga yang harus dibayar adalah {chocolateBarTotalPrice} rupiah."

# SOLUSI:
# 1. Buat variabel chocolateBarPrice bertipe data integer yang bernilai 3500
chocolateBarPrice: int = 3500
# 2. Tambahkan perintah untuk meminta masukan pengguna yang bertipe data integer dan simpan pada variabel chocolateBarCount
chocolateBarCount: int = int(input("Masukkan jumlah chocolate yang terbeli: "))
# 3. Gunakan ekspresi yang tepat untuk menghitung total harga snack dan simpan pada variabel chocolateBarTotalPrice bertipe data integer
chocolateBarTotalPrice: int = chocolateBarPrice * chocolateBarCount
# 4. Tampilkan hasil perhitungan pada console dengan teks "Harga yang harus dibayar adalah {chocolateBarTotalPrice} rupiah."
print(f"Harga yang harus dibayar adalah {chocolateBarTotalPrice} rupiah.")