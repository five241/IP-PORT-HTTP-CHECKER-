python_banner = '''
8888888 8888888b.        .d8888b.           888    
  888   888   Y88b      d88P  Y88b          888    
  888   888    888      888    888          888    
  888   888   d88P      888         .d88b.  888888 
  888   8888888P"       888  88888 d8P  Y8b 888    
  888   888             888    888 88888888 888    
  888   888             Y88b  d88P Y8b.     Y88b.  
8888888 888              "Y8888P88  "Y8888   "Y888 
        
        BY 7UM4D1007
        Tiktok:@7um4d1007
        Telegram:@jumadi007
'''

# Menampilkan banner Python
print(python_banner)
import socket
from colorama import Fore, Style, init

init(autoreset=True)

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
with open("target.txt", "w") as f:
    for ip in ips:
        f.write(ip + "\n")

# Tampilkan pesan pemberitahuan
print("Daftar IP berhasil disimpan di target.txt")
