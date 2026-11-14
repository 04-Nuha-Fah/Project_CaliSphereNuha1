"""
Project CaliSphere
"""

import math
import os
import tkinter as tk

FOLDER_UTAMA = os.path.dirname(os.path.abspath(__file__))

#Warna dan frame
MERAH = "#B71C1C"
MERAH_DARAH = "#9E1717"
HITAM = "#1A1A1A"
ABU_ABU = "#282828"

TEMA = {
    "light": dict(latar="#EFEFEF", kartu="#FFFFFF", teks=ABU_ABU,
                  keterangan="#5E5E5E", jalur="#D2D2D2", di_atas_merah=ABU_ABU),
    "alat": dict(latar=HITAM, kartu=ABU_ABU, teks="#EFEFEF",
                 keterangan="#A9A9A9", jalur="#3A3A3A", di_atas_merah=ABU_ABU),
}

FONT = "Helvetica"
BATAS_LEBAR = 900
UKURAN_HP = (420, 780)
UKURAN_LAPTOP = (1100, 720)
LEBAR_SIDEBAR = 190
LEBAR_KOLOM_KIRI = 290
WAKTU_LATIHAN = 45
WAKTU_ISTIRAHAT = 120

TEKS_POPUP = "Lakukan latihan ini 4 kali seminggu dan gunakan sisa hari untuk istirahat"

#Tata susunan icon char
IKON = {
    #Mode Easy
    "wall_pushup": dict(alat=[(82, 4, 82, 76)],
                        badan=[(18, 70, 62, 30), (62, 30, 82, 44)],
                        kepala=[(70, 24, 6)]),
    "knee_pushup": dict(badan=[(30, 48, 78, 40), (78, 40, 78, 68),
                             (30, 48, 20, 68), (20, 68, 10, 57)],
                        kepala=[(88, 36, 6)]),
    "squat": dict(badan=[(46, 24, 40, 42), (40, 42, 64, 50), (64, 50, 62, 70),
                       (44, 28, 60, 28)],
                  kepala=[(50, 14, 6)]),
    "lunge": dict(badan=[(50, 24, 50, 48), (50, 48, 68, 54), (68, 54, 72, 70),
                       (50, 48, 26, 70)],
                  kepala=[(50, 14, 6)]),
    "plank": dict(badan=[(12, 66, 74, 54), (74, 54, 74, 68)],
                  kepala=[(86, 50, 6)]),
    #Mode Normal
    "pushup": dict(badan=[(12, 68, 74, 48), (74, 48, 74, 69)],
                   kepala=[(86, 44, 6)]),
    "pullup": dict(alat=[(10, 8, 90, 8)],
                   badan=[(38, 8, 45, 22), (62, 8, 55, 22), (50, 34, 50, 54),
                        (50, 54, 42, 70), (50, 54, 58, 70)],
                   kepala=[(50, 28, 6)]),
    "dips": dict(alat=[(58, 40, 92, 40)],
                 badan=[(36, 28, 38, 56), (38, 32, 58, 40),
                      (38, 56, 30, 70), (38, 56, 46, 70)],
                 kepala=[(34, 18, 6)]),
    "bulgarian": dict(alat=[(70, 64, 92, 64), (70, 64, 70, 70), (92, 64, 92, 70)],
                      badan=[(52, 24, 52, 46), (52, 46, 34, 56), (34, 56, 32, 70),
                           (52, 46, 76, 58), (76, 58, 76, 64)],
                      kepala=[(52, 14, 6)]),
    "pike": dict(badan=[(16, 70, 38, 32), (38, 32, 64, 48), (64, 48, 68, 62)],
                 kepala=[(74, 54, 6)]),
    "adv_plank": dict(badan=[(10, 68, 74, 52), (74, 52, 74, 68), (80, 52, 94, 52)],
                      kepala=[(86, 42, 6)]),
    #Mode hard
    "handstand": dict(badan=[(50, 70, 50, 12), (50, 12, 46, 4), (50, 12, 54, 4)],
                      kepala=[(60, 62, 6)]),
    "archer": dict(badan=[(50, 34, 50, 56), (50, 40, 26, 68), (50, 40, 74, 52),
                        (74, 52, 74, 69), (50, 56, 42, 70), (50, 56, 58, 70)],
                   kepala=[(50, 26, 6)]),
    "human_flag": dict(alat=[(14, 6, 14, 76)],
                       badan=[(16, 28, 30, 38), (16, 50, 30, 38), (30, 38, 92, 38)],
                       kepala=[(36, 32, 6)]),
    "lsit": dict(badan=[(30, 28, 30, 58), (30, 58, 78, 58), (30, 58, 30, 70)],
                 kepala=[(30, 18, 6)]),
    "pistol": dict(badan=[(42, 24, 38, 42), (38, 42, 70, 42), (38, 42, 30, 56),
                        (30, 56, 38, 70), (40, 30, 62, 30)],
                   kepala=[(42, 14, 6)]),
}

