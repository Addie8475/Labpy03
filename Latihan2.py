modal_awal = 100000000
laba_bulanan = []
total_laba = 0

for bulan in range(1, 9):
    laba = 0
    
    if bulan <= 2:  # Bulan 1-2: belum ada laba
        laba = 0
    elif bulan <= 4:  # Bulan 3-4: laba 1%
        laba = modal_awal * 0.01
    elif bulan <= 7:  # Bulan 5-7: laba 5%
        laba = modal_awal * 0.05
    else:  # Bulan 8: laba 2%
        laba = modal_awal * 0.02
    
    laba_bulanan.append(laba)
    total_laba += laba

# Menampilkan laba per bulan
for bulan, laba in enumerate(laba_bulanan, 1):
    print(f"laba bulan ke- {bulan} sebesar: {laba}")

# Menampilkan total laba
print(f"Total laba adalah: {total_laba}")