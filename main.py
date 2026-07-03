import os
from modules.port_scanner import scan_ports
from modules.hash_generator import generate_hash
from modules.base64_tool import base64_tool
from modules.http_header_analyzer import analyze_headers
from modules.dns_lookup import dns_lookup

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_banner():
    print("=" * 55)
    print("          CYBER SECURITY TOOLKIT v1.0")
    print("=" * 55)
    print("Yalnızca izinli sistemlerde ve eğitim ortamlarında kullanın.\n")


def show_menu():
    print("[1] Port Scanner")
    print("[2] Hash Generator")
    print("[3] Base64 Encoder / Decoder")
    print("[4] HTTP Header Analyzer")
    print("[5] DNS Lookup")
    print("[0] Çıkış")


def main():
    while True:
        clear_screen()
        show_banner()
        show_menu()

        choice = input("\nBir işlem seçin: ").strip()

        if choice == "1":
            scan_ports()
        elif choice == "2":
            generate_hash()
        elif choice == "3":
            base64_tool()
        elif choice == "4":
            analyze_headers()
        elif choice == "5":
            dns_lookup()
        elif choice == "0":
            print("\nCyber Security Toolkit kapatılıyor...")
            break
        else:
            print("\nGeçersiz seçim. 0 ile 5 arasında bir değer girin.")

        input("\nAna menüye dönmek için Enter'a basın...")


if __name__ == "__main__":
    main()