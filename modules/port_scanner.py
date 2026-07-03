import socket
from datetime import datetime


def scan_ports():
    print("\n" + "=" * 55)
    print("PORT SCANNER")
    print("=" * 55)
    print("Yalnızca izinli sistemlerde kullanın.\n")

    target = input("Hedef IP veya alan adı: ").strip()

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("\nHedef adres çözümlenemedi.")
        return

    try:
        start_port = int(input("Başlangıç portu: "))
        end_port = int(input("Bitiş portu: "))
    except ValueError:
        print("\nPort değerleri sayı olmalıdır.")
        return

    if not 1 <= start_port <= 65535 or not 1 <= end_port <= 65535:
        print("\nPortlar 1-65535 arasında olmalıdır.")
        return

    if start_port > end_port:
        print("\nBaşlangıç portu bitiş portundan büyük olamaz.")
        return

    if end_port - start_port > 1000:
        print("\nGüvenlik amacıyla tek taramada en fazla 1000 port seçilebilir.")
        return

    print(f"\nHedef       : {target}")
    print(f"IP Adresi   : {target_ip}")
    print(f"Port Aralığı: {start_port}-{end_port}")
    print(f"Başlangıç   : {datetime.now().strftime('%H:%M:%S')}")
    print("-" * 55)

    open_ports = []

    for port in range(start_port, end_port + 1):
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(0.3)

        try:
            result = scanner.connect_ex((target_ip, port))

            if result == 0:
                try:
                    service = socket.getservbyport(port, "tcp")
                except OSError:
                    service = "Bilinmeyen servis"

                open_ports.append((port, service))
                print(f"[AÇIK] Port {port:<5} | {service}")

        except (socket.timeout, OSError):
            pass
        finally:
            scanner.close()

    print("-" * 55)

    if open_ports:
        print(f"Toplam {len(open_ports)} açık port bulundu.")
    else:
        print("Açık port bulunamadı.")

    print(f"Bitiş: {datetime.now().strftime('%H:%M:%S')}")