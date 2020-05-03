Nama = str("Lukman Irawan")
NIM = str("1911600094")
Prodi = str("Magister Ilmu Komputer")
Fakultas = str("Teknologi Informasi")
Univ = str("Budi Luhur")
Tahun = str("2020")

print("\n**********************************")
print("Tugas 9_DATA SCIENCE_PYTHON BASIC")
print("**********************************")
print("Nama         : ", Nama)
print("NIM          : ", NIM)
print("\nProdi        : ", Prodi)
print("Fakultas     : ", Fakultas)
print("Universitas  : ", Univ)
print("Tahun        : ", Tahun)
print("**********************************")

#Bagian Input Nilai
print("\n===================")
print("    Input Nilai ")
print("===================")
Tugas = input("Tugas       : ")
UTS = input("UTS         : ")
UAS = input("UAS         : ")
print("===================")

#Pengaturan Bobot Penilaian (Input Dalam Decimal)
BobotTugas = 0.30
BobotUTS = 0.30
BobotUAS = 0.40

#Bagian Perhitungan
Total = int(Tugas)+int(UTS)+int(UAS)
BobotTotal = (int(Total)*BobotTugas)+(int(Total)*BobotUTS)+(int(Total)*BobotUAS)
Akhir = float(int(BobotTotal)/3)

#Bagian kondisi Grade dan Bobot Nilai
if Akhir >= 90:
    grade = "A"
    bobot = "4,00"
elif Akhir >= 85:
    grade = "A-"
    bobot = "3,70"
elif Akhir >= 80:
    grade = "B+"
    bobot = "3,30"
elif Akhir >= 75:
    grade = "B"
    bobot = "2,70"
elif Akhir >= 70:
    grade = "B-"
    bobot = "2,30"
elif Akhir >= 65:
    grade = "C+"
    bobot = "2,00"
elif Akhir >= 60:
    grade = "C-"
    bobot = "1,70"
elif Akhir >= 50:
    grade = "D"
    bobot = "1,00"
elif Akhir >= 40:
    grade = "E"
    bobot = "0,00"
elif Akhir < 40:
    grade = "T"
    bobot = "Tunda"
else :
    print("Maaf anda Gagal!")

print("\n===================")
print("       Hasil")
print("===================")
print("Tugas       : ", Tugas)
print("UTS         : ", UTS)
print("UAS         : ", UAS)
print("Akhir       : ", round(Akhir, 1))
print("Grade       : ", grade)
print("Bobot Nilai : ", bobot)
print("===================")

print("\n**********************************")
print("    SELESAI!, TERIMA KASIH!")
print("**********************************")
