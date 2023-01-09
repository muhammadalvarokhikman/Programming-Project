# Project Tugas Algoritma dan Pemrograman
# S1 Teknik Telekomunikasi, Institut Teknologi Telkom Purwokerto
# Program perhitungan jumlah kolesterol berdasarkan jenis makanan
# Program Index Masa Tubuh

# import package                                    
import os

# fungsi-fungsi
def hitung_imt(berat, tinggi):
  imt = berat / ((tinggi/100) ** 2)
  return imt

def rekomendasi(imt):
  if imt < 18.5:
    print("Anda kekurangan berat badan. Direkomendasikan untuk\nmenambah asupan makanan bergizi dan melakukan olahraga ringan seperti jogging atau yoga.")
  elif imt >= 18.5 and imt < 25:
    print("Berat badan Anda ideal. Direkomendasikan untuk terus\nmenjaga pola makan sehat dan melakukan olahraga secara teratur.")
  elif imt >= 25 and imt < 30:
    print("Anda kelebihan berat badan. Direkomendasikan untuk\nmengurangi asupan makanan berlemak dan meningkatkan olahraga, seperti bersepeda atau berenang.")
  else:
    print("Anda obesitas. Direkomendasikan untuk segera mengubah\npola makan dan melakukan olahraga yang intens, seperti running atau latihan beban.")


makanan_cepat_saji = [
    {"nama": "Burger", "kolesterol": 80  },
    {"nama": "Hotdog", "kolesterol": 40 },
    {"nama": "Ayam goreng", "kolesterol": 60 },
    {"nama": "Nasi goreng", "kolesterol": 20 },
    {"nama": "Mie goreng", "kolesterol": 20 },
    {"nama": "nuggets", "kolesterol": 60 },
    {"nama": "Sosis", "kolesterol": 70 },
    {"nama": "Korokke", "kolesterol": 70 },
    {"nama": "Kue goreng", "kolesterol": 20 },
    {"nama": "Taco", "kolesterol": 20 },
    {"nama": "Bakso", "kolesterol": 40 },
    {"nama": "Pangsit", "kolesterol": 20 },
    {"nama": "Samosa", "kolesterol": 20 },
    {"nama": "Donat", "kolesterol": 20 },
    {"nama": "Pempek", "kolesterol": 20 },
    {"nama": "Kue keju", "kolesterol": 20 },
    {"nama": "Kue pisang", "kolesterol": 20 },
    {"nama": "Martabak", "kolesterol": 20 }
]

# Tampilan Depan
while True:
  # clear screen
  os.system("cls")
  print("="*50)
  print(f"{'SELAMAT DATANG':^50}\n{'DI APLIKASI KESEHATAN':^50}")
  print("="*50)
  print("Menu :\n\t1. Cek Jumlah Kolesterol\n\t2. Cek Index Masa Tubuh(IMT)")
  print("="*50)
  pil = int(input("Pilihan Menu(1/2) = "))

  # clear screen
  os.system("cls")
  # jika pilihan 1
  if pil == 1:
      # Table Header  
      print("|======|================|======================|")
      print("|  NO  |  NAMA MAKANAN  |   JUMLAH KOLESTEROL  |")
      print("|======|================|======================|")
      for i, makanan in enumerate(makanan_cepat_saji,start=1):
          print(f"| {i:^4} | {makanan['nama']:^14} | {makanan['kolesterol']:^20} |")
      print("|======|================|======================|\n")
      print("="*60)
      print(f"{'APLIKASI KESEHATAN':^60}")
      print("="*60)

      total_kolesterol = 0
      while True:
          nomor = int(input("Konsumsi Makanan (1-18) : "))
          jumlah_kolesterol = makanan_cepat_saji[nomor-1]["kolesterol"]
          total_kolesterol += jumlah_kolesterol
          is_done = input("Ada lagi? (y/n): ")
          if is_done == "y":
            continue
            
          if total_kolesterol >= 250:
              peringatan = "SUDAH Melebihi"
          else:
              peringatan = "TIDAK Melebihi"

          print(f"\nTotal Kolesterol = {total_kolesterol},\nJumlah kolesterol anda {peringatan} batas normal perhari")

          print("="*60)
          break

      is_done = input("Mau Coba lagi? (y/n): ")
      if is_done == "y" or is_done == "Y":
        continue
      elif is_done == "n" or is_done == "N":
        break

  # jika pilihan 2
  elif pil == 2:
    os.system("cls")
    print("="*90)
    print(f"{'APLIKASI CEK INDEX MASA TUBUH(IMT)':^90}")
    print("="*90)
    bb = int(input("Berapa Berat Badan Anda\t\t: "))
    tb = int(input("Berapa Tinggi Badan Anda\t: "))
    print()
    imt = hitung_imt(bb,tb)
    rekomendasi(imt)
    print("="*90)

    is_done = input("Mau Coba lagi? (y/n): ")
    if is_done == "y" or is_done == "Y":
      continue
    elif is_done == "n" or is_done == "N":
      break

  # jika pilihan salah
  else:
    is_done = input("Input Salah, Mau Coba lagi? (y/n): ")
    if is_done == "y" or is_done == "Y":
      continue
    elif is_done == "n" or is_done == "N":
      break