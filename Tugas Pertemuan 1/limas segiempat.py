print("program menghitug luas dan volume limas segiempat")
"""
Programmer : jaelani
Pertemuan : 1
Tanggal : 22 Oktober 2023
"""
# Input panjang alas, lebar alas, dan tinggi limas
panjang_alas = float(input("Masukkan panjang alas segiempat: "))
lebar_alas = float(input("Masukkan lebar alas segiempat: "))
tinggi_limas = float(input("Masukkan tinggi limas: "))

# Menghitung luas alas
luas_alas = panjang_alas * lebar_alas

# Menghitung volume limas
volume_limas = (1/3) * luas_alas * tinggi_limas

# Menampilkan hasil
print("Luas Alas segiempat:", luas_alas)
print("Volume Limas segiempat:", volume_limas)