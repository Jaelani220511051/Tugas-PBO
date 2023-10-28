print("program menghitug luas dan volume kubus")
"""
Programmer : jaelani
Pertemuan : 1
Tanggal : 22 Oktober 2023
"""
# Menghitung luas permukaan kubus
def hitung_luas_permukaan(sisi):
    luas_permukaan = 6 * sisi ** 2
    return luas_permukaan

# Menghitung volume kubus
def hitung_volume(sisi):
    volume = sisi ** 3
    return volume

# Input sisi kubus dari pengguna
sisi = float(input("Masukkan panjang sisi kubus: "))

# Menghitung dan mencetak luas permukaan
luas = hitung_luas_permukaan(sisi)
print(f"Luas permukaan kubus dengan sisi {sisi} adalah {luas}")

# Menghitung dan mencetak volume
volume = hitung_volume(sisi)
print(f"Volume kubus dengan sisi {sisi} adalah {volume}")