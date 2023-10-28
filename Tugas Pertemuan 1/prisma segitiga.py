print("program menghitug luas dan volume prisma segitiga")
"""
Programmer : jaelani
Pertemuan : 1
Tanggal : 22 Oktober 2023
"""
# Input panjang alas segitiga
panjang_alas = float(input("Masukkan panjang alas segitiga: "))

# Input tinggi segitiga
tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))

# Input tinggi prisma
tinggi_prisma = float(input("Masukkan tinggi prisma: "))

# Menghitung luas segitiga
luas_segitiga = 0.5 * panjang_alas * tinggi_segitiga

# Menghitung luas permukaan prisma
luas_permukaan_prisma = 2 * (luas_segitiga + panjang_alas * tinggi_prisma)

# Menghitung volume prisma
volume_prisma = luas_segitiga * tinggi_prisma

# Menampilkan hasil
print(f"Luas segitiga: {luas_segitiga}")
print(f"Luas permukaan prisma: {luas_permukaan_prisma}")
print(f"Volume prisma: {volume_prisma}")