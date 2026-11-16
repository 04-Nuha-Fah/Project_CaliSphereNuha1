"""
Project CaliSphere (asli)
"""

import math
import os
import tkinter as tk

FOLDER_UTAMA = os.path.dirname(os.path.abspath(__file__))

#Warna dan frame
KUNING = "#FFEF00"
KUNING_NEON = "#CCFF00"
HITAM = "#1A1A1A"
ABU_ABU = "#282828"

TEMA = {
    "terang": dict(latar="#EFEFEF", kartu="#FFFFFF", teks=ABU_ABU,
                  keterangan="#5E5E5E", jalur="#D2D2D2", di_atas_merah=ABU_ABU),
    "alas": dict(latar=HITAM, kartu=ABU_ABU, teks="#EFEFEF",
                 keterangan="#A9A9A9", jalur="#3A3A3A", di_atas_merah=ABU_ABU),
}

FONT = "Helvetica"
BATAS_LEBAR = 900
UKURAN_HP = (420, 780)
UKURAN_LAPTOP = (1100, 720)
LEBAR_SIDEBAR = 190
LEBAR_KOLOM_KIRI = 290
WAKTU_LATIHAN = 30
WAKTU_ISTIRAHAT = 120

TEKS_POPUP = "Lakukan latihan ini 4 kali seminggu dan gunakan sisa hari untuk istirahat"

