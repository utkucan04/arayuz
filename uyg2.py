from rommenu import MenuSistemi

# Kullanıcıdan eser bilgilerini alan fonksiyon
def ustveri():
    eserAdi = input("Eser Adı: ")
    eserSahibi = input("Eser Sahibi: ")
    userURL = input("Eser URL'si: ")
    sahipURL = input("Eser Sahibi URL'si: ")
    eserTarihi = input("Eser Tarihi (YYYY): ")
    return eserAdi, eserSahibi, userURL, sahipURL, eserTarihi

lisans_aciklamalari = {
    "Kamu Malı / Public Domain": "CC0 Sıfır (Zero): Kamu Malı tahsisi olarak kullanılır. Telif hakkı sınırlaması yoktur; kopyalanabilir, düzenlenebilir, dağıtılabilir ve yeniden kullanılabilir.",
    "CC BY": "Atıf (Attribution): Kaynak atıf vermek kaydıyla ticari amaç dahil kullanılabilir, düzenlenebilir ve dağıtılabilir.",
    "CC BY-SA": "Atıf-AynıLisanslaPaylaş (Attribution-ShareAlike): Kaynak atıf verilerek, aynı lisansla paylaşmak şartıyla kullanılabilir ve türetilebilir.",
    "CC BY-ND": "Atıf-Türetilemez (Attribution-NoDerivatives): Atıf verilerek ticari kullanım dahil kullanılabilir, fakat üzerinde değişiklik yapılamaz.",
    "CC BY-NC": "Atıf-GayriTicari (Attribution-NonCommercial): Atıf verilerek kullanılabilir ama ticari amaçla kullanılamaz.",
    "CC BY-NC-SA": "Atıf-GayriTicari-AynıLisanslaPaylaş: Atıf verilerek, aynı lisansla paylaşmak koşuluyla, ticari olmayan amaçlarla kullanılabilir ve düzenlenebilir.",
    "CC BY-NC-ND": "Atıf-GayriTicari-Türetilemez: Atıf verilerek, sadece ticari olmayan amaçlarla kullanılabilir ve üzerinde değişiklik yapılamaz."
}

# Zengin metin oluşturma fonksiyonu
def zenginmetin(eserAdi, eserSahibi, userURL, sahipURL, eserTarihi, lisans_turu):
    print(f"\nZengin Metin: {eserAdi} © {eserTarihi} {eserSahibi} tarafından {lisans_turu} lisansı ile lisanslanmıştır.\n")
    print(f"Eser URL: {userURL}")
    print(f"Sahip URL: {sahipURL}\n")

# --- Lisans Fonksiyonları ---
def zeropd():
    print("CC0 Sıfır (Zero): Kamu Malı tahsisi olarak kullanılır. Kullanımda olan son sürümü 1.0’dır.")
    eserAdi, eserSahibi, userURL, sahipURL, eserTarihi = ustveri()
    zenginmetin(eserAdi, eserSahibi, userURL, sahipURL, eserTarihi, "CC0 (Public Domain)")

def ccby():
    print("CC BY Atıf (Attribution): En özgür lisanslardan biridir.")
    eserAdi, eserSahibi, userURL, sahipURL, eserTarihi = ustveri()
    zenginmetin(eserAdi, eserSahibi, userURL, sahipURL, eserTarihi, "CC BY")

def ccbysa():
    print("CC BY-SA Atıf-AynıLisanslaPaylaş: Kaynak gösterip aynı lisansı sürdürme şartı vardır.")
    eserAdi, eserSahibi, userURL, sahipURL, eserTarihi = ustveri()
    zenginmetin(eserAdi, eserSahibi, userURL, sahipURL, eserTarihi, "CC BY-SA")

def ccbynd():
    print("CC BY-ND Atıf-Türetilemez: Kaynak gösterilerek paylaşılabilir ama değiştirilemez.")
    eserAdi, eserSahibi, userURL, sahipURL, eserTarihi = ustveri()
    zenginmetin(eserAdi, eserSahibi, userURL, sahipURL, eserTarihi, "CC BY-ND")

def ccbync():
    print("CC BY-NC Atıf-GayriTicari: Kaynak gösterilerek paylaşılabilir, ticari kullanım yasaktır.")
    eserAdi, eserSahibi, userURL, sahipURL, eserTarihi = ustveri()
    zenginmetin(eserAdi, eserSahibi, userURL, sahipURL, eserTarihi, "CC BY-NC")

def ccbyncsa():
    print("CC BY-NC-SA Atıf-GayriTicari-AynıLisanslaPaylaş: Kaynak göster, ticari olmayan ve aynı lisansla paylaş.")
    eserAdi, eserSahibi, userURL, sahipURL, eserTarihi = ustveri()
    zenginmetin(eserAdi, eserSahibi, userURL, sahipURL, eserTarihi, "CC BY-NC-SA")

def ccbyncnd():
    print("CC BY-NC-ND Atıf-GayriTicari-Türetilemez: Kaynak göster, ticari olmayan, değiştirilemez.")
    eserAdi, eserSahibi, userURL, sahipURL, eserTarihi = ustveri()
    zenginmetin(eserAdi, eserSahibi, userURL, sahipURL, eserTarihi, "CC BY-NC-ND")

# --- Menü Kurulumu ---
menu = MenuSistemi()
menu.karsilama("CC Lisans Seçim Programı")

menu_items = {
    "Kamu Malı / Public Domain": zeropd,
    "CC BY": ccby,
    "CC BY-SA": ccbysa,
    "CC BY-ND": ccbynd,
    "CC BY-NC": ccbync,
    "CC BY-NC-SA": ccbyncsa,
    "CC BY-NC-ND": ccbyncnd
}

menu.menuyuCalistir(menu_items)
