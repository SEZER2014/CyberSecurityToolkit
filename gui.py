import customtkinter as ctk
import hashlib
import base64
import binascii
import socket
import threading
import urllib.error
import urllib.request
import platform
import os
import subprocess

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class CyberSecurityToolkitGUI(ctk.CTk):
    BG = "#F8FAFC"
    PANEL = "#FFFFFF"
    SIDEBAR = "#FFFFFF"
    BORDER = "#DCE3EC"
    TEXT = "#0F172A"
    MUTED = "#475569"
    BLUE = "#0B4DBB"
    BLUE_HOVER = "#0A43A2"
    GREEN = "#16A34A"
    RED = "#DC2626"

    def __init__(self):
        super().__init__()

        self.title("Cyber Security Toolkit")
        self.geometry("1000x650")
        self.minsize(900, 600)
        self.configure(fg_color=self.BG)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.menu_buttons = {}
        self.create_sidebar()
        self.create_main_panel()

    def create_sidebar(self):
        self.sidebar = ctk.CTkFrame(
            self, width=300, corner_radius=0,
            fg_color=self.SIDEBAR,
            border_width=1, border_color=self.BORDER
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)

        brand = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        brand.pack(fill="x", padx=28, pady=(32, 22))

        logo = ctk.CTkLabel(
            brand,
            text="🛡",
            width=54,
            height=64,
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=38,
                weight="bold"
            ),
            text_color=self.BLUE
        )

        logo.grid(row=0, column=0, rowspan=2, padx=(0, 14))

        title = ctk.CTkLabel(
            brand, text="CYBER SECURITY\nTOOLKIT",
            font=ctk.CTkFont(family="Segoe UI", size=22, weight="bold"),
            text_color="#111111", justify="left"
        )
        title.grid(row=0, column=1, sticky="w")

        version = ctk.CTkLabel(
            brand, text="v1.0.0",
            font=ctk.CTkFont(family="Consolas", size=13, weight="bold"),
            text_color=self.BLUE
        )
        version.grid(row=1, column=1, sticky="w", pady=(5, 0))

        self.create_menu_button("dashboard", "⌂   Dashboard", self.show_dashboard)
        self.create_menu_button("port", "⌕   Port Scanner", self.show_port_scanner)
        self.create_menu_button("hash", "#   Hash Generator", self.show_hash_generator)
        self.create_menu_button("base64", "</>  Base64 Tool", self.show_base64)
        self.create_menu_button("http", "▤   HTTP Headers", self.show_http_headers)
        self.create_menu_button("dns", "◎   DNS Lookup", self.show_dns_lookup)

        warning = ctk.CTkLabel(
            self.sidebar, text="AUTHORIZED USE ONLY",
            font=ctk.CTkFont(family="Consolas", size=12, weight="bold"),
            text_color=self.RED
        )
        warning.pack(side="bottom", padx=20, pady=35)

    def create_menu_button(self, key, text, command):
        button = ctk.CTkButton(
            self.sidebar, text=text,
            command=lambda: self.open_page(key, command),
            height=54, corner_radius=8, anchor="w",
            font=ctk.CTkFont(family="Segoe UI", size=16),
            fg_color="transparent", hover_color="#EAF1FB",
            text_color=self.TEXT, border_width=0
        )
        button.pack(fill="x", padx=24, pady=4)
        self.menu_buttons[key] = button

    def open_page(self, key, command):
        self.set_active_menu(key)
        command()

    def set_active_menu(self, active_key):
        for key, button in self.menu_buttons.items():
            if key == active_key:
                button.configure(
                    fg_color=self.BLUE, hover_color=self.BLUE_HOVER,
                    text_color="#FFFFFF"
                )
            else:
                button.configure(
                    fg_color="transparent", hover_color="#EAF1FB",
                    text_color=self.TEXT
                )

    def create_main_panel(self):
        self.main_panel = ctk.CTkFrame(self, corner_radius=0, fg_color=self.BG)
        self.main_panel.grid(row=0, column=1, sticky="nsew")
        self.main_panel.grid_columnconfigure(0, weight=1)
        self.main_panel.grid_rowconfigure(1, weight=1)

        self.header = ctk.CTkFrame(
            self.main_panel, height=82, corner_radius=0, fg_color=self.PANEL
        )
        self.header.grid(row=0, column=0, sticky="ew")
        self.header.grid_propagate(False)

        self.page_title = ctk.CTkLabel(
            self.header, text="Dashboard",
            font=ctk.CTkFont(family="Segoe UI", size=30, weight="bold"),
            text_color="#111111"
        )
        self.page_title.pack(side="left", padx=38, pady=20)

        status = ctk.CTkLabel(
            self.header, text="●  SYSTEM ONLINE",
            font=ctk.CTkFont(family="Consolas", size=13, weight="bold"),
            text_color=self.GREEN
        )
        status.pack(side="right", padx=38)

        self.content = ctk.CTkFrame(
            self.main_panel, corner_radius=0, fg_color=self.BG
        )
        self.content.grid(row=1, column=0, padx=38, pady=(20, 34), sticky="nsew")

        self.show_dashboard()

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def make_card(self, parent, title):
        card = ctk.CTkFrame(
            parent, fg_color=self.PANEL, corner_radius=12,
            border_width=1, border_color=self.BORDER
        )
        heading = ctk.CTkLabel(
            card, text=title,
            font=ctk.CTkFont(family="Segoe UI", size=17, weight="bold"),
            text_color=self.BLUE
        )
        heading.pack(anchor="w", padx=24, pady=(20, 14))
        return card

    def show_dashboard(self):
        self.set_active_menu("dashboard")
        self.clear_content()
        self.page_title.configure(text="Dashboard")

        self.content.grid_columnconfigure(0, weight=4)
        self.content.grid_columnconfigure(1, weight=2)
        self.content.grid_rowconfigure(1, weight=1)

        intro = ctk.CTkLabel(
            self.content,
            text="Cyber Security Toolkit kontrol merkezine hoş geldiniz.",
            font=ctk.CTkFont(family="Segoe UI", size=16),
            text_color=self.MUTED
        )
        intro.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 24))

        terminal = ctk.CTkTextbox(
            self.content, corner_radius=10,
            fg_color=self.PANEL, border_width=1, border_color=self.BORDER,
            text_color=self.BLUE,
            font=ctk.CTkFont(family="Consolas", size=15),
            wrap="word"
        )
        terminal.grid(row=1, column=0, sticky="nsew", padx=(0, 24))
        terminal.insert(
            "1.0",
            "[+]  Modül hazır.\n\n"
            "[+]  Grafik arayüz bağlantısı oluşturuldu.\n\n"
            "[+]  Fonksiyonlar kullanıma hazır."
        )
        terminal.configure(state="disabled")

        right = ctk.CTkFrame(self.content, fg_color="transparent")
        right.grid(row=1, column=1, sticky="nsew")
        right.grid_columnconfigure(0, weight=1)

        system_card = self.make_card(right, "SİSTEM BİLGİLERİ")
        system_card.grid(row=0, column=0, sticky="ew", pady=(0, 18))

        rows = [
            ("◉", "Durum", "Online", self.GREEN),
            ("⚙", "Sürüm", "1.0.0", self.TEXT),
            ("♙", "Kullanıcı", "User", self.TEXT),
            ("▣", "Platform", platform.system(), self.TEXT),
        ]
        for icon, label, value, color in rows:
            row = ctk.CTkFrame(system_card, fg_color="transparent")
            row.pack(fill="x", padx=24, pady=8)
            ctk.CTkLabel(row, text=icon, width=28, text_color=self.MUTED,
                         font=ctk.CTkFont(size=17)).pack(side="left")
            ctk.CTkLabel(row, text=label, text_color=self.TEXT,
                         font=ctk.CTkFont(family="Segoe UI", size=14)).pack(side="left", padx=(8, 0))
            ctk.CTkLabel(row, text=value, text_color=color,
                         font=ctk.CTkFont(family="Segoe UI", size=14)).pack(side="right")
        ctk.CTkLabel(system_card, text="").pack(pady=2)

        quick_card = self.make_card(right, "KISAYOLLAR")
        quick_card.grid(row=1, column=0, sticky="ew")

        ctk.CTkButton(
            quick_card, text="▣   Dokümantasyon", command=self.open_documentation, anchor="w", height=44,
            fg_color="#FFFFFF", hover_color="#EEF3F9", text_color=self.TEXT,
            border_width=1, border_color=self.BORDER,
            font=ctk.CTkFont(family="Segoe UI", size=14)
        ).pack(fill="x", padx=22, pady=(0, 10))

        ctk.CTkButton(
            quick_card, text="●   GitHub Repository", anchor="w", height=44,
            fg_color="#FFFFFF", hover_color="#EEF3F9", text_color=self.TEXT,
            border_width=1, border_color=self.BORDER,
            font=ctk.CTkFont(family="Segoe UI", size=14)
        ).pack(fill="x", padx=22, pady=(0, 22))

    def show_page(self, title, description):
        self.clear_content()
        self.page_title.configure(text=title)

        heading = ctk.CTkLabel(
            self.content, text=title,
            font=ctk.CTkFont(family="Segoe UI", size=30, weight="bold"),
            text_color="#111111"
        )
        heading.pack(pady=(20, 8))

        description_label = ctk.CTkLabel(
            self.content, text=description,
            font=ctk.CTkFont(family="Segoe UI", size=16),
            text_color=self.MUTED
        )
        description_label.pack(pady=(0, 20))

        info_box = ctk.CTkTextbox(
            self.content, width=650, height=260, corner_radius=10,
            fg_color=self.PANEL, border_width=1, border_color=self.BORDER,
            text_color=self.BLUE,
            font=ctk.CTkFont(family="Consolas", size=14)
        )
        info_box.pack(padx=20, pady=20, fill="both", expand=True)
        info_box.insert(
            "1.0",
            "[+] Modül hazır.\n"
            "[+] Grafik arayüz bağlantısı oluşturuldu.\n"
            "[*] Fonksiyonlar bu panel üzerinden kullanılabilir.\n"
        )
        info_box.configure(state="disabled")

    def show_port_scanner(self):
        self.set_active_menu("port")
        self.clear_content()
        self.page_title.configure(text="PORT SCANNER")

        heading = ctk.CTkLabel(
            self.content,
            text="TCP Port Scanner",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=30,
                weight="bold"
            ),
            text_color="#0B4DBB"
        )
        heading.pack(pady=(30, 8))

        description = ctk.CTkLabel(
            self.content,
            text="Yalnızca size ait veya açıkça izin verilmiş sistemlerde kullanın.",
            font=ctk.CTkFont(family="Segoe UI", size=15),
            text_color="#0B4DBB"
        )
        description.pack(pady=(0, 18))

        self.port_target = ctk.CTkEntry(
            self.content,
            width=650,
            height=45,
            placeholder_text="Hedef IP veya alan adı: 127.0.0.1",
            fg_color="#FFFFFF",
            border_color="#D7DEE8",
            text_color="#0F172A"
        )
        self.port_target.pack(padx=40, pady=8)

        port_frame = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )
        port_frame.pack(pady=8)

        self.start_port_input = ctk.CTkEntry(
            port_frame,
            width=200,
            height=42,
            placeholder_text="Başlangıç portu"
        )
        self.start_port_input.grid(row=0, column=0, padx=8)

        self.end_port_input = ctk.CTkEntry(
            port_frame,
            width=200,
            height=42,
            placeholder_text="Bitiş portu"
        )
        self.end_port_input.grid(row=0, column=1, padx=8)

        self.port_scan_button = ctk.CTkButton(
            self.content,
            text="TARAMAYI BAŞLAT",
            command=self.start_port_scan,
            width=230,
            height=44,
            fg_color="#1358C8",
            hover_color="#0B4DBB",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=14,
                weight="bold"
            )
        )
        self.port_scan_button.pack(pady=10)

        self.port_progress = ctk.CTkProgressBar(
            self.content,
            width=650,
            progress_color="#0B4DBB"
        )
        self.port_progress.pack(padx=40, pady=8)
        self.port_progress.set(0)

        self.port_status = ctk.CTkLabel(
            self.content,
            text="Tarama bekleniyor.",
            font=ctk.CTkFont(family="Consolas", size=12),
            text_color="#64748B"
        )
        self.port_status.pack(pady=(0, 5))

        self.port_result = ctk.CTkTextbox(
            self.content,
            width=650,
            height=240,
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#D7DEE8",
            text_color="#0B4DBB",
            font=ctk.CTkFont(family="Consolas", size=13)
        )
        self.port_result.pack(
            padx=40,
            pady=8,
            fill="both",
            expand=True
        )

        copy_button = ctk.CTkButton(
            self.content,
            text="SONUCU KOPYALA",
            command=self.copy_port_result,
            width=180,
            height=38,
            fg_color="#1358C8",
            hover_color="#0B4DBB"
        )
        copy_button.pack(pady=(0, 18))

    def start_port_scan(self):
        target = self.port_target.get().strip()

        try:
            start_port = int(self.start_port_input.get())
            end_port = int(self.end_port_input.get())
        except ValueError:
            self.port_result.delete("1.0", "end")
            self.port_result.insert(
                "1.0",
                "[!] Port değerleri sayı olmalıdır."
            )
            return

        if not target:
            self.port_result.delete("1.0", "end")
            self.port_result.insert(
                "1.0",
                "[!] Hedef IP veya alan adı girin."
            )
            return

        if not 1 <= start_port <= 65535 or not 1 <= end_port <= 65535:
            self.port_result.delete("1.0", "end")
            self.port_result.insert(
                "1.0",
                "[!] Portlar 1-65535 arasında olmalıdır."
            )
            return

        if start_port > end_port:
            self.port_result.delete("1.0", "end")
            self.port_result.insert(
                "1.0",
                "[!] Başlangıç portu bitiş portundan büyük olamaz."
            )
            return

        if end_port - start_port > 1000:
            self.port_result.delete("1.0", "end")
            self.port_result.insert(
                "1.0",
                "[!] Tek taramada en fazla 1000 port seçilebilir."
            )
            return

        self.port_result.delete("1.0", "end")
        self.port_progress.set(0)

        self.port_scan_button.configure(
            state="disabled",
            text="TARANIYOR..."
        )

        self.port_status.configure(
            text="Hedef çözümleniyor...",
            text_color="#D97706"
        )

        threading.Thread(
            target=self.run_port_scan,
            args=(target, start_port, end_port),
            daemon=True
        ).start()

    def run_port_scan(self, target, start_port, end_port):
        try:
            target_ip = socket.gethostbyname(target)
        except socket.gaierror:
            self.after(
                0,
                lambda: self.finish_port_scan(
                    "[!] Hedef adres çözümlenemedi.",
                    False
                )
            )
            return

        open_ports = []
        total_ports = end_port - start_port + 1

        for index, port in enumerate(
            range(start_port, end_port + 1),
            start=1
        ):
            scanner = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )
            scanner.settimeout(0.25)

            try:
                if scanner.connect_ex((target_ip, port)) == 0:
                    try:
                        service = socket.getservbyport(port, "tcp")
                    except OSError:
                        service = "Bilinmeyen servis"

                    open_ports.append((port, service))
            finally:
                scanner.close()

            progress = index / total_ports

            self.after(
                0,
                lambda value=progress: self.port_progress.set(value)
            )

            self.after(
                0,
                lambda current=port: self.port_status.configure(
                    text=f"Taranan port: {current}"
                )
            )

        result_lines = [
            "[+] Tarama tamamlandı",
            "",
            f"Hedef      : {target}",
            f"IP adresi  : {target_ip}",
            f"Port aralığı: {start_port}-{end_port}",
            "",
            "Açık portlar:"
        ]

        if open_ports:
            for port, service in open_ports:
                result_lines.append(
                    f"  [AÇIK] {port}/tcp - {service}"
                )
        else:
            result_lines.append(
                "  Açık port bulunamadı."
            )

        result_lines.extend([
            "",
            f"Toplam açık port: {len(open_ports)}"
        ])

        self.after(
            0,
            lambda: self.finish_port_scan(
                "\n".join(result_lines),
                True
            )
        )

    def finish_port_scan(self, result, success):
        self.port_result.delete("1.0", "end")
        self.port_result.insert("1.0", result)

        self.port_scan_button.configure(
            state="normal",
            text="TARAMAYI BAŞLAT"
        )

        if success:
            self.port_progress.set(1)
            self.port_status.configure(
                text="Tarama tamamlandı.",
                text_color="#22C55E"
            )
        else:
            self.port_status.configure(
                text="Tarama başarısız.",
                text_color="#0B4DBB"
            )

    def copy_port_result(self):
        result = self.port_result.get(
            "1.0",
            "end"
        ).strip()

        if result:
            self.clipboard_clear()
            self.clipboard_append(result)
            self.update()

    def show_hash_generator(self):
        self.set_active_menu("hash")
        self.clear_content()
        self.page_title.configure(text="HASH GENERATOR")

        heading = ctk.CTkLabel(
            self.content,
            text="Hash Generator",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=30,
                weight="bold"
            ),
            text_color="#0B4DBB"
        )
        heading.pack(pady=(35, 8))

        description = ctk.CTkLabel(
            self.content,
            text="Metinlerden MD5, SHA-1, SHA-256 ve SHA-512 hash değerleri oluşturun.",
            font=ctk.CTkFont(family="Segoe UI", size=15),
            text_color="#475569"
        )
        description.pack(pady=(0, 20))

        self.hash_input = ctk.CTkEntry(
            self.content,
            width=650,
            height=45,
            placeholder_text="Hash oluşturulacak metni girin...",
            corner_radius=8,
            fg_color="#FFFFFF",
            border_color="#D7DEE8",
            text_color="#0F172A"
        )
        self.hash_input.pack(padx=40, pady=10)

        self.hash_algorithm = ctk.CTkOptionMenu(
            self.content,
            values=["MD5", "SHA-1", "SHA-256", "SHA-512"],
            width=220,
            height=40,
            fg_color="#1358C8",
            button_color="#0B4DBB",
            button_hover_color="#0B4DBB"
        )
        self.hash_algorithm.set("SHA-256")
        self.hash_algorithm.pack(pady=10)

        generate_button = ctk.CTkButton(
            self.content,
            text="HASH OLUŞTUR",
            command=self.generate_hash_gui,
            width=220,
            height=44,
            corner_radius=8,
            fg_color="#1358C8",
            hover_color="#0B4DBB"
        )
        generate_button.pack(pady=12)

        self.hash_result = ctk.CTkTextbox(
            self.content,
            width=650,
            height=180,
            corner_radius=10,
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#D7DEE8",
            text_color="#0B4DBB",
            font=ctk.CTkFont(family="Consolas", size=14),
            wrap="word"
        )
        self.hash_result.pack(
            padx=40,
            pady=15,
            fill="both",
            expand=True
        )

        copy_button = ctk.CTkButton(
            self.content,
            text="SONUCU KOPYALA",
            command=self.copy_hash_result,
            width=180,
            height=38,
            fg_color="#1358C8",
            hover_color="#0B4DBB"
        )
        copy_button.pack(pady=(0, 25))

    def generate_hash_gui(self):
        text = self.hash_input.get()
        algorithm = self.hash_algorithm.get()

        self.hash_result.delete("1.0", "end")

        if not text:
            self.hash_result.insert(
                "1.0",
                "[!] Lütfen hash oluşturulacak bir metin girin."
            )
            return

        algorithms = {
            "MD5": hashlib.md5,
            "SHA-1": hashlib.sha1,
            "SHA-256": hashlib.sha256,
            "SHA-512": hashlib.sha512,
        }

        result = algorithms[algorithm](
            text.encode("utf-8")
        ).hexdigest()

        self.hash_result.insert(
            "1.0",
            f"Algoritma : {algorithm}\n"
            f"Girdi     : {text}\n\n"
            f"Hash:\n{result}"
        )

    def copy_hash_result(self):
        result = self.hash_result.get("1.0", "end").strip()

        if result:
            self.clipboard_clear()
            self.clipboard_append(result)
            self.update()

    def show_base64(self):
        self.set_active_menu("base64")
        self.clear_content()
        self.page_title.configure(text="BASE64 TOOL")

        heading = ctk.CTkLabel(
            self.content,
            text="Base64 Encoder / Decoder",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=30,
                weight="bold"
            ),
            text_color="#0B4DBB"
        )
        heading.pack(pady=(30, 8))

        description = ctk.CTkLabel(
            self.content,
            text="Metinleri Base64 formatına kodlayın veya Base64 verilerini çözün.",
            font=ctk.CTkFont(family="Segoe UI", size=15),
            text_color="#475569"
        )
        description.pack(pady=(0, 15))

        self.base64_input = ctk.CTkTextbox(
            self.content,
            width=650,
            height=130,
            corner_radius=10,
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#D7DEE8",
            text_color="#0F172A",
            font=ctk.CTkFont(family="Consolas", size=14),
            wrap="word"
        )
        self.base64_input.pack(
            padx=40,
            pady=10,
            fill="x"
        )
        self.base64_input.insert(
            "1.0",
            "Kodlanacak metni veya çözülecek Base64 verisini girin..."
        )

        button_frame = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )
        button_frame.pack(pady=10)

        encode_button = ctk.CTkButton(
            button_frame,
            text="BASE64 KODLA",
            command=self.encode_base64_gui,
            width=190,
            height=44,
            fg_color="#1358C8",
            hover_color="#0B4DBB"
        )
        encode_button.grid(row=0, column=0, padx=8)

        decode_button = ctk.CTkButton(
            button_frame,
            text="BASE64 ÇÖZ",
            command=self.decode_base64_gui,
            width=190,
            height=44,
            fg_color="#1358C8",
            hover_color="#0B4DBB"
        )
        decode_button.grid(row=0, column=1, padx=8)

        self.base64_result = ctk.CTkTextbox(
            self.content,
            width=650,
            height=180,
            corner_radius=10,
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#D7DEE8",
            text_color="#0B4DBB",
            font=ctk.CTkFont(family="Consolas", size=14),
            wrap="word"
        )
        self.base64_result.pack(
            padx=40,
            pady=12,
            fill="both",
            expand=True
        )

        copy_button = ctk.CTkButton(
            self.content,
            text="SONUCU KOPYALA",
            command=self.copy_base64_result,
            width=180,
            height=38,
            fg_color="#1358C8",
            hover_color="#0B4DBB"
        )
        copy_button.pack(pady=(0, 20))

    def get_base64_input(self):
        text = self.base64_input.get("1.0", "end").strip()

        placeholder = (
            "Kodlanacak metni veya çözülecek "
            "Base64 verisini girin..."
        )

        if text == placeholder:
            return ""

        return text

    def encode_base64_gui(self):
        text = self.get_base64_input()
        self.base64_result.delete("1.0", "end")

        if not text:
            self.base64_result.insert(
                "1.0",
                "[!] Lütfen kodlanacak bir metin girin."
            )
            return

        encoded = base64.b64encode(
            text.encode("utf-8")
        ).decode("utf-8")

        self.base64_result.insert(
            "1.0",
            f"İşlem : Base64 Encode\n"
            f"Girdi : {text}\n\n"
            f"Sonuç:\n{encoded}"
        )

    def decode_base64_gui(self):
        encoded_text = self.get_base64_input()
        self.base64_result.delete("1.0", "end")

        if not encoded_text:
            self.base64_result.insert(
                "1.0",
                "[!] Lütfen çözülecek Base64 verisini girin."
            )
            return

        try:
            decoded = base64.b64decode(
                encoded_text,
                validate=True
            ).decode("utf-8")

            self.base64_result.insert(
                "1.0",
                f"İşlem : Base64 Decode\n"
                f"Girdi : {encoded_text}\n\n"
                f"Çözülen metin:\n{decoded}"
            )

        except (binascii.Error, UnicodeDecodeError):
            self.base64_result.insert(
                "1.0",
                "[!] Geçersiz veya desteklenmeyen Base64 verisi."
            )

    def copy_base64_result(self):
        result = self.base64_result.get(
            "1.0",
            "end"
        ).strip()

        if result:
            self.clipboard_clear()
            self.clipboard_append(result)
            self.update()

    def show_http_headers(self):
        self.set_active_menu("http")
        self.clear_content()
        self.page_title.configure(text="HTTP HEADER ANALYZER")

        heading = ctk.CTkLabel(
            self.content,
            text="HTTP Header Analyzer",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=30,
                weight="bold"
            ),
            text_color="#0B4DBB"
        )
        heading.pack(pady=(30, 8))

        description = ctk.CTkLabel(
            self.content,
            text="HTTP yanıt başlıklarını ve temel güvenlik başlıklarını analiz edin.",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=15
            ),
            text_color="#475569"
        )
        description.pack(pady=(0, 18))

        self.http_input = ctk.CTkEntry(
            self.content,
            width=650,
            height=45,
            placeholder_text="Örnek: https://example.com",
            corner_radius=8,
            fg_color="#FFFFFF",
            border_color="#D7DEE8",
            text_color="#0F172A"
        )
        self.http_input.pack(padx=40, pady=10)

        self.http_button = ctk.CTkButton(
            self.content,
            text="BAŞLIKLARI ANALİZ ET",
            command=self.start_http_analysis,
            width=240,
            height=44,
            corner_radius=8,
            fg_color="#1358C8",
            hover_color="#0B4DBB",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=14,
                weight="bold"
            )
        )
        self.http_button.pack(pady=10)

        self.http_status = ctk.CTkLabel(
            self.content,
            text="Analiz bekleniyor.",
            font=ctk.CTkFont(
                family="Consolas",
                size=12
            ),
            text_color="#64748B"
        )
        self.http_status.pack(pady=(0, 8))

        self.http_result = ctk.CTkTextbox(
            self.content,
            width=650,
            height=280,
            corner_radius=10,
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#D7DEE8",
            text_color="#0B4DBB",
            font=ctk.CTkFont(
                family="Consolas",
                size=13
            ),
            wrap="word"
        )
        self.http_result.pack(
            padx=40,
            pady=10,
            fill="both",
            expand=True
        )

        copy_button = ctk.CTkButton(
            self.content,
            text="SONUCU KOPYALA",
            command=self.copy_http_result,
            width=180,
            height=38,
            fg_color="#1358C8",
            hover_color="#0B4DBB"
        )
        copy_button.pack(pady=(0, 20))

    def start_http_analysis(self):
        url = self.http_input.get().strip()

        self.http_result.delete("1.0", "end")

        if not url:
            self.http_result.insert(
                "1.0",
                "[!] Lütfen analiz edilecek bir URL girin."
            )
            return

        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        self.http_button.configure(
            state="disabled",
            text="ANALİZ EDİLİYOR..."
        )

        self.http_status.configure(
            text="HTTP isteği gönderiliyor...",
            text_color="#D97706"
        )

        thread = threading.Thread(
            target=self.run_http_analysis,
            args=(url,),
            daemon=True
        )
        thread.start()

    def run_http_analysis(self, url):
        security_headers = {
            "Content-Security-Policy":
                "İçerik enjeksiyonu ve XSS risklerini azaltır.",

            "Strict-Transport-Security":
                "Tarayıcının HTTPS kullanmasını zorunlu kılar.",

            "X-Content-Type-Options":
                "MIME type sniffing riskini azaltır.",

            "X-Frame-Options":
                "Clickjacking saldırılarına karşı koruma sağlar.",

            "Referrer-Policy":
                "Referrer bilgisinin paylaşımını sınırlar.",

            "Permissions-Policy":
                "Tarayıcı özelliklerinin kullanımını sınırlar."
        }

        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "CyberSecurityToolkit/1.0"
            }
        )

        try:
            with urllib.request.urlopen(
                request,
                timeout=10
            ) as response:

                headers = response.headers
                found_count = 0

                result_lines = [
                    "[+] HTTP isteği başarılı",
                    "",
                    f"İstenen URL : {url}",
                    f"Son URL     : {response.geturl()}",
                    f"HTTP Durumu : {response.status}",
                    "",
                    "=" * 55,
                    "TÜM HTTP BAŞLIKLARI",
                    "=" * 55,
                    ""
                ]

                for header, value in headers.items():
                    result_lines.append(
                        f"{header}: {value}"
                    )

                result_lines.extend([
                    "",
                    "=" * 55,
                    "GÜVENLİK BAŞLIKLARI ANALİZİ",
                    "=" * 55,
                    ""
                ])

                for header, description in security_headers.items():
                    value = headers.get(header)

                    if value:
                        found_count += 1
                        result_lines.append(
                            f"[VAR] {header}"
                        )
                        result_lines.append(
                            f"      {value}"
                        )
                    else:
                        result_lines.append(
                            f"[YOK] {header}"
                        )
                        result_lines.append(
                            f"      {description}"
                        )

                    result_lines.append("")

                result_lines.append(
                    f"Bulunan güvenlik başlığı: "
                    f"{found_count}/{len(security_headers)}"
                )

                if headers.get("Server"):
                    result_lines.append(
                        f"Server bilgisi: {headers.get('Server')}"
                    )

                if headers.get("X-Powered-By"):
                    result_lines.append(
                        f"X-Powered-By: "
                        f"{headers.get('X-Powered-By')}"
                    )

                result = "\n".join(result_lines)

                self.after(
                    0,
                    lambda: self.finish_http_analysis(
                        result,
                        True
                    )
                )

        except urllib.error.HTTPError as error:
            message = (
                f"[!] HTTP hatası: "
                f"{error.code} - {error.reason}"
            )

            self.after(
                0,
                lambda: self.finish_http_analysis(
                    message,
                    False
                )
            )

        except urllib.error.URLError as error:
            message = f"[!] Bağlantı hatası: {error.reason}"

            self.after(
                0,
                lambda: self.finish_http_analysis(
                    message,
                    False
                )
            )

        except TimeoutError:
            self.after(
                0,
                lambda: self.finish_http_analysis(
                    "[!] Bağlantı zaman aşımına uğradı.",
                    False
                )
            )

        except Exception as error:
            message = f"[!] Beklenmeyen hata: {error}"

            self.after(
                0,
                lambda: self.finish_http_analysis(
                    message,
                    False
                )
            )

    def finish_http_analysis(self, result, success):
        self.http_result.delete("1.0", "end")
        self.http_result.insert("1.0", result)

        self.http_button.configure(
            state="normal",
            text="BAŞLIKLARI ANALİZ ET"
        )

        if success:
            self.http_status.configure(
                text="Analiz tamamlandı.",
                text_color="#22C55E"
            )
        else:
            self.http_status.configure(
                text="Analiz başarısız.",
                text_color="#0B4DBB"
            )

    def copy_http_result(self):
        result = self.http_result.get(
            "1.0",
            "end"
        ).strip()

        if result:
            self.clipboard_clear()
            self.clipboard_append(result)
            self.update()

    def show_dns_lookup(self):
        self.set_active_menu("dns")
        self.clear_content()
        self.page_title.configure(text="DNS LOOKUP")

        heading = ctk.CTkLabel(
            self.content,
            text="DNS Lookup",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=30,
                weight="bold"
            ),
            text_color="#0B4DBB"
        )
        heading.pack(pady=(35, 8))

        description = ctk.CTkLabel(
            self.content,
            text="Alan adlarının IP, hostname ve ters DNS bilgilerini görüntüleyin.",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=15
            ),
            text_color="#475569"
        )
        description.pack(pady=(0, 20))

        self.dns_input = ctk.CTkEntry(
            self.content,
            width=650,
            height=45,
            placeholder_text="Örnek: example.com",
            corner_radius=8,
            fg_color="#FFFFFF",
            border_color="#D7DEE8",
            text_color="#0F172A"
        )
        self.dns_input.pack(padx=40, pady=10)

        self.dns_button = ctk.CTkButton(
            self.content,
            text="DNS SORGULA",
            command=self.start_dns_lookup,
            width=220,
            height=44,
            corner_radius=8,
            fg_color="#1358C8",
            hover_color="#0B4DBB",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=14,
                weight="bold"
            )
        )
        self.dns_button.pack(pady=12)

        self.dns_status = ctk.CTkLabel(
            self.content,
            text="Sorgu bekleniyor.",
            font=ctk.CTkFont(
                family="Consolas",
                size=12
            ),
            text_color="#64748B"
        )
        self.dns_status.pack(pady=(0, 8))

        self.dns_result = ctk.CTkTextbox(
            self.content,
            width=650,
            height=250,
            corner_radius=10,
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#D7DEE8",
            text_color="#0B4DBB",
            font=ctk.CTkFont(
                family="Consolas",
                size=14
            ),
            wrap="word"
        )
        self.dns_result.pack(
            padx=40,
            pady=10,
            fill="both",
            expand=True
        )

        copy_button = ctk.CTkButton(
            self.content,
            text="SONUCU KOPYALA",
            command=self.copy_dns_result,
            width=180,
            height=38,
            fg_color="#1358C8",
            hover_color="#0B4DBB"
        )
        copy_button.pack(pady=(0, 20))

    def start_dns_lookup(self):
        domain = self.dns_input.get().strip()

        domain = (
            domain
            .replace("https://", "")
            .replace("http://", "")
            .split("/")[0]
            .split(":")[0]
        )

        self.dns_result.delete("1.0", "end")

        if not domain:
            self.dns_result.insert(
                "1.0",
                "[!] Lütfen geçerli bir alan adı girin."
            )
            return

        self.dns_button.configure(
            state="disabled",
            text="SORGULANIYOR..."
        )
        self.dns_status.configure(
            text="DNS sorgusu çalışıyor...",
            text_color="#D97706"
        )

        thread = threading.Thread(
            target=self.run_dns_lookup,
            args=(domain,),
            daemon=True
        )
        thread.start()

    def run_dns_lookup(self, domain):
        try:
            hostname, aliases, ip_addresses = socket.gethostbyname_ex(
                domain
            )

            unique_ips = sorted(set(ip_addresses))

            result_lines = [
                "[+] DNS sorgusu başarılı",
                "",
                f"Alan adı       : {domain}",
                f"Resmî hostname : {hostname}",
                ""
            ]

            if aliases:
                result_lines.append("Alias kayıtları:")
                for alias in aliases:
                    result_lines.append(f"  - {alias}")
            else:
                result_lines.append("Alias kaydı bulunamadı.")

            result_lines.append("")
            result_lines.append("IP adresleri:")

            for ip_address in unique_ips:
                result_lines.append(f"  - {ip_address}")

            result_lines.append("")
            result_lines.append("Ters DNS kontrolleri:")

            socket.setdefaulttimeout(3)

            for ip_address in unique_ips:
                try:
                    reverse_host, reverse_aliases, _ = (
                        socket.gethostbyaddr(ip_address)
                    )

                    result_lines.append(
                        f"  - {ip_address} -> {reverse_host}"
                    )

                    for alias in reverse_aliases:
                        result_lines.append(
                            f"    Alias: {alias}"
                        )

                except (socket.herror, socket.timeout):
                    result_lines.append(
                        f"  - {ip_address} -> Kayıt bulunamadı"
                    )

            result = "\n".join(result_lines)

            self.after(
                0,
                lambda: self.finish_dns_lookup(
                    result,
                    True
                )
            )

        except socket.gaierror:
            self.after(
                0,
                lambda: self.finish_dns_lookup(
                    "[!] Alan adı çözümlenemedi.",
                    False
                )
            )

        except Exception as error:
            error_message = f"[!] Beklenmeyen hata: {error}"

            self.after(
                0,
                lambda: self.finish_dns_lookup(
                    error_message,
                    False
                )
            )

    def finish_dns_lookup(self, result, success):
        self.dns_result.delete("1.0", "end")
        self.dns_result.insert("1.0", result)

        self.dns_button.configure(
            state="normal",
            text="DNS SORGULA"
        )

        if success:
            self.dns_status.configure(
                text="Sorgu tamamlandı.",
                text_color="#22C55E"
            )
        else:
            self.dns_status.configure(
                text="Sorgu başarısız.",
                text_color="#0B4DBB"
            )

    def open_documentation(self):
        readme_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "README.md"
        )

        if os.path.exists(readme_path):
            os.startfile(readme_path)
        else:
            print("README.md bulunamadı.")
    
    def copy_dns_result(self):
        result = self.dns_result.get(
            "1.0",
            "end"
        ).strip()

        if result:
            self.clipboard_clear()
            self.clipboard_append(result)
            self.update()


if __name__ == "__main__":
    app = CyberSecurityToolkitGUI()
    app.mainloop()