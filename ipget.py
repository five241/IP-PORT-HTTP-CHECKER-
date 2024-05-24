import random

# Batas bawah dan atas rentang IP
batas_bawah = 1
batas_atas = 500

# Inisialisasi daftar IP kosong
ips = []

# Loop untuk menghasilkan IP
for i in range(batas_bawah, batas_atas + 1):
    # Generate IP address
    ip = f"192.168.200.{i}"

    # Periksa apakah IP sudah ada dalam daftar
    if ip not in ips:
        # Tambahkan IP ke daftar
        ips.append(ip)

# Tulis daftar IP ke file
with open("hasil.txt", "w") as f:
    for ip in ips:
        f.write(ip + "\n")

# Tampilkan pesan pemberitahuan
print("Daftar IP berhasil disimpan di hasil.txt")