#Tata susunan icon char
IKON = {
    # Mode Easy
    "wall_pushup": dict(
        alas=[(84, 4, 84, 76)],
        badan=[(16, 70, 60, 32), (60, 32, 84, 46)],
        kepala=[(72, 26, 6)]
    ),
    "knee_pushup": dict(
        badan=[(28, 50, 76, 42), (76, 42, 80, 68),
               (28, 50, 18, 68), (18, 68, 12, 58)],
        kepala=[(86, 38, 6)]
    ),
    "squat": dict(
        badan=[(44, 26, 38, 44), (38, 44, 66, 52),
               (66, 52, 64, 70), (42, 30, 62, 30)],
        kepala=[(52, 16, 6)]
    ),
    "lunge": dict(
        badan=[(52, 26, 52, 48), (52, 48, 70, 56),
               (70, 56, 74, 70), (52, 48, 24, 68)],
        kepala=[(52, 16, 6)]
    ),
    "plank": dict(
        badan=[(10, 68, 76, 56), (76, 56, 76, 70)],
        kepala=[(88, 52, 6)]
    ),

    # Mode Normal
    "pushup": dict(
        badan=[(10, 70, 76, 50), (76, 50, 76, 70)],
        kepala=[(88, 46, 6)]
    ),
    "pullup": dict(
        alas=[(8, 10, 92, 10)],
        badan=[(36, 10, 44, 24), (64, 10, 56, 24),
               (50, 36, 50, 56), (50, 56, 40, 72),
               (50, 56, 60, 72)],
        kepala=[(52, 30, 6)]
    ),
    "dips": dict(
        alas=[(60, 42, 94, 42)],
        badan=[(34, 30, 36, 58), (36, 34, 60, 42),
               (36, 58, 28, 72), (36, 58, 48, 72)],
        kepala=[(32, 20, 6)]
    ),
    "bulgarian": dict(
        alas=[(72, 66, 94, 66), (72, 66, 72, 72),
               (94, 66, 94, 72)],
        badan=[(54, 26, 54, 48), (54, 48, 36, 58),
               (36, 58, 34, 72), (54, 48, 78, 60),
               (78, 60, 78, 66)],
        kepala=[(54, 16, 6)]
    ),
    "pike": dict(
        badan=[(14, 72, 40, 34), (40, 34, 66, 50),
               (66, 50, 70, 64)],
        kepala=[(76, 56, 6)]
    ),
    "adv_plank": dict(
        badan=[(12, 70, 76, 54), (76, 54, 76, 70),
               (82, 54, 96, 54)],
        kepala=[(88, 44, 6)]
    ),

    # Mode Hard
    "handstand": dict(
        badan=[(48, 72, 48, 14), (48, 14, 44, 6),
               (48, 14, 56, 6)],
        kepala=[(62, 64, 6)]
    ),
    "archer": dict(
        badan=[(52, 36, 52, 58), (52, 42, 28, 70),
               (52, 42, 76, 54), (76, 54, 76, 71),
               (52, 58, 44, 72), (52, 58, 60, 72)],
        kepala=[(52, 28, 6)]
    ),
    "human_flag": dict(
        alas=[(16, 8, 16, 78)],
        badan=[(18, 30, 32, 40), (18, 52, 32, 40),
               (32, 40, 94, 40)],
        kepala=[(38, 34, 6)]
    ),
    "lsit": dict(
        badan=[(32, 30, 32, 60), (32, 60, 80, 60),
               (32, 60, 32, 72)],
        kepala=[(32, 20, 6)]
    ),
    "pistol": dict(
        badan=[(44, 26, 40, 44), (40, 44, 72, 44),
               (40, 44, 32, 58), (32, 58, 40, 72),
               (42, 32, 64, 32)],
        kepala=[(44, 16, 6)]
    ),
}
# ----------------------------------------------------------------------------
# Data level latihan
# ----------------------------------------------------------------------------
DATA_LEVEL = {
    "easy": {
        "label": "MUDAH",
        "sasaran": "Pemula",
        "deskripsi": (
            "Kalistenik adalah latihan kebugaran yang memakai berat badan "
            "sendiri sebagai beban, tanpa alas, sehingga bisa dilakukan di "
            "mana saja.\n\nMode Mudah dibuat untuk pemula yang baru mulai "
            "berolahraga. Fokusnya mengenalkan gerakan dasar, membangun "
            "teknik yang benar, dan membentuk kebiasaan latihan."
        ),
        "daftar_gerakan": [
            ("Wall Pushup", "wall_pushup",
             "Push up (tekan badan) berdiri menghadap tembok. Gerakan paling ringan untuk melatih dada, bahu, dan lengan belakang.",
             " Berdirilah satu langkah dari tembok, letakkan telapak tangan di dinding setinggi bahu. "
             "Tekuk siku hingga dada mendekati tembok, lalu dorong kembali. Jaga tubuh tetap lurus dan perut mengencang."),
            ("Knee Pushup", "knee_pushup",
             "Push up dengan lutut menempel di lantai untuk membangun kekuatan tubuh bagian atas.",
             " Posisikan tangan selebar bahu, lutut di lantai, tubuh lurus dari kepala hingga lutut. "
             "Turunkan dada mendekati lantai, lalu dorong naik. Jangan biarkan pinggul turun atau menungging."),
            ("Squat", "squat",
             "Gerakan jongkok dasar (squat) untuk melatih paha, bokong, dan kestabilan tubuh.",
             " Berdiri selebar bahu, dorong pinggul ke belakang seperti duduk di kursi. "
             "Turunkan badan hingga paha hampir sejajar lantai, dada tetap tegak, lalu berdiri kembali dengan menekan tumit."),
            ("Lunge", "lunge",
             "Melangkah ke depan lalu menekuk lutut (lunge), melatih kaki satu sisi dan keseimbangan.",
             " Langkahkan satu kaki ke depan, turunkan badan hingga kedua lutut menekuk sekitar 90 derajat. "
             "Lutut depan tidak melewati ujung kaki. Dorong kembali ke posisi awal dan ganti kaki."),
            ("Plank", "plank",
             "Menahan tubuh lurus seperti papan (plank) bertumpu pada lengan bawah untuk melatih otot inti.",
             " Letakkan siku tepat di bawah bahu, tubuh lurus dari kepala hingga tumit. "
             "Kencangkan perut dan bokong, pandangan ke lantai, dan bernapas normal selama menahan posisi."),
        ],
    },
    "normal": {
        "label": "SEDANG",
        "sasaran": "Terbiasa",
        "deskripsi": (
            "Kalistenik melatih kekuatan, kontrol, dan kelenturan tubuh lewat "
            "gerakan berat badan.\n\nMode Sedang ditujukan bagi kamu yang "
            "sudah pernah berolahraga dan ingin mendalami. Gerakannya "
            "membutuhkan kekuatan dasar yang lebih baik dan teknik yang "
            "lebih rapi."
        ),
        "daftar_gerakan": [
            ("Pushup", "pushup",
             "Push up standar dengan tubuh lurus, melatih dada, bahu, lengan belakang, dan otot inti sekaligus.",
             " Tangan selebar bahu, tubuh lurus seperti papan. Turunkan dada hingga hampir menyentuh lantai, "
             "siku membentuk sudut sekitar 30 derajat dari tubuh, lalu dorong naik dengan kuat."),
            ("Pullup", "pullup",
             "Menarik tubuh ke atas hingga dagu melewati palang (pull up). Melatih punggung dan lengan depan.",
             " Pegang palang dengan genggaman sedikit lebih lebar dari bahu. Tarik dengan menggerakkan siku ke bawah, "
             "hindari mengayun. Turunkan perlahan hingga lengan lurus sebelum mengulang."),
            ("Dips", "dips",
             "Menurunkan dan mendorong tubuh di antara dua tumpuan (dips). Melatih lengan belakang, dada bawah, dan bahu.",
             " Gunakan palang paralel atau dua kursi kokoh. Tekuk siku hingga bahu sejajar siku, "
             "lalu dorong naik. Jaga bahu tetap turun dan dada sedikit condong ke depan."),
            ("Bulgarian Squat", "bulgarian",
             "Jongkok satu kaki dengan kaki belakang bertumpu di bangku (Bulgarian split squat). Melatih paha, bokong, dan keseimbangan.",
             " Letakkan punggung kaki belakang di bangku, kaki depan melangkah cukup jauh. "
             "Turunkan badan hingga paha depan sejajar lantai, lalu naik. Selesaikan satu sisi sebelum ganti kaki."),
            ("Pike Pushup", "pike",
             "Push up dengan pinggul diangkat membentuk huruf V terbalik (pike push up). Fokus pada bahu.",
             " Mulai dari posisi V terbalik, kaki dan tangan tetap di lantai. Tekuk siku hingga kepala mendekati lantai "
             "di antara kedua tangan, lalu dorong naik. Ini persiapan menuju push up berdiri tangan."),
            ("Advanced Plank", "adv_plank",
             "Variasi papan yang lebih berat, misalnya dengan mengangkat satu kaki atau tangan bergantian.",
             " Mulai dari posisi papan, lalu angkat satu kaki atau satu tangan tanpa memutar pinggul. "
             "Tahan beberapa detik, ganti sisi. Pertahankan perut mengencang dan tubuh tetap lurus."),
        ],
    },
    "hard": {
        "label": "SULIT",
        "sasaran": "Terlatih",
        "deskripsi": (
            "Kalistenik tingkat lanjut menuntut kekuatan, keseimbangan, dan "
            "kontrol tubuh yang tinggi.\n\nMode Sulit hanya untuk kamu yang "
            "sudah sangat berpengalaman. Lakukan pemanasan yang cukup, "
            "perhatikan batas tubuh, dan utamakan keamanan di atas target."
        ),
        "daftar_gerakan": [
            ("Handstand", "handstand",
             "Berdiri dengan bertumpu pada kedua tangan (handstand). Melatih bahu, otot inti, dan keseimbangan.",
             " Mulai dekat tembok untuk bantuan. Tangan selebar bahu, dorong lantai dengan kuat, "
             "tubuh lurus dari tangan hingga ujung kaki. Pandangan ke arah ujung jari."),
            ("Archer Pushup", "archer",
             "Push up dengan satu lengan lurus ke samping (archer push up), langkah menuju push up satu lengan.",
             " Posisi tangan lebar. Turunkan badan ke satu sisi sementara lengan sisi lain tetap lurus. "
             "Dorong kembali ke tengah lalu ganti sisi. Beban utama ada di lengan yang menekuk."),
            ("Human Flag", "human_flag",
             "Menahan tubuh horizontal di sebuah tiang (human flag). Salah satu gerakan kalistenik paling sulit.",
             " Pegang tiang dengan satu tangan di atas dan satu di bawah. Dorong tangan bawah, tarik tangan atas, "
             "lalu angkat tubuh sejajar lantai. Butuh kekuatan otot inti dan bahu yang sangat kuat."),
            ("L Sit", "lsit",
             "Menahan tubuh di atas tangan dengan kaki lurus ke depan membentuk huruf L (L-sit).",
             " Tekan lantai atau palang paralel dengan kedua tangan hingga pinggul terangkat. "
             "Kaki tetap lurus dan sejajar lantai. Kencangkan perut dan dorong bahu ke bawah."),
            ("Pistol Squat", "pistol",
             "Jongkok penuh dengan satu kaki, kaki lainnya lurus ke depan (pistol squat). Melatih kekuatan, kelenturan, dan kontrol.",
             " Berdiri satu kaki, luruskan kaki lainnya ke depan. Turunkan badan hingga bokong hampir menyentuh tumit, "
             "tumit tetap menempel lantai, lalu berdiri kembali. Gunakan pegangan jika perlu."),
        ],
    },
}

