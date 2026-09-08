print("Sistem kasir minimarket")
list_barang = []
total = 0 

print("silahkan memasukan barang belanjaan anda")

while True:
    barang = input("silahkan ketik nama barang: ")

    harga = int(input("masukan harga barang: "))
    total += harga
    list_barang.append([barang, harga])

    selesai = input("ingin menambahkan barang lagi? (ya/selesai): ").lower()
    if selesai == "selesai":
        break
    elif selesai == "ya":
        continue

membership = input("apakah anda memiliki membership? (ya/tidak): ").lower()

diskon = 0
if total >= 100000:
    diskon = total * 0.10
    if membership == "ya":
        diskon = diskon + (total * 0.15)
elif membership == "ya":
    diskon = total * 0.15        
else:
    diskon = 0

bayar = total - diskon

print("-Struk Belanja-")

for i in list_barang:
    print(i[0], "- Rp", i[1])

print("---------")
print("total belanja : Rp", total)
print("diskon : Rp", int(diskon))
print("total bayar : Rp", int(bayar))               