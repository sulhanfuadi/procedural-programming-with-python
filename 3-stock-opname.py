# Kuis Coding: Stock Opname
# January 25, 2024

# SOAL
# Sang pemilik kedai camilan di kantin sekolah memiliki berbagai jajanan ringan dengan beragam jenis. 
# Mulai dari wafer, biskuit, kue, kacang, hingga chocolate bar tersedia di kedai tersebut. 
# Pemilik kedai menyediakan 50 buah untuk setiap camilan yang dia miliki supaya tidak kehabisan stok.
# Saat jam istirahat sekolah, Bima datang ke kantin dan membeli chocolate bar sebanyak 10 buah. 
# Supaya tidak bingung, pemilik kedai mencatat seluruh pengeluaran dan pemasukan barang 
# saat transaksi jual beli berlangsung.
# Bantulah pemilik kedai untuk mencatat pemasukan atau pengeluaran barang chocolate bar 
# saat terjadi transaksi jual beli.

# TODO:
#  1. Buatlah variabel chocolateBarStock bertipe data integer yang bernilai 50.
#  2. Tambahkan perintah untuk meminta masukan pengguna yang bertipe data integer dan simpan pada variabel chocolateBarCount.
#  3. Gunakan ekspresi yang tepat untuk menghitung total stok camilan dan simpan pada newChocolateBarStock bertipe data integer.
#  4. Tampilkan hasil stok baru pada console dengan teks "Stok saat ini adalah {newChocolateBarStock} buah."

# SOLUSI:
# 1. Buat variabel chocolateBarStock bertipe data integer yang bernilai 50
chocolateBarStock: int = 50
# 2. Tambahkan perintah untuk meminta masukan pengguna yang bertipe data integer dan simpan pada variabel chocolateBarCount
chocolateBarCount: int = int(input("Masukkan jumlah chocolate yang terjual: "))
# 3. Gunakan ekspresi yang tepat untuk menghitung total stok camilan dan simpan pada newChocolateBarStock bertipe data integer
newChocolateBarStock: int = chocolateBarStock - chocolateBarCount
# 4. Tampilkan hasil stok baru pada console dengan teks "Stok saat ini adalah {newChocolateBarStock} buah."
print(f"Stok saat ini adalah {newChocolateBarStock} buah.")