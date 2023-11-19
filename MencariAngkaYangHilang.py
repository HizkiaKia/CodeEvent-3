# Fungsi untuk mencari angka yang hilang
def cari_hilang(n, arr):
  # Menghitung jumlah semua angka dari 1 sampai n
  total = n * (n + 1) // 2
  # Mengurangi jumlah semua angka yang ada di arr
  for x in arr:
    total -= x
  # Mengembalikan selisih sebagai angka yang hilang
  return total

# Membaca input dari pengguna
n = int(input())
arr = list(map(int, input().split()))

# Memanggil fungsi dan mencetak hasilnya
hilang = cari_hilang(n, arr)
print(hilang)
