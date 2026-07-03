import socket


def dns_lookup():
    print("\n" + "=" * 55)
    print("DNS LOOKUP")
    print("=" * 55)

    domain = input("\nAlan adı girin: ").strip()

    domain = (
        domain
        .replace("https://", "")
        .replace("http://", "")
        .split("/")[0]
    )

    if not domain:
        print("\nAlan adı boş bırakılamaz.")
        return

    try:
        hostname, aliases, ip_addresses = socket.gethostbyname_ex(domain)

        print("\n" + "-" * 55)
        print(f"Alan adı       : {domain}")
        print(f"Resmî hostname : {hostname}")

        if aliases:
            print("\nAlias kayıtları:")
            for alias in aliases:
                print(f"- {alias}")
        else:
            print("\nAlias kaydı bulunamadı.")

        print("\nIP adresleri:")
        for ip_address in sorted(set(ip_addresses)):
            print(f"- {ip_address}")

        print("\nTers DNS kontrolleri:")

        for ip_address in sorted(set(ip_addresses)):
            try:
                reverse_host, reverse_aliases, _ = socket.gethostbyaddr(
                    ip_address
                )
                print(f"- {ip_address} -> {reverse_host}")

                for alias in reverse_aliases:
                    print(f"  Alias: {alias}")

            except socket.herror:
                print(f"- {ip_address} -> Ters DNS kaydı bulunamadı.")

    except socket.gaierror:
        print("\nAlan adı çözümlenemedi.")

    except Exception as error:
        print(f"\nBeklenmeyen hata: {error}")

    print("\n" + "-" * 55)