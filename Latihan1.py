import random

# Meminta input dari pengguna untuk jumlah bilangan acak
n = int(input("Masukkan jumlah bilangan acak yang ingin ditampilkan: "))

count = 0  # Inisialisasi penghitung
random_numbers = []  # List untuk menyimpan bilangan acak

# Menggunakan while untuk terus menghasilkan bilangan sampai mencapai n
while count < n:
    # Menghasilkan bilangan acak antara 0 dan 1
    num = random.random()
    
    # Jika bilangan acak lebih kecil dari 0.5, simpan dan increment count
    if num < 0.5:
        random_numbers.append(num)
        count += 1

# Menampilkan hasil
print("Bilangan acak yang lebih kecil dari 0.5:")
for number in random_numbers:
    print(number)
