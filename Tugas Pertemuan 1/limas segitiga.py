print("program menghitug luas dan volume prisma segitiga")
"""
Programmer : jaelani
Pertemuan : 1
Tanggal : 22 Oktober 2023
"""
# Input panjang sisi segitiga alas (a), tinggi segitiga alas (h), dan tinggi limas (H)
a = float(input("Masukkan panjang sisi segitiga alas: "))
h = float(input("Masukkan tinggi segitiga alas: "))
H = float(input("Masukkan tinggi limas: "))

# Hitung luas segitiga alas (A)
A = 0.5 * a * h

# Hitung volume limas (V)
V = (1/3) * A * H

# Tampilkan hasil
print(f"Luas segitiga alas: {A}")
print(f"Volume limas: {V}")