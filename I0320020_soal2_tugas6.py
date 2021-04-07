#Program perhitungan rata-rata
print("---------------SELAMAT DATANG---------------", "\n")
print("Selamat menghitung nilai rata-rata dengan cikalku")
banyak_nilai = int(input(" Silahkan input banyak nilai yang akan diolah = "))
nilai = []
total = 0

#Perhitungan nilai
for i in range(banyak_nilai):
    angka = int(input("Silahkan input nilai ke = "))
    nilai.append(angka)
    total = int(total + angka)

rata_nilai = total/banyak_nilai
print("jumlah nilai = ", total, "\n", "Maka nilai rata-rata adalah ", rata_nilai)
