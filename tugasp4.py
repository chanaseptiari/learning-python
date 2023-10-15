print("============Program Hitung Gaji Karyawan=========")
print("")
nama=input(f"Nama Karyawan\t=")
golongan=int(input("Golongan Jabatan [1/2/3] ="))
pendidikan=input("Pendidikan [SMA/D1/D3/S1] =").lower()
jam=int(input("Jumlah Jam Kerja  ="))

if golongan==1:
    jabatan=300000*0.05
    if pendidikan=="sma":
        tunjangan=300000*0.025
    elif pendidikan=="d1":
         tunjangan="300000*0.05"
    elif pendidikan=="d3":
        tunjangan=300000*0.20
    elif pendidikan=="s1":
        tunjangan=300000*0.30
    else:
        print("Harap Isi Pendidikan dengan benar")
elif golongan==2:
    jabatan=300000*0.10
    if pendidikan=="sma":
        tunjangan=300000*0.025
    elif pendidikan=="d1":
         tunjangan="300000*0.05"
    elif pendidikan=="d3":
        tunjangan=300000*0.20
    elif pendidikan=="s1":
        tunjangan=300000*0.30
    else:
        print("Harap Isi Pendidikan dengan benar")
elif golongan==3:
    jabatan=300000*0.15
    if pendidikan=="sma":
        tunjangan=300000*0.025
    elif pendidikan=="d1":
         tunjangan="300000*0.05"
    elif pendidikan=="d3":
        tunjangan=300000*0.20
    elif pendidikan=="s1":
        tunjangan=300000*0.30
    else:
        print("Harap Isi Pendidikan dengan benar")
else:
    print("Harap Isi Golongan dengan benar")

if jam>=8:
    lembur=(jam-8)*3500
    
total_gaji=300000+jabatan+tunjangan+lembur

print("")
print("Karyawan Yang Bersama =",nama)
print("Honor Yang Diterima")
print(" Tunjangan Jabatan    :Rp. ",jabatan)
print(" Tunjangan Pendidikan :Rp. ",tunjangan)
print(" Honor Lembur         :Rp. ",lembur)
print("------------------------------------  ")
print("TOTAL GAJI             Rp. %s"%(total_gaji))
