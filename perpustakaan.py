# PROGRAM DAFTAR BUKU PERPUSTAKAAN

print("="*24)
print(" Data Buku Perpustakaan")
print("="*24)

daftarBuku = []
while True:
    namaBuku = input("Masukkan Nama Buku\t\t= ")
    namaPenulis = input("Masukkan Nama Penulis\t\t= ")
    tahun = int(input("Masukkan Tahun Terbit\t\t= "))
    print("="*24)

    bukuBaru = [namaBuku,namaPenulis,tahun]
    daftarBuku.append(bukuBaru)
    print(" Daftar Buku")
    for i,buku in enumerate(daftarBuku):
        print(f"No. {i} | {buku[0]} | {buku[1]} | {buku[2]}")
    print("="*24)

    tanya = input("Apakah lanjut program?(y/n)")
    if(tanya=="y"):
        pass
    elif(tanya=="n"):
        break
    else:
        print("Inputan salah, ulangi")

print("Program Selesai, Terimakasih")   
print("="*24)

# program ini bagian dari latihanku dari youtube Kelas Terbuka
    