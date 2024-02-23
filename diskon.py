total_uang_belanja = float(input("masukan total uang belanja anda: "))
total_belanja = float(input("masukan total belanja anda: "))

if total_belanja > 70000 :
    diskon = 0.1 * total_belanja
    total_belanja_setelah_diskon = total_belanja - diskon
    Kembalian = total_uang_belanja - total_belanja_setelah_diskon
    
    print("uang kembalian anda : %.2f" %Kembalian)