python_banner = '''
_______   ____  ___  _________  __  
|___  / | | |  \/  | /   |  _  \/  | 
   / /| | | | .  . |/ /| | | | |`| | 
  / / | | | | |\/| / /_| | | | | | | 
./ /  | |_| | |  | \___  | |/ / _| |_
\_/    \___/\_|  |_/   |_/___/  \___/
                                     
'''

# Menampilkan banner Python
print(python_banner)
import socket
from colorama import Fore, Style, init

init(autoreset=True)

def check_ip(ip, port, output_file):
    try:
        socket.setdefaulttimeout(0.5)  # Ubah timeout menjadi 0.5 detik
        sock = socket.create_connection((ip, port))
        result = f"IP {ip} on port {port} is {Fore.GREEN}[VULN]{Style.RESET_ALL}"
        print(result)
        with open(output_file, "a") as out_file:
            out_file.write(result + "\n")
        sock.close()
    except (socket.timeout, socket.error):
        result = f"IP {ip} on port {port} is {Fore.RED}[NOT VULN]{Style.RESET_ALL}"
        print(result)

def main():
    filename = "list_ip.txt"
    output_file = "hasil.txt"
    port = 80

    try:
        with open(filename, "r") as file:
            ip_list = file.read().splitlines()
            for ip in ip_list:
                check_ip(ip, port, output_file)
    except FileNotFoundError:
        print(f"File {filename} not found")

if __name__ == "__main__":
    main()

