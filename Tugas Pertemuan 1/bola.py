print("program menghitug luas dan volume bola")
"""
Programmer : jaelani
Pertemuan : 1
Tanggal : 22 Oktober 2023
"""
import math

# Menghitung luas permukaan bola
def luas_permukaan_bola(jari_jari):
    return 4 * math.pi * jari_jari**2

# Menghitung volume bola
def volume_bola(jari_jari):
    return (4/3) * math.pi * jari_jari**3

# Masukkan jari-jari bola
jari_jari = float(input("Masukkan jari-jari bola: "))

# Hitung dan cetak luas permukaan dan volume bola
print(f"Luas Permukaan Bola: {luas_permukaan_bola(jari_jari)}")
print(f"Volume Bola: {volume_bola(jari_jari)}")