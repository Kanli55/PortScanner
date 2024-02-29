import socket
import os
os.system("pkg install figlet")
os.system("clear")
os.system("figlet Port Scanner")
print('______________#Yazar KanlıSilah__________')
print('Sitenin ip adresine göre port taraması yapar.')
class PortScanThread:
    def __init__(self, target_ip, start_port, end_port):
        super().__init__()
        self.target_ip = target_ip
        self.start_port = start_port
        self.end_port = end_port

    def run(self):
        for port in range(self.start_port, self.end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.target_ip, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                    print(f"Port {port} is open. Used protocol: {service}")
                except socket.error:
                    print(f"Port {port} is open, but the used protocol couldn't be determined.")
            sock.close()

# Kullanıcıdan hedef IP adresini alalım
target_ip = input("Hedef IP adresini giriniz: ")

# Port tarama aralığını belirleyelim
start_port = int(input("Başlangıç portunu giriniz: "))
end_port = int(input("Bitiş portunu giriniz: "))

# Port tarama işlemini başlatalım
scanner = PortScanThread(target_ip, start_port, end_port)
scanner.run()