URUTAN_LEVEL = ("easy", "normal", "hard")

def kotak_frame(kanvas, x1, y1, x2, y2, r, **opsi):
    """Gambar persegi panjang bersudut membulat."""
    titik = [
        x1 + r, y1,  x2 - r, y1,  x2, y1,  x2, y1 + r,
        x2, y2 - r,  x2, y2,      x2 - r, y2,  x1 + r, y2,
        x1, y2,      x1, y2 - r,  x1, y1 + r,  x1, y1,
    ]
    return kanvas.create_polygon(titik, smooth=True, **opsi)


class TombolBulat(tk.Canvas):
    """Tombol kanvas dengan sudut membulat dan efek sorot."""

    def __init__(self, induk, teks, aksi, lebar, tinggi, latar,
                 isi=KUNING, warna_teks=ABU_ABU, garis=None,
                 ukuran_font=18, radius=16):
        super().__init__(induk, width=lebar, height=tinggi, bg=latar,
                         highlightthickness=0, bd=0, cursor="hand2")
        self.lebar, self.tinggi, self.radius = lebar, tinggi, radius
        self.teks, self.aksi = teks, aksi
        self.isi, self.warna_teks, self.garis = isi, warna_teks, garis
        self.huruf = (FONT, ukuran_font, "bold")
        self._sorot = False
        self.frame()
        self.bind("<Enter>", lambda e: self.sorot(True))
        self.bind("<Leave>", lambda e: self.sorot(False))
        self.bind("<Button-1>", lambda e: self.aksi())

    def sorot(self, nilai):
        self._sorot = nilai
        self.frame()

    def ubah_teks(self, teks_baru):
        self.teks = teks_baru
        self.frame()

    def frame(self):
        self.delete("all")
        warna = KUNING_NEON if (self._sorot and self.isi == KUNING) else self.isi
        kotak_frame(self, 2, 2, self.lebar - 2, self.tinggi - 2, self.radius,
                    fill=warna, outline=self.garis or warna, width=2)
        self.create_text(self.lebar / 2, self.tinggi / 2, text=self.teks,
                         fill=self.warna_teks, font=self.huruf)


def icon_stickman(kanvas, kunci, ox, oy, skala, tema, tebal=3):
    data = IKON[kunci]
    lebar_garis = max(2, int(tebal * skala))

    def garis(x1, y1, x2, y2, warna, **extra):
        kanvas.create_line(ox + x1 * skala, oy + y1 * skala,
                           ox + x2 * skala, oy + y2 * skala,
                           fill=warna, width=lebar_garis,
                           capstyle="round", **extra)

    garis(5, 70, 95, 70, tema["teks"])
    for seg in data.get("alas", []):
        garis(*seg, tema["teks"])
    for seg in data["badan"]:
        garis(*seg, KUNING, joinstyle="round")
    for x, y, r in data["kepala"]:
        kanvas.create_oval(ox + (x - r) * skala, oy + (y - r) * skala,
                           ox + (x + r) * skala, oy + (y + r) * skala,
                           fill=KUNING, outline=KUNING)