TINGKAT = {
    "easy": dict(
        mode="MUDAH", untuk="Pemula",
        catatan=("Kalistenik adalah latihan kebugaran yang memakai berat badan "
              "sendiri sebagai beban, tanpa alat, sehingga bisa dilakukan di "
              "mana saja.\n\nMode Mudah dibuat untuk pemula yang baru mulai "
              "berolahraga. Fokusnya mengenalkan gerakan dasar, membangun "
              "teknik yang benar, dan membentuk kebiasaan latihan."),
        gerakan=[
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
        ]),
    "normal": dict(
        mode="SEDANG", untuk="Terbiasa",
        catatan=("Kalistenik melatih kekuatan, kontrol, dan kelenturan tubuh lewat "
              "gerakan berat badan.\n\nMode Sedang ditujukan bagi kamu yang "
              "sudah pernah berolahraga dan ingin mendalami. Gerakannya "
              "membutuhkan kekuatan dasar yang lebih baik dan teknik yang "
              "lebih rapi."),
        gerakan=[
            ("Pushup", "pushup",
             "Push up standar dengan tubuh lurus, melatih dada, bahu, lengan belakang, dan otot inti sekaligus.",
             " Tangan selebar bahu, tubuh lurus seperti papan. Turunkan dada hingga hampir menyentuh lantai, "
             "siku membentuk sudut sekitar 45 derajat dari tubuh, lalu dorong naik dengan kuat."),
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
        ]),
    "hard": dict(
        mode="SULIT", untuk="Terlatih",
        catatan=("Kalistenik tingkat lanjut menuntut kekuatan, keseimbangan, dan "
              "kontrol tubuh yang tinggi.\n\nMode Sulit hanya untuk kamu yang "
              "sudah sangat berpengalaman. Lakukan pemanasan yang cukup, "
              "perhatikan batas tubuh, dan utamakan keamanan di atas target."),
        gerakan=[
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
        ]),
}
URUTAN_TINGKAT = ["easy", "normal", "hard"]

def round_rect(cv, x1, y1, x2, y2, r, **kw):
    pts = [x1 + r, y1, x2 - r, y1, x2, y1, x2, y1 + r, x2, y2 - r, x2, y2,
           x2 - r, y2, x1 + r, y2, x1, y2, x1, y2 - r, x1, y1 + r, x1, y1]
    return cv.create_polygon(pts, smooth=True, **kw)


class RoundButton(tk.Canvas):
    """Tombol dengan sudut membulat."""

    def __init__(self, parent, text, command, width, height, bg,
                 fill=MERAH, fg=ABU_ABU, outline=None, font_size=18, radius=16):
        super().__init__(parent, width=width, height=height, bg=bg,
                         highlightthickness=0, bd=0, cursor="hand2")
        self.w, self.h, self.r = width, height, radius
        self.text, self.cmd = text, command
        self.fill, self.fg, self.outline = fill, fg, outline
        self.font = (FONT, font_size, "bold")
        self.hover = False
        self.draw() 
        self.bind("<Enter>", lambda e: self._set_hover(True))
        self.bind("<Leave>", lambda e: self._set_hover(False))
        self.bind("<Button-1>", lambda e: self.cmd())

    def _set_hover(self, v):
        self.hover = v
        self.draw()

    def set_text(self, text):
        self.text = text
        self.draw()

    def draw(self):
        self.delete("all")
        fill = self.fill
        if self.hover and fill == MERAH:
            fill = MERAH_DARAH
        round_rect(self, 2, 2, self.w - 2, self.h - 2, self.r, fill=fill,
                   outline=self.outline or fill, width=2)
        self.create_text(self.w / 2, self.h / 2, text=self.text,
                         fill=self.fg, font=self.font)


