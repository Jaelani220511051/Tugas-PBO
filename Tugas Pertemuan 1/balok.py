print("program menghitug luas dan volume balok")
"""
Programmer : jaelani
Pertemuan : 1
Tanggal : 22 Oktober 2023
"""
# Input panjang, lebar, dan tinggi balok dari pengguna
panjang = float(input("Masukkan panjang balok: "))
lebar = float(input("Masukkan lebar balok: "))
tinggi = float(input("Masukkan tinggi balok: "))

# Hitung luas permukaan balok
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

# Hitung volume balok
volume = panjang * lebar * tinggi

# Tampilkan hasil
print(f"Luas permukaan balok: {luas_permukaan}")
print(f"Volume balok: {volume}")