# ----------------------------------------------------------------------------
# Aplikasi utama
# ----------------------------------------------------------------------------
class CaliSphere(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CaliSphere")
        self.logo_aplikasi()
        self.geometry(f"{UKURAN_LAPTOP[0]}x{UKURAN_LAPTOP[1]}")
        self.minsize(380, 640)

        self.tema_aktif = "alas"
        self.halaman = "home"
        self.ringkas = False
        self.lebar = UKURAN_LAPTOP[0]
        self.terbuka = {}
        self.sesi = None
        self.pekerjaan = None
        self.scrol = None
        self.kanvas_timer = None
        self.tombol_jeda = None
        self.label_langkah = []
        self.ukuran_akhir = None
        self.resize = None

        for peristiwa in ("<MouseWheel>", "<Button-4>", "<Button-5>"):
            self.bind_all(peristiwa, self.scroll)
        self.bind("<Configure>", self.berubah_ukuran)
        self.protocol("WM_DELETE_WINDOW", self.tutup)
        self.gambar_ulang()

    # ------------------------------------------------------------- ikon/logo
    def logo_aplikasi(self):
        self.logo = None
        berkas_ico = os.path.join(FOLDER_UTAMA, "ikon.ico")
        berkas_png = os.path.join(FOLDER_UTAMA, "ikon.png")
        try:
            if os.path.exists(berkas_png):
                self.logo = tk.PhotoImage(file=berkas_png)
        except tk.TclError:
            self.logo = None
        try:
            if os.name == "nt" and os.path.exists(berkas_ico):
                self.iconbitmap(berkas_ico)
            elif self.logo is not None:
                self.iconphoto(True, self.logo)
        except tk.TclError:
            pass

    def logo_kiri(self, ukuran):
        if self.logo is None:
            return None
        faktor = max(1, round(max(self.logo.width(), self.logo.height()) / ukuran))
        return self.logo.subsample(faktor, faktor) if faktor > 1 else self.logo

    def logo_tengah(self, induk, latar, ukuran, **tata):
        gambar = self.logo_kiri(ukuran)
        if gambar is None:
            return None
        label = tk.Label(induk, image=gambar, bg=latar, bd=0)
        label.image = gambar
        label.pack(**tata)
        return label

    @property
    def tema(self):
        return TEMA[self.tema_aktif]

    def tutup(self):
        self.timer_mati()
        self.destroy()

    def timer_mati(self):
        if self.pekerjaan is not None:
            try:
                self.after_cancel(self.pekerjaan)
            except Exception:
                pass
            self.pekerjaan = None

    def scroll(self, e):
        kv = self.scrol
        if kv is None or not kv.winfo_exists():
            return
        if kv.yview() == (0.0, 1.0):
            return
        if e.num == 4:
            arah = -1
        elif e.num == 5:
            arah = 1
        else:
            arah = -1 if e.delta > 0 else 1
        kv.yview_scroll(arah * 2, "units")

    def berubah_ukuran(self, e):
        if e.widget is not self:
            return
        if (e.width, e.height) == self.ukuran_akhir:
            return
        self.ukuran_akhir = (e.width, e.height)
        if self.resize is not None:
            self.after_cancel(self.resize)
        self.resize = self.after(200, self._setelah_ubah)

    def _setelah_ubah(self):
        self.resize = None
        self.gambar_ulang()

    def ganti_tema(self):
        self.tema_aktif = "alas" if self.tema_aktif == "terang" else "terang"
        self.gambar_ulang()

    def ganti_tampilan(self):
        lebar, tinggi = UKURAN_LAPTOP if self.ringkas else UKURAN_HP
        self.geometry(f"{lebar}x{tinggi}")

    def buka(self, halaman):
        self.halaman = halaman
        self.gambar_ulang()

    # ------------------------------------------------------------ render
    def gambar_ulang(self):
        tema = self.tema
        self.update_idletasks()
        lebar = self.winfo_width()
        if lebar <= 1:
            lebar = UKURAN_LAPTOP[0]
        self.lebar = lebar
        self.ringkas = lebar < BATAS_LEBAR

        self.configure(bg=tema["latar"])
        for anak in self.winfo_children():
            if not isinstance(anak, tk.Toplevel):
                anak.destroy()
        self.scrol = None
        self.kanvas_timer = None
        self.tombol_jeda = None
        self.label_langkah = []

        di_timer = self.halaman == "timer"
        if self.ringkas:
            wadah = self
            self.header(wadah)
            if not di_timer:
                self.nav()
        else:
            if not di_timer:
                self.sidebar()
            wadah = tk.Frame(self, bg=tema["latar"])
            wadah.pack(side="left", fill="both", expand=True)
            self.header(wadah)

        self.isi = tk.Frame(wadah, bg=tema["latar"])
        self.isi.pack(fill="both", expand=True)

        if self.halaman == "home":
            self.beranda()
        elif di_timer:
            self.timer()
        else:
            self.susunan_level(self.halaman)

    # ------------------------------------------------------------ header
    def header(self, induk):
        tema = self.tema
        bar = tk.Frame(induk, bg=tema["latar"], height=56)
        bar.pack(side="top", fill="x")
        bar.pack_propagate(False)

        tampil_judul = ((self.ringkas and self.halaman != "home") or
                        (not self.ringkas and self.halaman == "timer"))
        if tampil_judul:
            logo = self.logo_tengah(bar, tema["latar"], 32, side="left", padx=(16, 0))
            if logo is not None:
                logo.config(cursor="hand2")
                logo.bind("<Button-1>", lambda e: self.buka("home"))
            judul = tk.Label(bar, text="CaliSphere", fg=KUNING, bg=tema["latar"],
                             font=(FONT, 16, "bold"), cursor="hand2")
            judul.pack(side="left", padx=(8, 18))
            judul.bind("<Button-1>", lambda e: self.buka("home"))

        # tombol tema terang / alas (kanan atas)
        kv_tema = tk.Canvas(bar, width=36, height=36, bg=tema["latar"],
                            highlightthickness=0, cursor="hand2")
        kv_tema.pack(side="right", padx=(8, 16), pady=10)
        if self.tema_aktif == "terang":
            kv_tema.create_oval(11, 11, 25, 25, fill=KUNING, outline=KUNING)
            for i in range(8):
                sudut = math.radians((i * 45))
                kv_tema.create_line(18 + 11 * math.cos(sudut), 18 + 11 * math.sin(sudut),
                               18 + 15 * math.cos(sudut), 18 + 15 * math.sin(sudut),
                                    fill=KUNING, width=3, capstyle="round")
        else:
            kv_tema.create_oval(5, 5, 31, 31, fill=KUNING, outline=KUNING)
            kv_tema.create_oval(13, 0, 38, 24, fill=tema["latar"], outline=tema["latar"])
        kv_tema.bind("<Button-1>", lambda e: self.ganti_tema())

        # tombol ganti tampilan HP ke Laptop dan sebaliknya
        kv_tampil = tk.Canvas(bar, width=36, height=36, bg=tema["latar"],
                              highlightthickness=0, cursor="hand2")
        kv_tampil.pack(side="right", pady=10)
        if self.ringkas:
            kv_tampil.create_rectangle(7, 9, 29, 24, outline=KUNING, width=2)
            kv_tampil.create_line(3, 28, 33, 28, fill=KUNING, width=3, capstyle="round")
        else:
            kotak_frame(kv_tampil, 10, 4, 26, 32, 4, fill=tema["latar"],
                        outline=KUNING, width=2)
            kv_tampil.create_line(15, 27, 21, 27, fill=KUNING, width=2, capstyle="round")
        kv_tampil.bind("<Button-1>", lambda e: self.ganti_tampilan())

    # ----------------------------------------------tampilan HP
    def nav(self):
        tema = self.tema
        nav = tk.Frame(self, bg=tema["latar"])
        nav.pack(side="bottom", fill="x")
        tk.Frame(nav, bg=tema["jalur"], height=1).pack(fill="x")
        baris = tk.Frame(nav, bg=tema["latar"])
        baris.pack(fill="x", pady=(0, 10))
        for kunci in URUTAN_LEVEL:
            aktif = self.halaman == kunci
            kolom = tk.Frame(baris, bg=tema["latar"], cursor="hand2")
            kolom.pack(side="left", expand=True, fill="x")
            tk.Frame(kolom, height=5, bg=KUNING if aktif else tema["latar"]).pack(
                fill="x", padx=36)
            label = tk.Label(kolom, text=DATA_LEVEL[kunci]["label"], bg=tema["latar"],
                             fg=KUNING if aktif else tema["teks"],
                             font=(FONT, 15, "bold" if aktif else "normal"),
                             cursor="hand2")
            label.pack(pady=(8, 4))
            for w in (kolom, label):
                w.bind("<Button-1>", lambda e, k=kunci: self.buka(k))

    # ---------------------------------------------tampilan Laptop
    def sidebar(self):
        tema = self.tema
        samping = tk.Frame(self, bg=tema["kartu"], width=LEBAR_SIDEBAR)
        samping.pack(side="left", fill="y")
        samping.pack_propagate(False)

        logo = self.logo_tengah(samping, tema["kartu"], 64, anchor="w",
                                 padx=20, pady=(20, 0))
        if logo is not None:
            logo.config(cursor="hand2")
            logo.bind("<Button-1>", lambda e: self.buka("home"))
        judul = tk.Label(samping, text="CaliSphere", fg=KUNING, bg=tema["kartu"],
                         font=(FONT, 20, "bold"), cursor="hand2")
        judul.pack(anchor="w", padx=20, pady=(8 if logo else 24, 0))
        judul.bind("<Button-1>", lambda e: self.buka("home"))
        tk.Label(samping, text="Kalistenik untuk hidup sehat", fg=tema["keterangan"],
                 bg=tema["kartu"], font=(FONT, 9), anchor="w", justify="left",
                 wraplength=LEBAR_SIDEBAR - 40).pack(anchor="w", padx=20, pady=(2, 28))

        for kunci in URUTAN_LEVEL:
            aktif = self.halaman == kunci
            baris = tk.Frame(samping, bg=tema["kartu"], cursor="hand2")
            baris.pack(fill="x", pady=3)
            tk.Frame(baris, width=5, bg=KUNING if aktif else tema["kartu"]).pack(
                side="left", fill="y")
            teks = tk.Frame(baris, bg=tema["kartu"], cursor="hand2")
            teks.pack(side="left", fill="x", padx=(16, 0), pady=8)
            judul_lv = tk.Label(teks, text=DATA_LEVEL[kunci]["label"], bg=tema["kartu"],
                                fg=KUNING if aktif else tema["teks"], cursor="hand2",
                                font=(FONT, 15, "bold" if aktif else "normal"))
            judul_lv.pack(anchor="w")
            sub_lv = tk.Label(teks, text=DATA_LEVEL[kunci]["sasaran"], bg=tema["kartu"],
                              fg=tema["keterangan"], font=(FONT, 9), cursor="hand2")
            sub_lv.pack(anchor="w")
            for w in (baris, teks, judul_lv, sub_lv):
                w.bind("<Button-1>", lambda e, k=kunci: self.buka(k))

    # -------------------------------------------------------------- beranda
    def beranda(self):
        tema = self.tema
        besar = not self.ringkas
        kotak = tk.Frame(self.isi, bg=tema["latar"])
        kotak.pack(expand=True)

        self.logo_tengah(kotak, tema["latar"], 128 if besar else 96, pady=(0, 10))
        tk.Label(kotak, text="CaliSphere", fg=KUNING, bg=tema["latar"],
                 font=(FONT, 46 if besar else 34, "bold")).pack(pady=(0, 6))
        subjudul = ("Pemandu hidup sehat dengan olahraga kalistenik" if besar
                    else "Pemandu hidup sehat dengan\nolahraga kalistenik")
        tk.Label(kotak, text=subjudul, fg=tema["keterangan"], bg=tema["latar"],
                 font=(FONT, 14 if besar else 12), justify="center").pack(
            pady=(0, 34 if besar else 30))

        baris = tk.Frame(kotak, bg=tema["latar"])
        baris.pack(pady=(0, 40 if besar else 36))
        contoh = {"easy": "squat", "normal": "pullup", "hard": "handstand"}
        skala = 1.35 if besar else 1.0
        for kunci in URUTAN_LEVEL:
            kolom = tk.Frame(baris, bg=tema["latar"])
            kolom.pack(side="left", padx=18 if besar else 6)
            kv = tk.Canvas(kolom, width=int(100 * skala), height=int(80 * skala),
                           bg=tema["latar"], highlightthickness=0)
            kv.pack()
            icon_stickman(kv, contoh[kunci], 0, 0, skala, tema)
            lv = DATA_LEVEL[kunci]
            tk.Label(kolom, text=lv["label"].title(), fg=tema["teks"], bg=tema["latar"],
                     font=(FONT, 11 if besar else 10, "bold")).pack()
            tk.Label(kolom, text=f"({lv['sasaran']})", fg=tema["keterangan"],
                     bg=tema["latar"], font=(FONT, 10 if besar else 9)).pack()

        TombolBulat(kotak, "AYO LATIHAN", lambda: self.buka("easy"),
                    320 if besar else 260, 68 if besar else 62, tema["latar"],
                    warna_teks=tema["di_atas_merah"],
                    ukuran_font=22 if besar else 20, radius=18).pack()

    # ------------------------------------------------------- halaman level
    def area_scroll(self, induk):
        tema = self.tema
        pembungkus = tk.Frame(induk, bg=tema["latar"])
        pembungkus.pack(side="top", fill="both", expand=True)
        kv = tk.Canvas(pembungkus, bg=tema["latar"], highlightthickness=0, bd=0)
        kv.pack(fill="both", expand=True)
        dalam = tk.Frame(kv, bg=tema["latar"])
        window = kv.create_window((0, 0), window=dalam, anchor="nw")
        dalam.bind("<Configure>", lambda e: kv.configure(scrollregion=kv.bbox("all")))
        kv.bind("<Configure>", lambda e: kv.itemconfigure(window, width=e.width))
        self.scrol = kv
        return dalam

    def info(self, induk, lv, bungkus, padx, pady):
        tema = self.tema
        kartu = tk.Frame(induk, bg=tema["kartu"], highlightbackground=KUNING,
                         highlightthickness=1)
        kartu.pack(fill="x", padx=padx, pady=pady)
        tk.Label(kartu, text=f"Mode {lv['label'].title()} ({lv['sasaran']})",
                 fg=KUNING, bg=tema["kartu"], font=(FONT, 14, "bold"),
                 anchor="w").pack(fill="x", padx=14, pady=(12, 4))
        tk.Label(kartu, text=lv["deskripsi"], fg=tema["teks"], bg=tema["kartu"],
                 font=(FONT, 10), justify="left", anchor="w",
                 wraplength=bungkus).pack(fill="x", padx=14, pady=(0, 12))

    def susunan_level(self, kunci):
        tema = self.tema
        lv = DATA_LEVEL[kunci]
        mulai = lambda: self.mulai_sesi(kunci)

        if self.ringkas:
            # Tampilan HP: satu kolom, tombol MULAI tetap di bawah
            bawah = tk.Frame(self.isi, bg=tema["latar"])
            bawah.pack(side="bottom", fill="x", pady=10)
            TombolBulat(bawah, "MULAI", mulai, 240, 54, tema["latar"],
                        warna_teks=tema["di_atas_merah"], ukuran_font=20,
                        radius=16).pack()

            dalam = self.area_scroll(self.isi)
            self.info(dalam, lv, max(240, self.lebar - 72), 20, (4, 12))
            tk.Label(dalam, text="Panduan Gerakan", fg=tema["teks"], bg=tema["latar"],
                     font=(FONT, 12, "bold"), anchor="w").pack(
                fill="x", padx=22, pady=(0, 6))
            bungkus = max(150, self.lebar - 190)
            for gerak in lv["daftar_gerakan"]:
                self.kartu_gerakan(dalam, kunci, gerak, bungkus, (20, 20))
            tk.Frame(dalam, bg=tema["latar"], height=6).pack()
        else:
            # Tampilan Laptop: kolom kiri (info + MULAI), kolom kanan (gerakan)
            kiri = tk.Frame(self.isi, bg=tema["latar"], width=LEBAR_KOLOM_KIRI)
            kiri.pack(side="left", fill="y", padx=(24, 12), pady=(0, 20))
            kiri.pack_propagate(False)
            self.info(kiri, lv, LEBAR_KOLOM_KIRI - 32, 0, (4, 12))
            jumlah = len(lv["daftar_gerakan"])
            ringkasan = (f"{jumlah} gerakan\n{WAKTU_LATIHAN} detik latihan per gerakan\n"
                         f"{WAKTU_ISTIRAHAT // 60} menit istirahat antar gerakan")
            tk.Label(kiri, text=ringkasan, fg=tema["keterangan"], bg=tema["latar"],
                     font=(FONT, 10), justify="left", anchor="w").pack(fill="x", padx=2)
            TombolBulat(kiri, "MULAI", mulai, LEBAR_KOLOM_KIRI, 58, tema["latar"],
                        warna_teks=tema["di_atas_merah"], ukuran_font=20,
                        radius=16).pack(side="bottom")

            kanan = tk.Frame(self.isi, bg=tema["latar"])
            kanan.pack(side="left", fill="both", expand=True, padx=(12, 24))
            tk.Label(kanan, text="Panduan Gerakan", fg=tema["teks"], bg=tema["latar"],
                     font=(FONT, 13, "bold"), anchor="w").pack(fill="x", pady=(4, 6))
            dalam = self.area_scroll(kanan)
            lebar_kanan = self.lebar - LEBAR_SIDEBAR - LEBAR_KOLOM_KIRI - 24 * 2 - 24
            bungkus = max(160, lebar_kanan - 200)
            for gerak in lv["daftar_gerakan"]:
                self.kartu_gerakan(dalam, kunci, gerak, bungkus, (0, 8))
            tk.Frame(dalam, bg=tema["latar"], height=6).pack()

    def kartu_gerakan(self, induk, level, gerak, bungkus, padx):
        tema = self.tema
        nama, kunci_ikon, singkat, tambahan = gerak
        id_gerak = (level, nama)

        kartu = tk.Frame(induk, bg=tema["kartu"], highlightbackground=KUNING,
                         highlightthickness=1, cursor="hand2")
        kartu.pack(fill="x", padx=padx, pady=5)

        kv_ikon = tk.Canvas(kartu, width=96, height=76, bg=tema["kartu"],
                            highlightthickness=0, cursor="hand2")
        kv_ikon.pack(side="left", padx=(8, 4), pady=10)
        icon_stickman(kv_ikon, kunci_ikon, 0, 0, 0.95, tema)

        kanan = tk.Frame(kartu, bg=tema["kartu"], cursor="hand2")
        kanan.pack(side="left", fill="both", expand=True, padx=(4, 12), pady=10)

        tk.Label(kanan, text=nama, fg=tema["teks"], bg=tema["kartu"],
                 font=(FONT, 13, "bold"), anchor="w", cursor="hand2").pack(fill="x")
        deskripsi = tk.Label(kanan, fg=tema["keterangan"], bg=tema["kartu"],
                             font=(FONT, 9), justify="left", anchor="w",
                             wraplength=bungkus, cursor="hand2")
        deskripsi.pack(fill="x", pady=(2, 2))
        pemicu = tk.Label(kanan, fg=KUNING, bg=tema["kartu"], font=(FONT, 9, "bold"),
                          anchor="w", cursor="hand2")
        pemicu.pack(fill="x")

        def segarkan():
            if self.terbuka.get(id_gerak):
                deskripsi.config(text=singkat + tambahan)
                pemicu.config(text="Tutup \u25B4")
            else:
                deskripsi.config(text=singkat)
                pemicu.config(text="Selengkapnya \u25BE")

        def balik(_e=None):
            self.terbuka[id_gerak] = not self.terbuka.get(id_gerak, False)
            segarkan()

        segarkan()
        for w in (kartu, kv_ikon, kanan, deskripsi, pemicu) + tuple(kanan.winfo_children()):
            w.bind("<Button-1>", balik)

    # --------------------------------------------------------------- timer
    def mulai_sesi(self, kunci):
        self.timer_mati()
        self.sesi = {"tingkat": kunci, "indeks": 0, "fase": "latih",
                     "sisa": WAKTU_LATIHAN, "jalan": True}
        self.halaman = "timer"
        self.gambar_ulang()
        self.pekerjaan = self.after(1000, self._detak)

    def timer(self):
        tema = self.tema
        sesi = self.sesi
        baris = tk.Frame(self.isi, bg=tema["latar"])
        baris.pack(expand=True)

        kiri = tk.Frame(baris, bg=tema["latar"])
        kiri.pack(side="left")
        self.kanvas_timer = tk.Canvas(kiri, width=380, height=440, bg=tema["latar"],
                                      highlightthickness=0)
        self.kanvas_timer.pack(pady=(0, 6))

        deret = tk.Frame(kiri, bg=tema["latar"])
        deret.pack(pady=6)
        dijeda = sesi is not None and not sesi["jalan"]
        self.tombol_jeda = TombolBulat(
            deret, "LANJUT" if dijeda else "JEDA", self.jeda,
            160, 52, tema["latar"], warna_teks=tema["di_atas_merah"], ukuran_font=16)
        self.tombol_jeda.pack(side="left", padx=8)
        TombolBulat(deret, "LEWATI", self.lewati, 160, 52, tema["latar"],
                    isi=tema["latar"], warna_teks=KUNING, garis=KUNING,
                    ukuran_font=16).pack(side="left", padx=8)

        akhiri = tk.Label(kiri, text="Akhiri latihan", fg=tema["keterangan"],
                          bg=tema["latar"], font=(FONT, 11, "underline"),
                          cursor="hand2")
        akhiri.pack(pady=10)
        akhiri.bind("<Button-1>", lambda e: self.sesi())

        # daftar_gerakan gerakan di sisi kanan (khusus tampilan Laptop)
        if not self.ringkas and sesi is not None:
            panel = tk.Frame(baris, bg=tema["kartu"], highlightbackground=KUNING,
                             highlightthickness=1, width=270)
            panel.pack(side="left", anchor="n", padx=(48, 0), pady=40)
            tk.Label(panel, text="Daftar Gerakan", fg=KUNING, bg=tema["kartu"],
                     font=(FONT, 13, "bold"), anchor="w").pack(
                fill="x", padx=18, pady=(16, 8))
            for gerak in DATA_LEVEL[sesi["tingkat"]]["daftar_gerakan"]:
                label = tk.Label(panel, text=gerak[0], bg=tema["kartu"], anchor="w",
                                 font=(FONT, 12), width=22)
                label.pack(fill="x", padx=18, pady=3)
                self.label_langkah.append(label)
            tk.Frame(panel, bg=tema["kartu"], height=12).pack()

        self.gambar_timer()

    def gambar_timer(self):
        kv = self.kanvas_timer
        sesi = self.sesi
        if kv is None or sesi is None or not kv.winfo_exists():
            return
        tema = self.tema
        kv.delete("all")
        lv = DATA_LEVEL[sesi["tingkat"]]
        daftar_gerakan = lv["daftar_gerakan"]
        jumlah = len(daftar_gerakan)
        latihan = sesi["fase"] == "latih"
        durasi = WAKTU_LATIHAN if latihan else WAKTU_ISTIRAHAT
        porsi = max(0.0, sesi["sisa"] / durasi)
        sekarang = daftar_gerakan[sesi["indeks"]]
        berikut = daftar_gerakan[min(sesi["indeks"] + 1, jumlah - 1)]

        kv.create_text(190, 20, fill=tema["keterangan"], font=(FONT, 11, "bold"),
                       text=f"{lv['label']}  \u2022  GERAKAN {sesi['indeks'] + 1} / {jumlah}")
        kv.create_text(190, 56, fill=tema["teks"], font=(FONT, 20, "bold"),
                       text=sekarang[0] if latihan else "Istirahat")

        cx, cy, r = 190, 235, 128
        kotak = (cx - r, cy - r, cx + r, cy + r)
        kv.create_arc(*kotak, start=225, extent=-270, style="arc",
                      outline=tema["jalur"], width=16)
        if porsi > 0:
            kv.create_arc(*kotak, start=225, extent=-270 * porsi, style="arc",
                          outline=KUNING, width=16)

        # ikon gerakan selanjutnya saat istirahat
        icon_stickman(kv, sekarang[1] if latihan else berikut[1],
                    cx - 30, cy - 100, 0.9, tema)

        menit, detik = divmod(max(0, sesi["sisa"]), 60)
        kv.create_text(cx, cy + 28, text=f"{menit:02d}:{detik:02d}", fill=tema["teks"],
                       font=(FONT, 44, "bold"))
        status = "LATIHAN" if latihan else "ISTIRAHAT"
        if not sesi["jalan"]:
            status = "DIJEDA"
        kv.create_text(cx, cy + 74, text=status, fill=KUNING, font=(FONT, 13, "bold"))

        if latihan:
            keterangan = f"Lakukan gerakan selama {WAKTU_LATIHAN} detik"
        else:
            keterangan = f"Selanjutnya: {berikut[0]}"
        kv.create_text(190, 420, fill=tema["keterangan"], font=(FONT, 11),
                       text=keterangan)

        # daftar_gerakan gerakan (tampilan Laptop)
        for i, label in enumerate(self.label_langkah):
            nama = daftar_gerakan[i][0]
            if i < sesi["indeks"]:
                label.config(text=f"\u2713  {nama}", fg=tema["keterangan"],
                             font=(FONT, 12))
            elif i == sesi["indeks"]:
                label.config(text=f"\u25CF  {nama}", fg=KUNING, font=(FONT, 12, "bold"))
            else:
                label.config(text=f"\u25CB  {nama}", fg=tema["teks"], font=(FONT, 12))

    def _detak(self):
        self.pekerjaan = None
        sesi = self.sesi
        if sesi is None:
            return
        if sesi["jalan"]:
            sesi["sisa"] -= 1
            if sesi["sisa"] <= 0:
                self._lanjut_fase()
            elif sesi["sisa"] <= 3:
                self.bell()
        if self.sesi is not None:
            self.gambar_timer()
            self.pekerjaan = self.after(1000, self._detak)

    def _lanjut_fase(self):
        """Pindah fase: latihan -> istirahat -> gerakan berikutnya -> selesai."""
        sesi = self.sesi
        jumlah = len(DATA_LEVEL[sesi["tingkat"]]["daftar_gerakan"])
        self.bell()
        if sesi["fase"] == "latih":
            if sesi["indeks"] >= jumlah - 1:
                self.selesai()
                return
            sesi["fase"], sesi["sisa"] = "rehat", WAKTU_ISTIRAHAT
        else:
            sesi["indeks"] += 1
            sesi["fase"], sesi["sisa"] = "latih", WAKTU_LATIHAN

    def jeda(self):
        sesi = self.sesi
        if sesi is None:
            return
        sesi["jalan"] = not sesi["jalan"]
        if self.tombol_jeda is not None:
            self.tombol_jeda.ubah_teks("JEDA" if sesi["jalan"] else "LANJUT")
        self.gambar_timer()

    def lewati(self):
        if self.sesi is None:
            return
        self._lanjut_fase()
        if self.sesi is not None:
            self.gambar_timer()

    def sesi(self):
        level = self.sesi["tingkat"] if self.sesi else "easy"
        self.timer_mati()
        self.sesi = None
        self.buka(level)

    def selesai(self):
        level = self.sesi["tingkat"]
        self.timer_mati()
        self.sesi = None
        self.buka(level)
        self.pop()

    # --------------------------------------------------------------- popup
    def pop(self):
        tema = self.tema
        window = tk.Toplevel(self)
        window.title("Latihan Selesai")
        window.configure(bg=tema["latar"])
        window.resizable(False, False)
        window.transient(self)
        w, h = 340, 240
        x = self.winfo_x() + (self.winfo_width() - w) // 2
        y = self.winfo_y() + (self.winfo_height() - h) // 2
        window.geometry(f"{w}x{h}+{x}+{y}")

        kotak = tk.Frame(window, bg=tema["kartu"], highlightbackground=KUNING,
                         highlightthickness=2)
        kotak.pack(fill="both", expand=True, padx=10, pady=10)
        tk.Label(kotak, text="Latihan Selesai!", fg=KUNING, bg=tema["kartu"],
                 font=(FONT, 17, "bold")).pack(pady=(22, 10))
        tk.Label(kotak, text=TEKS_POPUP, fg=tema["teks"], bg=tema["kartu"],
                 font=(FONT, 12), wraplength=270, justify="center").pack(padx=16)
        TombolBulat(kotak, "SIAP", window.destroy, 140, 44, tema["kartu"],
                    warna_teks=tema["di_atas_merah"], ukuran_font=15,
                    radius=14).pack(pady=20)
        window.grab_set()


if __name__ == "__main__":
    CaliSphere().mainloop()