def draw_icon(cv, key, ox, oy, s, t, w=3):
    """Gambar ikon stick figure pada canvas."""
    ic = IKON[key]
    wd = max(2, int(w * s))
    cv.create_line(ox + 5 * s, oy + 70 * s, ox + 95 * s, oy + 70 * s,
                   fill=t["teks"], width=wd, capstyle="round")
    for x1, y1, x2, y2 in ic.get("alat", []):
        cv.create_line(ox + x1 * s, oy + y1 * s, ox + x2 * s, oy + y2 * s,
                       fill=t["teks"], width=wd, capstyle="round")
    for x1, y1, x2, y2 in ic["badan"]:
        cv.create_line(ox + x1 * s, oy + y1 * s, ox + x2 * s, oy + y2 * s,
                       fill=MERAH, width=wd, capstyle="round", joinstyle="round")
    for x, y, r in ic["kepala"]:
        cv.create_oval(ox + (x - r) * s, oy + (y - r) * s,
                       ox + (x + r) * s, oy + (y + r) * s,
                       fill=MERAH, outline=MERAH)


# ----------------------------------------------------------------------------
# Aplikasi utama
# ----------------------------------------------------------------------------
class CaliSphere(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CaliSphere")
        self._set_app_icon()
        self.geometry(f"{UKURAN_LAPTOP[0]}x{UKURAN_LAPTOP[1]}")
        self.minsize(380, 640)

        self.mode = "light"
        self.page = "home"
        self.compact = False
        self.W = UKURAN_LAPTOP[0]
        self.expanded = {}
        self.session = None
        self.job = None
        self.scroll_cv = None
        self.timer_cv = None
        self.pause_btn = None
        self.step_labels = []
        self._last_size = None
        self._resize_job = None

        self.bind_all("<MouseWheel>", self._on_wheel)
        self.bind_all("<Button-4>", self._on_wheel)
        self.bind_all("<Button-5>", self._on_wheel)
        self.bind("<Configure>", self._on_configure)
        self.protocol("WM_DELETE_WINDOW", self._close)
        self.render()

    def _set_app_icon(self):
        """Pasang ikon aplikasi dari icon.png (icon.ico dipakai di Windows bila
        ada). Gambar juga disimpan di self.logo untuk logo di dalam UI."""
        self.logo = None
        ico = os.path.join(FOLDER_UTAMA, "icon.ico")
        png = os.path.join(FOLDER_UTAMA, "icon.png")
        try:
            if os.path.exists(png):
                self.logo = tk.PhotoImage(file=png)       # simpan referensinya
        except tk.TclError:
            self.logo = None
        try:
            if os.name == "nt" and os.path.exists(ico):
                self.iconbitmap(ico)
            elif self.logo is not None:
                self.iconphoto(True, self.logo)
        except tk.TclError:
            pass

    def _logo_image(self, size):
        """Kembalikan logo yang diperkecil agar sisi terpanjangnya ~size px."""
        if self.logo is None:
            return None
        f = max(1, round(max(self.logo.width(), self.logo.height()) / size))
        return self.logo.subsample(f, f) if f > 1 else self.logo

    def _logo_label(self, parent, bg, size, **pack):
        """Tampilkan logo berukuran `size` px bila tersedia."""
        img = self._logo_image(size)
        if img is None:
            return None
        lbl = tk.Label(parent, image=img, bg=bg, bd=0)
        lbl.image = img
        lbl.pack(**pack)
        return lbl

    @property
    def t(self):
        return TEMA[self.mode]

    # ------------------------------------------------------------- umum
    def _close(self):
        self._cancel_job()
        self.destroy()

    def _cancel_job(self):
        if self.job is not None:
            try:
                self.after_cancel(self.job)
            except Exception:
                pass
            self.job = None

    def _on_wheel(self, e):
        cv = self.scroll_cv
        if cv is None or not cv.winfo_exists():
            return
        if cv.yview() == (0.0, 1.0):
            return
        if e.num == 4:
            d = -1
        elif e.num == 5:
            d = 1
        else:
            d = -1 if e.delta > 0 else 1
        cv.yview_scroll(d * 2, "units")

    def _on_configure(self, e):
        """Jendela diubah ukurannya -> susun ulang (HP <-> Laptop)."""
        if e.widget is not self:
            return
        if (e.width, e.height) == self._last_size:
            return
        self._last_size = (e.width, e.height)
        if self._resize_job is not None:
            self.after_cancel(self._resize_job)
        self._resize_job = self.after(200, self._on_resized)

    def _on_resized(self):
        self._resize_job = None
        self.render()

    def toggle_mode(self):
        self.mode = "alat" if self.mode == "light" else "light"
        self.render()

    def toggle_layout(self):
        """Pindah paksa antara ukuran HP dan ukuran Laptop."""
        w, h = UKURAN_LAPTOP if self.compact else UKURAN_HP
        self.geometry(f"{w}x{h}")

    def goto(self, page):
        self.page = page
        self.render()

    # ------------------------------------------------------------ render
    def render(self):
        t = self.t
        self.update_idletasks()
        w = self.winfo_width()
        if w <= 1:
            w = UKURAN_LAPTOP[0]
        self.W = w
        self.compact = w < BATAS_LEBAR

        self.configure(bg=t["latar"])
        for ch in self.winfo_children():
            if not isinstance(ch, tk.Toplevel):
                ch.destroy()
        self.scroll_cv = None
        self.timer_cv = None
        self.pause_btn = None
        self.step_labels = []

        if self.compact:
            body = self
            self._build_header(body)
            if self.page != "timer":
                self._build_nav_bottom()
        else:
            if self.page != "timer":
                self._build_sidebar()
            body = tk.Frame(self, bg=t["latar"])
            body.pack(side="left", fill="both", expand=True)
            self._build_header(body)

        self.content = tk.Frame(body, bg=t["latar"])
        self.content.pack(fill="both", expand=True)

        if self.page == "home":
            self._build_home()
        elif self.page == "timer":
            self._build_timer()
        else:
            self._build_level(self.page)

    # ------------------------------------------------------------ header
    def _build_header(self, parent):
        t = self.t
        bar = tk.Frame(parent, bg=t["latar"], height=56)
        bar.pack(side="top", fill="x")
        bar.pack_propagate(False)

        show_title = ((self.compact and self.page != "home") or
                      (not self.compact and self.page == "timer"))
        if show_title:
            ic = self._logo_label(bar, t["latar"], 32, side="left", padx=(16, 0))
            if ic is not None:
                ic.config(cursor="hand2")
                ic.bind("<Button-1>", lambda e: self.goto("home"))
            lbl = tk.Label(bar, text="CaliSphere", fg=MERAH, bg=t["latar"],
                           font=(FONT, 16, "bold"), cursor="hand2")
            lbl.pack(side="left", padx=(8, 18))
            lbl.bind("<Button-1>", lambda e: self.goto("home"))

        # tombol mode terang / gelap (kanan atas)
        cv = tk.Canvas(bar, width=36, height=36, bg=t["latar"],
                       highlightthickness=0, cursor="hand2")
        cv.pack(side="right", padx=(8, 16), pady=10)
        if self.mode == "light":      # ikon matahari
            cv.create_oval(11, 11, 25, 25, fill=MERAH, outline=MERAH)
            for i in range(8):
                a = math.radians(i * 45)
                cv.create_line(18 + 11 * math.cos(a), 18 + 11 * math.sin(a),
                               18 + 15 * math.cos(a), 18 + 15 * math.sin(a),
                               fill=MERAH, width=3, capstyle="round")
        else:                         # ikon bulan
            cv.create_oval(5, 5, 31, 31, fill=MERAH, outline=MERAH)
            cv.create_oval(13, 0, 38, 24, fill=t["latar"], outline=t["latar"])
        cv.bind("<Button-1>", lambda e: self.toggle_mode())

        # tombol ganti tampilan HP <-> Laptop (menampilkan ikon tujuan)
        lv = tk.Canvas(bar, width=36, height=36, bg=t["latar"],
                       highlightthickness=0, cursor="hand2")
        lv.pack(side="right", pady=10)
        if self.compact:              # tujuan: laptop
            lv.create_rectangle(7, 9, 29, 24, outline=MERAH, width=2)
            lv.create_line(3, 28, 33, 28, fill=MERAH, width=3, capstyle="round")
        else:                         # tujuan: HP
            round_rect(lv, 10, 4, 26, 32, 4, fill=t["latar"], outline=MERAH, width=2)
            lv.create_line(15, 27, 21, 27, fill=MERAH, width=2, capstyle="round")
        lv.bind("<Button-1>", lambda e: self.toggle_layout())

    # ---------------------------------------------- navigasi (tampilan HP)
    def _build_nav_bottom(self):
        t = self.t
        nav = tk.Frame(self, bg=t["latar"])
        nav.pack(side="bottom", fill="x")
        tk.Frame(nav, bg=t["jalur"], height=1).pack(fill="x")
        row = tk.Frame(nav, bg=t["latar"])
        row.pack(fill="x", pady=(0, 10))
        for key in URUTAN_TINGKAT:
            active = (self.page == key)
            col = tk.Frame(row, bg=t["latar"], cursor="hand2")
            col.pack(side="left", expand=True, fill="x")
            tk.Frame(col, height=5, bg=MERAH if active else t["latar"]).pack(
                fill="x", padx=36)
            lbl = tk.Label(col, text=TINGKAT[key]["mode"], bg=t["latar"],
                           fg=MERAH if active else t["teks"],
                           font=(FONT, 15, "bold" if active else "normal"),
                           cursor="hand2")
            lbl.pack(pady=(8, 4))
            for w in (col, lbl):
                w.bind("<Button-1>", lambda e, k=key: self.goto(k))

    # --------------------------------------------- navigasi (tampilan Laptop)
    def _build_sidebar(self):
        t = self.t
        side = tk.Frame(self, bg=t["kartu"], width=LEBAR_SIDEBAR)
        side.pack(side="left", fill="y")
        side.pack_propagate(False)

        logo = self._logo_label(side, t["kartu"], 64, anchor="w",
                                padx=20, pady=(20, 0))
        if logo is not None:
            logo.config(cursor="hand2")
            logo.bind("<Button-1>", lambda e: self.goto("home"))
        title = tk.Label(side, text="CaliSphere", fg=MERAH, bg=t["kartu"],
                         font=(FONT, 20, "bold"), cursor="hand2")
        title.pack(anchor="w", padx=20, pady=(8 if logo else 24, 0))
        title.bind("<Button-1>", lambda e: self.goto("home"))
        tk.Label(side, text="Kalistenik untuk hidup sehat", fg=t["keterangan"],
                 bg=t["kartu"], font=(FONT, 9), anchor="w", justify="left",
                 wraplength=LEBAR_SIDEBAR - 40).pack(anchor="w", padx=20,
                                                 pady=(2, 28))

        for key in URUTAN_TINGKAT:
            active = (self.page == key)
            row = tk.Frame(side, bg=t["kartu"], cursor="hand2")
            row.pack(fill="x", pady=3)
            tk.Frame(row, width=5, bg=MERAH if active else t["kartu"]).pack(
                side="left", fill="y")
            txt = tk.Frame(row, bg=t["kartu"], cursor="hand2")
            txt.pack(side="left", fill="x", padx=(16, 0), pady=8)
            l1 = tk.Label(txt, text=TINGKAT[key]["mode"], bg=t["kartu"],
                          fg=MERAH if active else t["teks"], cursor="hand2",
                          font=(FONT, 15, "bold" if active else "normal"))
            l1.pack(anchor="w")
            l2 = tk.Label(txt, text=TINGKAT[key]["untuk"], bg=t["kartu"],
                          fg=t["keterangan"], font=(FONT, 9), cursor="hand2")
            l2.pack(anchor="w")
            for w in (row, txt, l1, l2):
                w.bind("<Button-1>", lambda e, k=key: self.goto(k))

    # -------------------------------------------------------------- home
    def _build_home(self):
        t = self.t
        big = not self.compact
        box = tk.Frame(self.content, bg=t["latar"])
        box.pack(expand=True)

        self._logo_label(box, t["latar"], 128 if big else 96, pady=(0, 10))
        tk.Label(box, text="CaliSphere", fg=MERAH, bg=t["latar"],
                 font=(FONT, 46 if big else 34, "bold")).pack(pady=(0, 6))
        tk.Label(box, text="Pemandu hidup sehat dengan olahraga kalistenik"
                 if big else "Pemandu hidup sehat dengan\nolahraga kalistenik",
                 fg=t["keterangan"], bg=t["latar"], font=(FONT, 14 if big else 12),
                 justify="center").pack(pady=(0, 34 if big else 30))

        row = tk.Frame(box, bg=t["latar"])
        row.pack(pady=(0, 40 if big else 36))
        sample = {"easy": "squat", "normal": "pullup", "hard": "handstand"}
        s = 1.35 if big else 1.0
        for key in URUTAN_TINGKAT:
            col = tk.Frame(row, bg=t["latar"])
            col.pack(side="left", padx=18 if big else 6)
            cv = tk.Canvas(col, width=int(100 * s), height=int(80 * s),
                           bg=t["latar"], highlightthickness=0)
            cv.pack()
            draw_icon(cv, sample[key], 0, 0, s, t)
            lv = TINGKAT[key]
            tk.Label(col, text=lv["mode"].title(), fg=t["teks"], bg=t["latar"],
                     font=(FONT, 11 if big else 10, "bold")).pack()
            tk.Label(col, text=f"({lv['untuk']})", fg=t["keterangan"], bg=t["latar"],
                     font=(FONT, 10 if big else 9)).pack()

        RoundButton(box, "AYO LATIHAN", lambda: self.goto("easy"),
                    320 if big else 260, 68 if big else 62, t["latar"],
                    fg=t["di_atas_merah"], font_size=22 if big else 20,
                    radius=18).pack()

    # ------------------------------------------------------- halaman level
    def _make_scroll(self, parent):
        t = self.t
        wrap = tk.Frame(parent, bg=t["latar"])
        wrap.pack(side="top", fill="both", expand=True)
        cv = tk.Canvas(wrap, bg=t["latar"], highlightthickness=0, bd=0)
        cv.pack(fill="both", expand=True)
        inner = tk.Frame(cv, bg=t["latar"])
        win = cv.create_window((0, 0), window=inner, anchor="nw")
        inner.bind("<Configure>",
                   lambda e: cv.configure(scrollregion=cv.bbox("all")))
        cv.bind("<Configure>", lambda e: cv.itemconfigure(win, width=e.width))
        self.scroll_cv = cv
        return inner

    def _info_card(self, parent, lv, wrap, padx, pady):
        t = self.t
        catatan = tk.Frame(parent, bg=t["kartu"], highlightbackground=MERAH,
                        highlightthickness=1)
        catatan.pack(fill="x", padx=padx, pady=pady)
        tk.Label(catatan, text=f"Mode {lv['mode'].title()} ({lv['untuk']})",
                 fg=MERAH, bg=t["kartu"], font=(FONT, 14, "bold"),
                 anchor="w").pack(fill="x", padx=14, pady=(12, 4))
        tk.Label(catatan, text=lv["catatan"], fg=t["teks"], bg=t["kartu"],
                 font=(FONT, 10), justify="left", anchor="w",
                 wraplength=wrap).pack(fill="x", padx=14, pady=(0, 12))

    def _build_level(self, key):
        t = self.t
        lv = TINGKAT[key]
        start = lambda: self.start_session(key)

        if self.compact:
            # ---- Tampilan HP: satu kolom, tombol MULAI tetap di bawah
            bottom = tk.Frame(self.content, bg=t["latar"])
            bottom.pack(side="bottom", fill="x", pady=10)
            RoundButton(bottom, "MULAI", start, 240, 54, t["latar"],
                        fg=t["di_atas_merah"], font_size=20, radius=16).pack()

            inner = self._make_scroll(self.content)
            self._info_card(inner, lv, max(240, self.W - 72), 20, (4, 12))
            tk.Label(inner, text="Panduan Gerakan", fg=t["teks"], bg=t["latar"],
                     font=(FONT, 12, "bold"), anchor="w").pack(
                fill="x", padx=22, pady=(0, 6))
            wrap = max(150, self.W - 190)
            for ex in lv["gerakan"]:
                self._exercise_card(inner, key, ex, wrap, (20, 20))
            tk.Frame(inner, bg=t["latar"], height=6).pack()
        else:
            # ---- Tampilan Laptop: kolom kiri (catatan + MULAI), kolom kanan (gerakan)
            left = tk.Frame(self.content, bg=t["latar"], width=LEBAR_KOLOM_KIRI)
            left.pack(side="left", fill="y", padx=(24, 12), pady=(0, 20))
            left.pack_propagate(False)
            self._info_card(left, lv, LEBAR_KOLOM_KIRI - 32, 0, (4, 12))
            n = len(lv["gerakan"])
            tk.Label(left, fg=t["keterangan"], bg=t["latar"], font=(FONT, 10),
                     justify="left", anchor="w",
                     text=f"{n} gerakan\n{WAKTU_LATIHAN} detik latihan per gerakan\n"
                          f"{WAKTU_ISTIRAHAT // 60} menit istirahat antar gerakan"
                     ).pack(fill="x", padx=2)
            RoundButton(left, "MULAI", start, LEBAR_KOLOM_KIRI, 58, t["latar"],
                        fg=t["di_atas_merah"], font_size=20, radius=16).pack(
                side="bottom")

            right = tk.Frame(self.content, bg=t["latar"])
            right.pack(side="left", fill="both", expand=True,
                       padx=(12, 24))
            tk.Label(right, text="Panduan Gerakan", fg=t["teks"], bg=t["latar"],
                     font=(FONT, 13, "bold"), anchor="w").pack(
                fill="x", pady=(4, 6))
            inner = self._make_scroll(right)
            right_w = self.W - LEBAR_SIDEBAR - LEBAR_KOLOM_KIRI - 24 * 2 - 24
            wrap = max(160, right_w - 200)
            for ex in lv["gerakan"]:
                self._exercise_card(inner, key, ex, wrap, (0, 8))
            tk.Frame(inner, bg=t["latar"], height=6).pack()

    def _exercise_card(self, parent, level, ex, wrap, padx):
        t = self.t
        name, icon, short, extra = ex
        ident = (level, name)

        card = tk.Frame(parent, bg=t["kartu"], highlightbackground=MERAH,
                        highlightthickness=1, cursor="hand2")
        card.pack(fill="x", padx=padx, pady=5)

        icv = tk.Canvas(card, width=96, height=76, bg=t["kartu"],
                        highlightthickness=0, cursor="hand2")
        icv.pack(side="left", padx=(8, 4), pady=10)
        draw_icon(icv, icon, 0, 0, 0.95, t)

        right = tk.Frame(card, bg=t["kartu"], cursor="hand2")
        right.pack(side="left", fill="both", expand=True, padx=(4, 12), pady=10)

        tk.Label(right, text=name, fg=t["teks"], bg=t["kartu"],
                 font=(FONT, 13, "bold"), anchor="w", cursor="hand2").pack(
            fill="x")
        desc = tk.Label(right, fg=t["keterangan"], bg=t["kartu"], font=(FONT, 9),
                        justify="left", anchor="w", wraplength=wrap,
                        cursor="hand2")
        desc.pack(fill="x", pady=(2, 2))
        tog = tk.Label(right, fg=MERAH, bg=t["kartu"], font=(FONT, 9, "bold"),
                       anchor="w", cursor="hand2")
        tog.pack(fill="x")

        def refresh():
            if self.expanded.get(ident):
                desc.config(text=short + extra)
                tog.config(text="Tutup \u25B4")
            else:
                desc.config(text=short)
                tog.config(text="Selengkapnya \u25BE")

        def toggle(_e=None):
            self.expanded[ident] = not self.expanded.get(ident, False)
            refresh()

        refresh()
        for w in (card, icv, right, desc, tog) + tuple(right.winfo_children()):
            w.bind("<Button-1>", toggle)

    # --------------------------------------------------------------- timer
    def start_session(self, key):
        self._cancel_job()
        self.session = dict(level=key, idx=0, phase="work",
                            remaining=WAKTU_LATIHAN, running=True)
        self.page = "timer"
        self.render()
        self.job = self.after(1000, self._tick)

    def _build_timer(self):
        t = self.t
        s = self.session
        row = tk.Frame(self.content, bg=t["latar"])
        row.pack(expand=True)

        left = tk.Frame(row, bg=t["latar"])
        left.pack(side="left")
        self.timer_cv = tk.Canvas(left, width=380, height=440, bg=t["latar"],
                                  highlightthickness=0)
        self.timer_cv.pack(pady=(0, 6))

        btns = tk.Frame(left, bg=t["latar"])
        btns.pack(pady=6)
        paused = s is not None and not s["running"]
        self.pause_btn = RoundButton(
            btns, "LANJUT" if paused else "JEDA", self._toggle_pause,
            160, 52, t["latar"], fg=t["di_atas_merah"], font_size=16)
        self.pause_btn.pack(side="left", padx=8)
        RoundButton(btns, "LEWATI", self._skip, 160, 52, t["latar"],
                    fill=t["latar"], fg=MERAH, outline=MERAH,
                    font_size=16).pack(side="left", padx=8)

        end = tk.Label(left, text="Akhiri latihan", fg=t["keterangan"], bg=t["latar"],
                       font=(FONT, 11, "underline"), cursor="hand2")
        end.pack(pady=10)
        end.bind("<Button-1>", lambda e: self._end_session())

        # daftar gerakan di sisi kanan (khusus tampilan Laptop)
        if not self.compact and s is not None:
            panel = tk.Frame(row, bg=t["kartu"], highlightbackground=MERAH,
                             highlightthickness=1, width=270)
            panel.pack(side="left", anchor="n", padx=(48, 0), pady=40)
            tk.Label(panel, text="Daftar Gerakan", fg=MERAH, bg=t["kartu"],
                     font=(FONT, 13, "bold"), anchor="w").pack(
                fill="x", padx=18, pady=(16, 8))
            for ex in TINGKAT[s["level"]]["gerakan"]:
                lbl = tk.Label(panel, text=ex[0], bg=t["kartu"], anchor="w",
                               font=(FONT, 12), width=22)
                lbl.pack(fill="x", padx=18, pady=3)
                self.step_labels.append(lbl)
            tk.Frame(panel, bg=t["kartu"], height=12).pack()

        self.draw_timer()

    def draw_timer(self):
        cv = self.timer_cv
        s = self.session
        if cv is None or s is None or not cv.winfo_exists():
            return
        t = self.t
        cv.delete("all")
        lv = TINGKAT[s["level"]]
        exs = lv["gerakan"]
        n = len(exs)
        work = s["phase"] == "work"
        total = WAKTU_LATIHAN if work else WAKTU_ISTIRAHAT
        frac = max(0.0, s["remaining"] / total)
        cur = exs[s["idx"]]

if __name__ == "__main__":
    CaliSphere().mainloop()
