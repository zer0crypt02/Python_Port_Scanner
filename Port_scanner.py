import socket

def port_scanner(target_ip):
    print(f"Tarama Başladı: {target_ip}")
    
    # Açık portları tutacak liste
    open_ports = []

    # İlk 1000 portu taramak için
    for port in range(1, 1001):  # 1'den 1000'e kadar
        # Socket oluştur
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Bağlantı zaman aşımı süresi
        result = s.connect_ex((target_ip, port))  # Bağlantı denemesi
        
        if result == 0:
            # Eğer port açıksa, open_ports listesine ekle
            open_ports.append(port)
        
        s.close()

    # Sonuçları daha düzenli bir şekilde yazdır
    if open_ports:
        print(f"\nAçık Portlar (Port No - Durum):")
        print("=" * 40)
        print(f"{'Port No':<10}{'Durum'}")
        print("=" * 40)
        for port in open_ports:
            print(f"{port:<10}{'Açık'}")
        print("=" * 40)
    else:
        print(f"Hiç açık port bulunamadı.")

# Hedef IP (Buraya taramak istediğiniz IP'yi yazabilirsiniz)
target_ip = input("Taranacak IP Adresini Yazın: ")

port_scanner(target_ip)
