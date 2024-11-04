# Praktikum 4

**Latihan 1**

**Kode Python**

 ![Screenshot_1](https://github.com/user-attachments/assets/e1450d2e-b11e-4b8e-93bf-c478359b34bf)

**Input dan Output**

 ![Screenshot_4](https://github.com/user-attachments/assets/063c393f-6ef5-4c9b-8412-c63cc276abb3)

**Penjelasan :**

Impor random: Mengimpor modul random untuk menghasilkan bilangan acak.

Input pengguna: Meminta pengguna untuk memasukkan jumlah bilangan acak yang diinginkan (n).

Looping: Menggunakan while untuk terus menghasilkan bilangan acak hingga jumlah yang diinginkan tercapai. Di dalam while, jika bilangan yang dihasilkan lebih kecil dari 0.5, bilangan tersebut ditambahkan ke dalam list dan penghitung count ditambah satu.

Output: Setelah loop selesai, program menampilkan semua bilangan acak yang telah dihasilkan.
Anda dapat menjalankan kode ini di lingkungan Python apa pun untuk melihat hasilnya.


**Latihan 2**

**Kode Python**

 ![Screenshot_2](https://github.com/user-attachments/assets/496dac0c-1422-48f2-9464-8df884a78023)

**Input dan Output**

 ![Screenshot_5](https://github.com/user-attachments/assets/7a62aeb1-b951-496b-8f9f-b3156ba188f1)

**Penjelasan :**

1. Inisialisasi Modal Awal
•	Mendefinisikan variabel modal_awal yang menyimpan nilai investasi awal pengusaha, yaitu 100 juta rupiah.

2. Laba Bulan 1 dan 2
•	Pada bulan pertama dan kedua, pengusaha tidak mendapatkan laba, jadi kita menetapkan variabel laba_bulan_1_2 dengan nilai 0.

3. Laba Bulan 3
•	Pada bulan ketiga, pengusaha mulai mendapatkan laba sebesar 1% dari modal awal. Kita menghitung nilai ini dan menyimpannya dalam laba_bulan_3.

4. Laba Bulan 4
•	Bulan keempat tidak ada perubahan, jadi laba tetap sama dengan bulan ketiga.

5. Laba Bulan 5
•	Pada bulan kelima, laba meningkat menjadi 5% dari modal awal. Kita menghitung dan menyimpan nilai ini di laba_bulan_5.

6. Laba Bulan 6 dan 7
•	Bulan keenam dan ketujuh juga tidak ada perubahan, sehingga laba tetap 5% dari modal awal.

7. Laba Bulan 8
•	Pada bulan kedelapan, terjadi penurunan laba menjadi 3% dari modal awal, sehingga kita menghitung dan menyimpan nilai ini di laba_bulan_8.

8. Menghitung Total Laba
•	Di sini, kita menghitung total laba selama 8 bulan dengan menjumlahkan laba dari setiap bulan. Untuk bulan pertama dan kedua, kita kalikan laba_bulan_1_2 dengan 2 (karena kedua bulan tersebut tidak mendapatkan laba).

9. Menampilkan Total Laba
•	Terakhir, kita mencetak total laba yang dihitung ke layar.

 
**Latihan 3**

**Kode Python**

 ![Screenshot_3](https://github.com/user-attachments/assets/c4a53fde-604f-4925-bc71-22f052ace05c)

**Input dan Output**

 ![Screenshot_6](https://github.com/user-attachments/assets/225e900a-d3d9-4730-a772-ee89b423912e)

**Penjelasan :**

Kelas ATM

Kelas ATM merupakan inti dari program ini. Kelas ini berfungsi untuk mengelola saldo pengguna dan menyediakan fungsi untuk interaksi dengan pengguna. Mari kita bahas setiap metode dalam kelas ini:

1.	Metode __init__
o	Fungsi ini adalah konstruktor kelas yang dipanggil saat objek dari kelas ATM dibuat.
o	Dalam fungsi ini, saldo awal diinisialisasi sebesar Rp 1.000.000.

2.	Metode tampilkan_saldo
o	Metode ini bertanggung jawab untuk menampilkan saldo pengguna saat ini.
o	Ketika metode ini dipanggil, ia mencetak saldo ke layar.

3.	Metode tarik_uang
o	Metode ini digunakan untuk menarik uang dari saldo pengguna.
o	Ia menerima satu parameter jumlah, yang merupakan jumlah uang yang ingin ditarik.
o	Metode ini melakukan beberapa pemeriksaan:
	Memastikan jumlah yang diminta lebih besar dari 0.
	Memastikan saldo cukup untuk menarik jumlah yang diminta.
o	Jika kedua kondisi tersebut terpenuhi, saldo akan dikurangi dengan jumlah yang ditarik, dan saldo baru akan ditampilkan.

4.	Metode menu
o	Metode ini menjalankan loop yang terus menampilkan menu hingga pengguna memilih untuk keluar.
o	Pengguna dapat memilih antara tiga opsi:
	Tampilkan Saldo: Memanggil metode tampilkan_saldo.
	Tarik Uang: Meminta pengguna untuk memasukkan jumlah yang ingin ditarik dan memanggil metode tarik_uang.
	Keluar: Menghentikan loop dan menampilkan pesan perpisahan.
o	Jika pengguna memasukkan pilihan yang tidak valid, program akan meminta pengguna untuk mencoba lagi.

Penggunaan Objek
•	Di bagian bawah program, objek dari kelas ATM dibuat dan fungsi menu dijalankan untuk memulai interaksi dengan pengguna.
•	Ini akan memanggil metode menu, yang akan terus menampilkan opsi hingga pengguna memilih untuk keluar.

