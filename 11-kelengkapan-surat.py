# Kuis Coding: Kelengkapan Surat
# January 26, 2024


# SOAL
# Sebelum memulai pembangunan, pemilik rumah perlu menyiapkan beberapa surat untuk memenuhi persyaratan hukum dan administrasi. 
# Hal ini ditujukan untuk kelegalan dalam mendirikan suatu bangunan. Surat-surat tersebut meliputi Izin Mendirikan Bangunan (IMB), 
# Pembebasan Lahan, Perjanjian Kontrak, Izin Lingkungan, dan Izin Penggunaan Bangunan (IPM). 
# Berkas yang dimiliki oleh pemilik rumah harus lengkap supaya dapat membangun rumah di lahan yang ia inginkan. 
# Keseluruhan berkas akan diserahkan ke pihak yang berwenang di kota untuk diperiksa kelengkapannya. 
# Mereka membutuhkan sistem untuk memeriksa kelengkapan berkas dan kota tempat lokasi bangunan berada agar pemilik rumah 
# segera melangsungkan proses pembangunan rumah.
# Buatkan program yang fleksibel digunakan oleh siapa pun dalam proses pemeriksaan kelengkapan berkas dan 
# mencatat kota tempat lokasi bangunan. 


# TODO:
#  1. Buatlah perintah untuk meminta masukan pengguna yang bertipe data integer dan simpan pada variabel permission.
#      1.1. Beri informasi bahwa masukan hanya boleh mengizinkan nilai 1 untuk True atau 0 untuk False.
#  2. Buatlah perintah untuk meminta masukan pengguna yang bertipe data string dan simpan pada variabel city.
#  3. Buatlah prosedur bernama checkPermission yang memiliki parameter permission dan city.
#      3.1. Gunakan pengondisian untuk memeriksa permission.
#           3.1.1. Apabila bernilai False, cetak teks "Anda tidak bisa membangun rumah di kota {city} karena berkas belum lengkap."
#           3.1.2. Apabila bernilai True, cetak teks "Anda dapat membangun rumah di kota {city}."
#      3.2. Jalankan prosedur untuk memeriksa berkas

# SOLUSI:
#  1. Buatlah perintah untuk meminta masukan pengguna yang bertipe data integer dan simpan pada variabel permission.
#   1.1. Beri informasi bahwa masukan hanya boleh mengizinkan nilai 1 untuk True atau 0 untuk False.
permission: int = int(input("Masukkan izin (0 untuk False, 1 untuk True): "))

#  2. Buatlah perintah untuk meminta masukan pengguna yang bertipe data string dan simpan pada variabel city.
city: str = input("Masukkan nama kota: ")

#  3. Buatlah prosedur bernama checkPermission yang memiliki parameter permission dan city.
def checkPermission(permission: int, city: str) -> None:
#   3.1. Gunakan pengondisian untuk memeriksa permission.
#       3.1.1. Apabila bernilai False, cetak teks "Anda tidak bisa membangun rumah di kota {city} karena berkas belum lengkap."
#       3.1.2. Apabila bernilai True, cetak teks "Anda dapat membangun rumah di kota {city}."
    if permission == 0:
        print(f"Anda tidak bisa membangun rumah di kota {city} karena berkas belum lengkap.")
    elif permission == 1:
        print(f"Anda dapat membangun rumah di kota {city}.")
#   3.2. Jalankan prosedur untuk memeriksa berkas
checkPermission(permission, city)