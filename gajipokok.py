gaji_pokok = float(input("masukan gaji pokok karyawan :"))
uang_transport_harian = float(input("masukan uang transport harian :"))
uang_makan_harian = float(input("masukan uang makan harian :"))
tunjangan_jabatan = float(input("masukan tunjangan jabatan :"))
honor_lembur = float(input("masukan honor lembur :"))

total_gaji =gaji_pokok + uang_transport_harian + uang_makan_harian + tunjangan_jabatan + honor_lembur
print ("total_gaji :%.0f" %total_gaji)