print ("PERHITUNGAN PAJAK SEDERHANA")

print ("masukkan kelas kendaraan")
print ("1.motor 2.mobil 3.minibus 4.truk")
kelas= input ('kelas: ')

if kelas== '1':
    print ("Pajak Motor Rp. 230.000")
elif kelas== '2':
    print ("Pajak Mobil Rp. 620.000")
elif kelas== '3':
    print ("Pajak Minibus Rp. 890.000")
elif kelas== '4':
    print ("Pajak Truk Rp. 1.200.000")
else:
    print ("Tidak Valid")