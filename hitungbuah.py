jumlah_jeruk = float (input("masukan_jumlah_kg_jeruk"))
jumlah_apel = float (input("masukan_jumlah_kg_apel"))
jumlah_mangga = float (input("masukan_jumlah_kg_mangga"))
jumlah_manggis = float (input("masukan_jumlah_kg_manggis"))
jumlah_durian = float (input("masukan_jumlah_kg_durian"))

jeruk = 15000
apel = 30000
mangga = 20000
manggis = 7000
durian = 50000


harga_total = (jeruk*jumlah_jeruk)+(apel*jumlah_apel)+(mangga*jumlah_mangga)+(manggis*jumlah_manggis)+(durian*jumlah_durian)
print (f"jumlah keseluruhan belanja : {harga_total:1,.2f} rupiah ")


