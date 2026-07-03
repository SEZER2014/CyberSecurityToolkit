import hashlib


def generate_hash():
    print("\n" + "=" * 55)
    print("HASH GENERATOR")
    print("=" * 55)

    text = input("\nHash oluşturulacak metni girin: ")

    encoded_text = text.encode("utf-8")

    print("\n[1] MD5")
    print("[2] SHA-1")
    print("[3] SHA-256")
    print("[4] SHA-512")
    print("[5] Tümünü oluştur")

    choice = input("\nHash türünü seçin: ").strip()

    hash_types = {
        "1": ("MD5", hashlib.md5),
        "2": ("SHA-1", hashlib.sha1),
        "3": ("SHA-256", hashlib.sha256),
        "4": ("SHA-512", hashlib.sha512),
    }

    print("\n" + "-" * 55)

    if choice in hash_types:
        name, algorithm = hash_types[choice]
        result = algorithm(encoded_text).hexdigest()

        print(f"{name}:")
        print(result)

    elif choice == "5":
        for name, algorithm in hash_types.values():
            result = algorithm(encoded_text).hexdigest()
            print(f"{name}:")
            print(result)
            print()

    else:
        print("Geçersiz hash türü seçildi.")

    print("-" * 55)