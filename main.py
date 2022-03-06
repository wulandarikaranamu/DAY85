#soal tipe data dan variabel
#buatlah beberapa variabel yang masing2 dapat menampung nama,alamat,tanggal lahir,jenis kelamin,
#TB, dan status. kemudian berikan nilai/value setiap variabel kemudian tampilkan semua nilai variabel tersebut.

nama = "merry"
tanggal_lahir = 19
gender = "perempuan"
TB = 163
status = "singgel"

print("nama :",nama)
print("tanggal lahir :",tanggal_lahir)
print("jenis kelamin :",gender)
print("tinggi badan :",TB)
print("status :",status)

print("="*40)

#soal perbandingan,logika dan percabangan
#buatlah program menghitung pajak. Dimana syarat minimum penghasilan untuk membayar pajak adalah Rp.5000.000
#penghasilan bulanan diinput dari keyboard. (jika penghasilan minimum terpenuhi maka besaran pajak adalah 5%
#dari total penghasilan bulanan)

gaji_bulanan = int(input("masukkan gaji perbulan anda: Rp"))
pajak_penghasilan_5jt = 5/100
if gaji_bulanan >= 5000000 :
    potongan = (gaji_bulanan*pajak_penghasilan_5jt)
    penghasilan_bersih = (gaji_bulanan-potongan)
    print("total penghasilan: Rp",penghasilan_bersih)
else:
    print("tidak valid")