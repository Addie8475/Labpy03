class ATM:
    def __init__(self):
        self.saldo = 1000000  # Saldo awal

    def tampilkan_saldo(self):
        print(f"Saldo Anda saat ini: Rp {self.saldo}")

    def tarik_uang(self, jumlah):
        if jumlah <= 0:
            print("Jumlah tarik uang harus lebih besar dari 0.")
        elif jumlah > self.saldo:
            print("Saldo Anda tidak cukup untuk menarik uang tersebut.")
        else:
            self.saldo -= jumlah
            print(f"Anda berhasil menarik uang sebesar: Rp {jumlah}")
            self.tampilkan_saldo()

    def menu(self):
        while True:
            print("\n--- Menu ATM ---")
            print("1. Tampilkan Saldo")
            print("2. Tarik Uang")
            print("3. Keluar")
            pilihan = input("Pilih opsi (1/2/3): ")

            if pilihan == '1':
                self.tampilkan_saldo()
            elif pilihan == '2':
                jumlah = int(input("Masukkan jumlah uang yang ingin ditarik: Rp "))
                self.tarik_uang(jumlah)
            elif pilihan == '3':
                print("Terima kasih! Selamat tinggal.")
                break
            else:
                print("Pilihan tidak valid, silakan coba lagi.")

# Membuat objek ATM dan menjalankan menu
atm = ATM()
atm.menu()
