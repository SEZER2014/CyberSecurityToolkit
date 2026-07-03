import base64
import binascii


def base64_tool():
    print("\n" + "=" * 55)
    print("BASE64 ENCODER / DECODER")
    print("=" * 55)

    print("\n[1] Metni Base64 olarak kodla")
    print("[2] Base64 verisini çöz")

    choice = input("\nİşlem seçin: ").strip()

    if choice == "1":
        text = input("\nKodlanacak metni girin: ")
        encoded = base64.b64encode(text.encode("utf-8")).decode("utf-8")

        print("\nBase64 sonucu:")
        print(encoded)

    elif choice == "2":
        encoded_text = input("\nÇözülecek Base64 verisini girin: ").strip()

        try:
            decoded = base64.b64decode(
                encoded_text,
                validate=True
            ).decode("utf-8")

            print("\nÇözülen metin:")
            print(decoded)

        except (binascii.Error, UnicodeDecodeError):
            print("\nGeçersiz veya desteklenmeyen Base64 verisi.")

    else:
        print("\nGeçersiz seçim.")

    print("\n" + "-" * 55)