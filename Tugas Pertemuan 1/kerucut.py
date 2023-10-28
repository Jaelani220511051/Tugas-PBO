print("program menghitug luas dan volume kerucut")
"""
Programmer : jaelani
Pertemuan : 1
Tanggal : 22 Oktober 2023
"""
import math

# Input jari-jari dan tinggi kerucut dari pengguna
r = float(input("Masukkan jari-jari kerucut: "))
h = float(input("Masukkan tinggi kerucut: "))

# Hitung luas permukaan kerucut
luas_permukaan = math.pi * r * (r + math.sqrt(r**2 + h**2))

# Hitung volume kerucut
volume = (1/3) * math.pi * r**2 * h

# Tampilkan hasil
print(f"Luas Permukaan Kerucut: {luas_permukaan:.2f}")
print(f"Volume Kerucut: {volume:.2f}")