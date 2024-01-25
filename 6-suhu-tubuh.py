# Kuis Coding: Pemeriksaan Suhu Tubuh
# January 26, 2024

# SOAL
# Suatu hari, Bima ke sekolah dalam kondisi yang tidak fit. Ternyata, dia mengalami demam. 
# Bima tidak tahu harus ke dokter atau tetap melanjutkan sekolahnya. 
# Saat jam istirahat, Bima mencoba pergi ke UKS (usaha kesehatan sekolah) untuk memastikan 
# bahwa dia bisa melanjutkan belajar atau tidak. Bima diperiksa oleh perawat dengan mengukur suhu tubuhnya.
# Saat perawat memeriksa suhu tubuh, Bima dipastikan mengalami demam tinggi dan tidak bisa melanjutkan belajar di hari itu. 
# Bima bertanya ke perawat, “Berapa derajat suhu tubuh saya?” Perawat pun menjelaskan dengan detail beberapa kategori demam 
# berdasarkan suhu tubuh yang telah dipelajari melalui riset. Berikut adalah pernyataan perawat kepada Bima.
# Saat ini, suhu tubuh Bima adalah 38,4 derajat celsius. Ini masuk kategori demam. 
# Seseorang dikatakan demam apabila suhu tubuh mencapai 38ºC ke atas. 
# Selain itu, suhu tubuh rendah juga dapat berakibat fatal. 
# Seseorang akan terjangkit hipotermia dengan keadaan suhu tubuh 35ºC ke bawah.
# Berdasarkan jawaban perawat, sebaiknya Bima mengetahui hal tersebut sebelum berangkat ke sekolah. 
# Dia perlu memeriksa suhu tubuhnya dan menentukan dia sakit atau tidak.
# Bantulah Bima untuk membuatkan program yang fleksibel digunakan oleh siapa pun dalam menentukan 
# seseorang sedang sakit atau tidak berdasarkan suhu badan. Dengan begitu, setiap orang dapat lebih waspada 
# akan kondisinya sebelum beraktivitas seharian.

# TODO:
#  1. Buatlah variabel isSick bertipe data boolean yang bernilai False untuk menyimpan status sakit.
#  2. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel temperature.
#  3. Ada pengecekan variabel temperature sesuai dengan kebutuhan.
#     3.1. Jika temperature 38 ke atas akan mencetak teks "Anda mengalami sakit demam." dan ubahlah status isSick menjadi True.
#     3.2. Jika temperature di antara 35 dan 38 akan mencetak teks "Suhu tubuh Anda normal."
#     3.3. Jika temperature kurang dari atau sama dengan 35 akan mencetak teks "Anda terjangkit sakit hipotermia." dan ubahlah status isSick menjadi True.
#  4. Ada pemberian saran apabila sedang mengalami sakit.
#     4.1. Gunakan variabel isSick untuk memeriksa sedang sakit atau tidak.
#     4.2. Jika mengalami sakit, program akan mencetak teks "Anda disarankan istirahat atau kunjungi dokter secepatnya."

# SOLUSI:
# 1. Buatlah variabel isSick bertipe data boolean yang bernilai False untuk menyimpan status sakit.
isSick: bool = False

# 2. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel temperature.
temperature: float = float(input("Masukkan suhu tubuh Anda: "))

# 3. Ada pengecekan variabel temperature sesuai dengan kebutuhan.
# 3.1. Jika temperature 38 ke atas akan mencetak teks "Anda mengalami sakit demam." dan ubahlah status isSick menjadi True.
if temperature >= 38:
    print("Anda mengalami sakit demam.")
    isSick = True
# 3.2. Jika temperature di antara 35 dan 38 akan mencetak teks "Suhu tubuh Anda normal."
elif 35 < temperature < 38:
    print("Suhu tubuh Anda normal.")
# 3.3. Jika temperature kurang dari atau sama dengan 35 akan mencetak teks "Anda terjangkit sakit hipotermia." dan ubahlah status isSick menjadi True.
else:
    print("Anda terjangkit sakit hipotermia.")
    isSick = True

# 4. Ada pemberian saran apabila sedang mengalami sakit.
# 4.1. Gunakan variabel isSick untuk memeriksa sedang sakit atau tidak.
# 4.2. Jika mengalami sakit, program akan mencetak teks "Anda disarankan istirahat atau kunjungi dokter secepatnya."
if isSick:
    print("Anda disarankan istirahat atau kunjungi dokter secepatnya.")