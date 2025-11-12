import tkinter as tk
from tkinter import ttk, messagebox

# --- Arayüz fonksiyonları ---
def zenginmetin_goster(eserAdi, eserSahibi, userURL, sahipURL, eserTarihi, lisans):
    sonuc = (
        f"\nZengin Metin:\n\n"
        f"{eserAdi} © {eserTarihi} {eserSahibi} tarafından {lisans} lisansı ile lisanslanmıştır.\n\n"
        f"Eser URL: {userURL}\n"
        f"Sahip URL: {sahipURL}"
    )
    sonuc_yazisi.config(state="normal")
    sonuc_yazisi.delete(1.0, tk.END)
    sonuc_yazisi.insert(tk.END, sonuc)
    sonuc_yazisi.config(state="disabled")

def bilgileri_al_ve_yaz(lisans):
    # Kullanıcıdan bilgileri al
    eserAdi = entry_eserAdi.get().strip()
    eserSahibi = entry_eserSahibi.get().strip()
    userURL = entry_userURL.get().strip()
    sahipURL = entry_sahipURL.get().strip()
    eserTarihi = entry_eserTarihi.get().strip()

    if not eserAdi or not eserSahibi or not eserTarihi:
        messagebox.showwarning("Eksik Bilgi", "Lütfen en az Eser Adı, Sahibi ve Tarihini giriniz.")
        return

    zenginmetin_goster(eserAdi, eserSahibi, userURL, sahipURL, eserTarihi, lisans)

# --- Ana pencere ---
pencere = tk.Tk()
pencere.title("Creative Commons Lisans Arayüzü")
pencere.geometry("650x600")
pencere.resizable(False, False)

baslik = ttk.Label(pencere, text="CC Lisans Seçim Arayüzü", font=("Arial", 16, "bold"))
baslik.pack(pady=10)

# Bilgi giriş çerçevesi
bilgi_frame = ttk.LabelFrame(pencere, text="Eser Bilgileri", padding=10)
bilgi_frame.pack(fill="x", padx=20, pady=10)

ttk.Label(bilgi_frame, text="Eser Adı:").grid(row=0, column=0, sticky="e", pady=5)
entry_eserAdi = ttk.Entry(bilgi_frame, width=40)
entry_eserAdi.grid(row=0, column=1)

ttk.Label(bilgi_frame, text="Eser Sahibi:").grid(row=1, column=0, sticky="e", pady=5)
entry_eserSahibi = ttk.Entry(bilgi_frame, width=40)
entry_eserSahibi.grid(row=1, column=1)

ttk.Label(bilgi_frame, text="Eser URL'si:").grid(row=2, column=0, sticky="e", pady=5)
entry_userURL = ttk.Entry(bilgi_frame, width=40)
entry_userURL.grid(row=2, column=1)

ttk.Label(bilgi_frame, text="Eser Sahibi URL'si:").grid(row=3, column=0, sticky="e", pady=5)
entry_sahipURL = ttk.Entry(bilgi_frame, width=40)
entry_sahipURL.grid(row=3, column=1)

ttk.Label(bilgi_frame, text="Eser Tarihi (YYYY):").grid(row=4, column=0, sticky="e", pady=5)
entry_eserTarihi = ttk.Entry(bilgi_frame, width=40)
entry_eserTarihi.grid(row=4, column=1)

# Lisans seçim çerçevesi
lisans_frame = ttk.LabelFrame(pencere, text="Lisans Seç", padding=10)
lisans_frame.pack(fill="x", padx=20, pady=10)

lisanslar = [
    "Kamu Malı / Public Domain",
    "CC BY",
    "CC BY-SA",
    "CC BY-ND",
    "CC BY-NC",
    "CC BY-NC-SA",
    "CC BY-NC-ND"
]

for i, lisans in enumerate(lisanslar):
    ttk.Button(lisans_frame, text=lisans, width=25, command=lambda l=lisans: bilgileri_al_ve_yaz(l)).grid(row=i//2, column=i%2, padx=10, pady=5)

# Çıktı alanı
sonuc_frame = ttk.LabelFrame(pencere, text="Zengin Metin Çıktısı", padding=10)
sonuc_frame.pack(fill="both", expand=True, padx=20, pady=10)

sonuc_yazisi = tk.Text(sonuc_frame, height=10, wrap="word", state="disabled")
sonuc_yazisi.pack(fill="both", expand=True)

# Çıkış butonu
ttk.Button(pencere, text="Kapat", command=pencere.destroy).pack(pady=10)

pencere.mainloop()
