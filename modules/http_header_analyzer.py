import urllib.error
import urllib.request


SECURITY_HEADERS = {
    "Content-Security-Policy": "XSS ve içerik enjeksiyonlarına karşı koruma",
    "Strict-Transport-Security": "HTTPS kullanımını zorunlu hâle getirir",
    "X-Content-Type-Options": "MIME type sniffing saldırılarını azaltır",
    "X-Frame-Options": "Clickjacking saldırılarına karşı koruma",
    "Referrer-Policy": "Referrer bilgisinin paylaşımını sınırlar",
    "Permissions-Policy": "Tarayıcı özelliklerine erişimi sınırlar",
}


def analyze_headers():
    print("\n" + "=" * 55)
    print("HTTP HEADER ANALYZER")
    print("=" * 55)
    print("Yalnızca izinli sistemlerde kullanın.\n")

    url = input("Analiz edilecek URL: ").strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "CyberSecurityToolkit/1.0"
        }
    )

    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            headers = response.headers

            print("\n" + "-" * 55)
            print(f"İstenen URL : {url}")
            print(f"Son URL     : {response.geturl()}")
            print(f"HTTP Durumu : {response.status}")
            print("-" * 55)

            print("\nTÜM HTTP BAŞLIKLARI\n")

            for header, value in headers.items():
                print(f"{header}: {value}")

            print("\n" + "-" * 55)
            print("GÜVENLİK BAŞLIKLARI ANALİZİ")
            print("-" * 55)

            found_count = 0

            for header, description in SECURITY_HEADERS.items():
                if headers.get(header):
                    found_count += 1
                    print(f"[VAR]  {header}")
                    print(f"       {headers.get(header)}")
                else:
                    print(f"[YOK]  {header}")
                    print(f"       {description}")

            print("\n" + "-" * 55)
            print(
                f"Bulunan güvenlik başlığı: "
                f"{found_count}/{len(SECURITY_HEADERS)}"
            )

            if headers.get("Server"):
                print(f"Server bilgisi: {headers.get('Server')}")

            if headers.get("X-Powered-By"):
                print(f"X-Powered-By: {headers.get('X-Powered-By')}")

    except urllib.error.HTTPError as error:
        print(f"\nHTTP hatası: {error.code} - {error.reason}")

    except urllib.error.URLError as error:
        print(f"\nBağlantı hatası: {error.reason}")

    except TimeoutError:
        print("\nBağlantı zaman aşımına uğradı.")

    except Exception as error:
        print(f"\nBeklenmeyen hata: {error}")

    print("\n" + "-" * 55)