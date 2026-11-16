"""
CaliSphere - Pemandu hidup sehat dengan olahraga kalistenik
GUI minimalis berbasis Tkinter (Python 3, tanpa library tambahan)
Responsif: tampilan HP (jendela sempit) dan tampilan Laptop (jendela lebar)

Jalankan:  python calisphere.py
"""
import math
import os
import tkinter as tk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------------------
# Konfigurasi
# ----------------------------------------------------------------------------
RED = "#B71C1C"
RED_HOVER = "#9E1717"
DARK_1 = "#1A1A1A"
DARK_2 = "#282828"

THEMES = {
    "light": dict(bg="#EFEFEF", card="#FFFFFF", text=DARK_2,
                  sub="#5E5E5E", track="#D2D2D2", on_red=DARK_2),
    "dark": dict(bg=DARK_1, card=DARK_2, text="#EFEFEF",
                 sub="#A9A9A9", track="#3A3A3A", on_red=DARK_2),
}

FONT = "Helvetica"
BREAKPOINT = 900             # lebar jendela < 900 px -> tampilan HP, selain itu -> laptop
PHONE_SIZE = (420, 780)
DESKTOP_SIZE = (1100, 720)
SIDEBAR_W = 190              # lebar sidebar (tampilan laptop)
LEFT_COL_W = 290             # lebar kolom kiri halaman level (tampilan laptop)
WORK_SEC = 45        # durasi tiap gerakan (detik)
REST_SEC = 120       # durasi istirahat antar gerakan (detik)

POPUP_TEXT = "Lakukan latihan ini 4 kali seminggu dan gunakan sisa hari untuk istirahat"

# ----------------------------------------------------------------------------
# Ikon gerakan (stick figure) - koordinat pada kotak 100 x 80
#   red  = garis tubuh, dark = garis pendukung (tembok, bar, bangku)
#   dots = kepala (x, y, radius)
# ----------------------------------------------------------------------------
ICONS = {
    "wall_pushup": dict(dark=[(82, 4, 82, 76)],
                        red=[(18, 70, 62, 30), (62, 30, 82, 44)],
                        dots=[(70, 24, 6)]),
    "knee_pushup": dict(red=[(30, 48, 78, 40), (78, 40, 78, 68),
                             (30, 48, 20, 68), (20, 68, 10, 57)],
                        dots=[(88, 36, 6)]),
    "squat": dict(red=[(46, 24, 40, 42), (40, 42, 64, 50), (64, 50, 62, 70),
                       (44, 28, 60, 28)],
                  dots=[(50, 14, 6)]),
    "lunge": dict(red=[(50, 24, 50, 48), (50, 48, 68, 54), (68, 54, 72, 70),
                       (50, 48, 26, 70)],
                  dots=[(50, 14, 6)]),
    "plank": dict(red=[(12, 66, 74, 54), (74, 54, 74, 68)],
                  dots=[(86, 50, 6)]),
    "pushup": dict(red=[(12, 68, 74, 48), (74, 48, 74, 69)],
                   dots=[(86, 44, 6)]),
    "pullup": dict(dark=[(10, 8, 90, 8)],
                   red=[(38, 8, 45, 22), (62, 8, 55, 22), (50, 34, 50, 54),
                        (50, 54, 42, 70), (50, 54, 58, 70)],
                   dots=[(50, 28, 6)]),
    "dips": dict(dark=[(58, 40, 92, 40)],
                 red=[(36, 28, 38, 56), (38, 32, 58, 40),
                      (38, 56, 30, 70), (38, 56, 46, 70)],
                 dots=[(34, 18, 6)]),
    "bulgarian": dict(dark=[(70, 64, 92, 64), (70, 64, 70, 70), (92, 64, 92, 70)],
                      red=[(52, 24, 52, 46), (52, 46, 34, 56), (34, 56, 32, 70),
                           (52, 46, 76, 58), (76, 58, 76, 64)],
                      dots=[(52, 14, 6)]),
    "pike": dict(red=[(16, 70, 38, 32), (38, 32, 64, 48), (64, 48, 68, 62)],
                 dots=[(74, 54, 6)]),
    "adv_plank": dict(red=[(10, 68, 74, 52), (74, 52, 74, 68), (80, 52, 94, 52)],
                      dots=[(86, 42, 6)]),
    "handstand": dict(red=[(50, 70, 50, 12), (50, 12, 46, 4), (50, 12, 54, 4)],
                      dots=[(60, 62, 6)]),
    "archer": dict(red=[(50, 34, 50, 56), (50, 40, 26, 68), (50, 40, 74, 52),
                        (74, 52, 74, 69), (50, 56, 42, 70), (50, 56, 58, 70)],
                   dots=[(50, 26, 6)]),
    "human_flag": dict(dark=[(14, 6, 14, 76)],
                       red=[(16, 28, 30, 38), (16, 50, 30, 38), (30, 38, 92, 38)],
                       dots=[(36, 32, 6)]),
    "lsit": dict(red=[(30, 28, 30, 58), (30, 58, 78, 58), (30, 58, 30, 70)],
                 dots=[(30, 18, 6)]),
    "pistol": dict(red=[(42, 24, 38, 42), (38, 42, 70, 42), (38, 42, 30, 56),
                        (30, 56, 38, 70), (40, 30, 62, 30)],
                   dots=[(42, 14, 6)]),
}

# ----------------------------------------------------------------------------
# Data latihan
# ----------------------------------------------------------------------------
LEVELS = {
    "easy": dict(
        label="EASY", sub="Pemula",
        info=("Kalistenik adalah latihan kebugaran yang memakai berat badan "
              "sendiri sebagai beban, tanpa alat, sehingga bisa dilakukan di "
              "mana saja.\n\nMode Easy dibuat untuk pemula yang baru mulai "
              "berolahraga. Fokusnya mengenalkan gerakan dasar, membangun "
              "teknik yang benar, dan membentuk kebiasaan latihan."),
        exercises=[
            ("Wall Push Up", "wall_pushup",
             "Push up berdiri menghadap tembok. Gerakan paling ringan untuk melatih dada, bahu, dan trisep.",
             " Berdirilah satu langkah dari tembok, letakkan telapak tangan di dinding setinggi bahu. "
             "Tekuk siku hingga dada mendekati tembok, lalu dorong kembali. Jaga tubuh tetap lurus dan perut mengencang."),
            ("Knee Push Up", "knee_pushup",
             "Push up dengan lutut menempel di lantai untuk membangun kekuatan tubuh bagian atas.",
             " Posisikan tangan selebar bahu, lutut di lantai, tubuh lurus dari kepala hingga lutut. "
             "Turunkan dada mendekati lantai, lalu dorong naik. Jangan biarkan pinggul turun atau menungging."),
            ("Squat", "squat",
             "Gerakan jongkok dasar untuk melatih paha, bokong, dan kestabilan tubuh.",
             " Berdiri selebar bahu, dorong pinggul ke belakang seperti duduk di kursi. "
             "Turunkan badan hingga paha hampir sejajar lantai, dada tetap tegak, lalu berdiri kembali dengan menekan tumit."),
            ("Lunge", "lunge",
             "Melangkah ke depan lalu menekuk lutut, melatih kaki satu sisi dan keseimbangan.",
             " Langkahkan satu kaki ke depan, turunkan badan hingga kedua lutut menekuk sekitar 90 derajat. "
             "Lutut depan tidak melewati ujung kaki. Dorong kembali ke posisi awal dan ganti kaki."),
            ("Plank", "plank",
             "Menahan tubuh lurus bertumpu pada lengan bawah untuk melatih otot inti (core).",
             " Letakkan siku tepat di bawah bahu, tubuh lurus dari kepala hingga tumit. "
             "Kencangkan perut dan bokong, pandangan ke lantai, dan bernapas normal selama menahan posisi."),
        ]),
    "normal": dict(
        label="NORMAL", sub="Terbiasa",
        info=("Kalistenik melatih kekuatan, kontrol, dan mobilitas tubuh lewat "
              "gerakan berat badan.\n\nMode Normal ditujukan bagi kamu yang "
              "sudah pernah berolahraga dan ingin mendalami. Gerakannya "
              "membutuhkan kekuatan dasar yang lebih baik dan teknik yang "
              "lebih rapi."),
        exercises=[
            ("Regular Push Up", "pushup",
             "Push up standar dengan tubuh lurus, melatih dada, bahu, trisep, dan core sekaligus.",
             " Tangan selebar bahu, tubuh lurus seperti papan. Turunkan dada hingga hampir menyentuh lantai, "
             "siku membentuk sudut sekitar 45 derajat dari tubuh, lalu dorong naik dengan kuat."),
            ("Pull Up", "pullup",
             "Menarik tubuh ke atas hingga dagu melewati bar. Melatih punggung dan bisep.",
             " Pegang bar dengan genggaman sedikit lebih lebar dari bahu. Tarik dengan menggerakkan siku ke bawah, "
             "hindari mengayun. Turunkan perlahan hingga lengan lurus sebelum mengulang."),
            ("Dips", "dips",
             "Menurunkan dan mendorong tubuh di antara dua tumpuan. Melatih trisep, dada bawah, dan bahu.",
             " Gunakan parallel bar atau dua kursi kokoh. Tekuk siku hingga bahu sejajar siku, "
             "lalu dorong naik. Jaga bahu tetap turun dan dada sedikit condong ke depan."),
            ("Bulgarian Split Squat", "bulgarian",
             "Squat satu kaki dengan kaki belakang bertumpu di bangku. Melatih paha, bokong, dan keseimbangan.",
             " Letakkan punggung kaki belakang di bangku, kaki depan melangkah cukup jauh. "
             "Turunkan badan hingga paha depan sejajar lantai, lalu naik. Selesaikan satu sisi sebelum ganti kaki."),
            ("Pike Push Up", "pike",
             "Push up dengan pinggul diangkat membentuk huruf V terbalik. Fokus pada bahu.",
             " Mulai dari posisi V terbalik, kaki dan tangan tetap di lantai. Tekuk siku hingga kepala mendekati lantai "
             "di antara kedua tangan, lalu dorong naik. Ini persiapan menuju handstand push up."),
            ("Advanced Plank", "adv_plank",
             "Variasi plank yang lebih berat, misalnya dengan mengangkat satu kaki atau tangan bergantian.",
             " Mulai dari posisi plank, lalu angkat satu kaki atau satu tangan tanpa memutar pinggul. "
             "Tahan beberapa detik, ganti sisi. Pertahankan perut mengencang dan tubuh tetap lurus."),
        ]),
    "hard": dict(
        label="HARD", sub="Terlatih",
        info=("Kalistenik tingkat lanjut menuntut kekuatan, keseimbangan, dan "
              "kontrol tubuh yang tinggi.\n\nMode Hard hanya untuk kamu yang "
              "sudah sangat berpengalaman. Lakukan pemanasan yang cukup, "
              "perhatikan batas tubuh, dan utamakan keamanan di atas target."),
        exercises=[
            ("Handstand", "handstand",
             "Berdiri dengan bertumpu pada kedua tangan. Melatih bahu, core, dan keseimbangan.",
             " Mulai dekat tembok untuk bantuan. Tangan selebar bahu, dorong lantai dengan kuat, "
             "tubuh lurus dari tangan hingga ujung kaki. Pandangan ke arah ujung jari."),
            ("Archer Push Up", "archer",
             "Push up dengan satu lengan lurus ke samping, langkah menuju one arm push up.",
             " Posisi tangan lebar. Turunkan badan ke satu sisi sementara lengan sisi lain tetap lurus. "
             "Dorong kembali ke tengah lalu ganti sisi. Beban utama ada di lengan yang menekuk."),
            ("Human Flag", "human_flag",
             "Menahan tubuh horizontal di sebuah tiang. Salah satu gerakan kalistenik paling sulit.",
             " Pegang tiang dengan satu tangan di atas dan satu di bawah. Dorong tangan bawah, tarik tangan atas, "
             "lalu angkat tubuh sejajar lantai. Butuh kekuatan core dan bahu yang sangat kuat."),
            ("L Pose (L-Sit)", "lsit",
             "Menahan tubuh di atas tangan dengan kaki lurus ke depan membentuk huruf L.",
             " Tekan lantai atau parallel bar dengan kedua tangan hingga pinggul terangkat. "
             "Kaki tetap lurus dan sejajar lantai. Kencangkan perut dan dorong bahu ke bawah."),
            ("Pistol Squat", "pistol",
             "Squat satu kaki penuh dengan kaki lainnya lurus ke depan. Melatih kekuatan, mobilitas, dan kontrol.",
             " Berdiri satu kaki, luruskan kaki lainnya ke depan. Turunkan badan hingga bokong hampir menyentuh tumit, "
             "tumit tetap menempel lantai, lalu berdiri kembali. Gunakan pegangan jika perlu."),
        ]),
}
LEVEL_ORDER = ["easy", "normal", "hard"]


# ----------------------------------------------------------------------------
# Komponen UI
# ----------------------------------------------------------------------------
def round_rect(cv, x1, y1, x2, y2, r, **kw):
    pts = [x1 + r, y1, x2 - r, y1, x2, y1, x2, y1 + r, x2, y2 - r, x2, y2,
           x2 - r, y2, x1 + r, y2, x1, y2, x1, y2 - r, x1, y1 + r, x1, y1]
    return cv.create_polygon(pts, smooth=True, **kw)


class RoundButton(tk.Canvas):
    """Tombol dengan sudut membulat."""

    def __init__(self, parent, text, command, width, height, bg,
                 fill=RED, fg=DARK_2, outline=None, font_size=18, radius=16):
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
        if self.hover and fill == RED:
            fill = RED_HOVER
        round_rect(self, 2, 2, self.w - 2, self.h - 2, self.r, fill=fill,
                   outline=self.outline or fill, width=2)
        self.create_text(self.w / 2, self.h / 2, text=self.text,
                         fill=self.fg, font=self.font)


def draw_icon(cv, key, ox, oy, s, t, w=3):
    """Gambar ikon stick figure pada canvas."""
    ic = ICONS[key]
    wd = max(2, int(w * s))
    cv.create_line(ox + 5 * s, oy + 70 * s, ox + 95 * s, oy + 70 * s,
                   fill=t["text"], width=wd, capstyle="round")
    for x1, y1, x2, y2 in ic.get("dark", []):
        cv.create_line(ox + x1 * s, oy + y1 * s, ox + x2 * s, oy + y2 * s,
                       fill=t["text"], width=wd, capstyle="round")
    for x1, y1, x2, y2 in ic["red"]:
        cv.create_line(ox + x1 * s, oy + y1 * s, ox + x2 * s, oy + y2 * s,
                       fill=RED, width=wd, capstyle="round", joinstyle="round")
    for x, y, r in ic["dots"]:
        cv.create_oval(ox + (x - r) * s, oy + (y - r) * s,
                       ox + (x + r) * s, oy + (y + r) * s,
                       fill=RED, outline=RED)


# ----------------------------------------------------------------------------
# Aplikasi utama
# ----------------------------------------------------------------------------
class CaliSphere(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CaliSphere")
        self._set_app_icon()
        self.geometry(f"{DESKTOP_SIZE[0]}x{DESKTOP_SIZE[1]}")
        self.minsize(380, 640)

        self.mode = "light"
        self.page = "home"          # home | easy | normal | hard | timer
        self.compact = False        # True = tampilan HP, False = tampilan Laptop
        self.W = DESKTOP_SIZE[0]
        self.expanded = {}          # status kartu yang dibuka
        self.session = None         # data sesi timer
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
        ico = os.path.join(BASE_DIR, "icon.ico")
        png = os.path.join(BASE_DIR, "icon.png")
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
        lbl.image = img                                    # cegah garbage collect
        lbl.pack(**pack)
        return lbl

    @property
    def t(self):
        return THEMES[self.mode]

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
        self.mode = "dark" if self.mode == "light" else "light"
        self.render()

    def toggle_layout(self):
        """Pindah paksa antara ukuran HP dan ukuran Laptop."""
        w, h = DESKTOP_SIZE if self.compact else PHONE_SIZE
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
            w = DESKTOP_SIZE[0]
        self.W = w
        self.compact = w < BREAKPOINT

        self.configure(bg=t["bg"])
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
            body = tk.Frame(self, bg=t["bg"])
            body.pack(side="left", fill="both", expand=True)
            self._build_header(body)

        self.content = tk.Frame(body, bg=t["bg"])
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
        bar = tk.Frame(parent, bg=t["bg"], height=56)
        bar.pack(side="top", fill="x")
        bar.pack_propagate(False)

        show_title = ((self.compact and self.page != "home") or
                      (not self.compact and self.page == "timer"))
        if show_title:
            ic = self._logo_label(bar, t["bg"], 32, side="left", padx=(16, 0))
            if ic is not None:
                ic.config(cursor="hand2")
                ic.bind("<Button-1>", lambda e: self.goto("home"))
            lbl = tk.Label(bar, text="CaliSphere", fg=RED, bg=t["bg"],
                           font=(FONT, 16, "bold"), cursor="hand2")
            lbl.pack(side="left", padx=(8, 18))
            lbl.bind("<Button-1>", lambda e: self.goto("home"))

        # tombol mode cerah / gelap (kanan atas)
        cv = tk.Canvas(bar, width=36, height=36, bg=t["bg"],
                       highlightthickness=0, cursor="hand2")
        cv.pack(side="right", padx=(8, 16), pady=10)
        if self.mode == "light":      # ikon matahari
            cv.create_oval(11, 11, 25, 25, fill=RED, outline=RED)
            for i in range(8):
                a = math.radians(i * 45)
                cv.create_line(18 + 11 * math.cos(a), 18 + 11 * math.sin(a),
                               18 + 15 * math.cos(a), 18 + 15 * math.sin(a),
                               fill=RED, width=3, capstyle="round")
        else:                         # ikon bulan
            cv.create_oval(5, 5, 31, 31, fill=RED, outline=RED)
            cv.create_oval(13, 0, 38, 24, fill=t["bg"], outline=t["bg"])
        cv.bind("<Button-1>", lambda e: self.toggle_mode())

        # tombol ganti tampilan HP <-> Laptop (menampilkan ikon tujuan)
        lv = tk.Canvas(bar, width=36, height=36, bg=t["bg"],
                       highlightthickness=0, cursor="hand2")
        lv.pack(side="right", pady=10)
        if self.compact:              # tujuan: laptop
            lv.create_rectangle(7, 9, 29, 24, outline=RED, width=2)
            lv.create_line(3, 28, 33, 28, fill=RED, width=3, capstyle="round")
        else:                         # tujuan: HP
            round_rect(lv, 10, 4, 26, 32, 4, fill=t["bg"], outline=RED, width=2)
            lv.create_line(15, 27, 21, 27, fill=RED, width=2, capstyle="round")
        lv.bind("<Button-1>", lambda e: self.toggle_layout())

    # ---------------------------------------------- navigasi (tampilan HP)
    def _build_nav_bottom(self):
        t = self.t
        nav = tk.Frame(self, bg=t["bg"])
        nav.pack(side="bottom", fill="x")
        tk.Frame(nav, bg=t["track"], height=1).pack(fill="x")
        row = tk.Frame(nav, bg=t["bg"])
        row.pack(fill="x", pady=(0, 10))
        for key in LEVEL_ORDER:
            active = (self.page == key)
            col = tk.Frame(row, bg=t["bg"], cursor="hand2")
            col.pack(side="left", expand=True, fill="x")
            tk.Frame(col, height=5, bg=RED if active else t["bg"]).pack(
                fill="x", padx=36)
            lbl = tk.Label(col, text=LEVELS[key]["label"], bg=t["bg"],
                           fg=RED if active else t["text"],
                           font=(FONT, 15, "bold" if active else "normal"),
                           cursor="hand2")
            lbl.pack(pady=(8, 4))
            for w in (col, lbl):
                w.bind("<Button-1>", lambda e, k=key: self.goto(k))

    # --------------------------------------------- navigasi (tampilan Laptop)
    def _build_sidebar(self):
        t = self.t
        side = tk.Frame(self, bg=t["card"], width=SIDEBAR_W)
        side.pack(side="left", fill="y")
        side.pack_propagate(False)

        logo = self._logo_label(side, t["card"], 64, anchor="w",
                                padx=20, pady=(20, 0))
        if logo is not None:
            logo.config(cursor="hand2")
            logo.bind("<Button-1>", lambda e: self.goto("home"))
        title = tk.Label(side, text="CaliSphere", fg=RED, bg=t["card"],
                         font=(FONT, 20, "bold"), cursor="hand2")
        title.pack(anchor="w", padx=20, pady=(8 if logo else 24, 0))
        title.bind("<Button-1>", lambda e: self.goto("home"))
        tk.Label(side, text="Kalistenik untuk hidup sehat", fg=t["sub"],
                 bg=t["card"], font=(FONT, 9), anchor="w", justify="left",
                 wraplength=SIDEBAR_W - 40).pack(anchor="w", padx=20,
                                                 pady=(2, 28))

        for key in LEVEL_ORDER:
            active = (self.page == key)
            row = tk.Frame(side, bg=t["card"], cursor="hand2")
            row.pack(fill="x", pady=3)
            tk.Frame(row, width=5, bg=RED if active else t["card"]).pack(
                side="left", fill="y")
            txt = tk.Frame(row, bg=t["card"], cursor="hand2")
            txt.pack(side="left", fill="x", padx=(16, 0), pady=8)
            l1 = tk.Label(txt, text=LEVELS[key]["label"], bg=t["card"],
                          fg=RED if active else t["text"], cursor="hand2",
                          font=(FONT, 15, "bold" if active else "normal"))
            l1.pack(anchor="w")
            l2 = tk.Label(txt, text=LEVELS[key]["sub"], bg=t["card"],
                          fg=t["sub"], font=(FONT, 9), cursor="hand2")
            l2.pack(anchor="w")
            for w in (row, txt, l1, l2):
                w.bind("<Button-1>", lambda e, k=key: self.goto(k))

    # -------------------------------------------------------------- home
    def _build_home(self):
        t = self.t
        big = not self.compact
        box = tk.Frame(self.content, bg=t["bg"])
        box.pack(expand=True)

        self._logo_label(box, t["bg"], 128 if big else 96, pady=(0, 10))
        tk.Label(box, text="CaliSphere", fg=RED, bg=t["bg"],
                 font=(FONT, 46 if big else 34, "bold")).pack(pady=(0, 6))
        tk.Label(box, text="Pemandu hidup sehat dengan olahraga kalistenik"
                 if big else "Pemandu hidup sehat dengan\nolahraga kalistenik",
                 fg=t["sub"], bg=t["bg"], font=(FONT, 14 if big else 12),
                 justify="center").pack(pady=(0, 34 if big else 30))

        row = tk.Frame(box, bg=t["bg"])
        row.pack(pady=(0, 40 if big else 36))
        sample = {"easy": "squat", "normal": "pullup", "hard": "handstand"}
        s = 1.35 if big else 1.0
        for key in LEVEL_ORDER:
            col = tk.Frame(row, bg=t["bg"])
            col.pack(side="left", padx=18 if big else 6)
            cv = tk.Canvas(col, width=int(100 * s), height=int(80 * s),
                           bg=t["bg"], highlightthickness=0)
            cv.pack()
            draw_icon(cv, sample[key], 0, 0, s, t)
            lv = LEVELS[key]
            tk.Label(col, text=lv["label"].title(), fg=t["text"], bg=t["bg"],
                     font=(FONT, 11 if big else 10, "bold")).pack()
            tk.Label(col, text=f"({lv['sub']})", fg=t["sub"], bg=t["bg"],
                     font=(FONT, 10 if big else 9)).pack()

        RoundButton(box, "AYO LATIHAN", lambda: self.goto("easy"),
                    320 if big else 260, 68 if big else 62, t["bg"],
                    fg=t["on_red"], font_size=22 if big else 20,
                    radius=18).pack()

    # ------------------------------------------------------- halaman level
    def _make_scroll(self, parent):
        t = self.t
        wrap = tk.Frame(parent, bg=t["bg"])
        wrap.pack(side="top", fill="both", expand=True)
        cv = tk.Canvas(wrap, bg=t["bg"], highlightthickness=0, bd=0)
        cv.pack(fill="both", expand=True)
        inner = tk.Frame(cv, bg=t["bg"])
        win = cv.create_window((0, 0), window=inner, anchor="nw")
        inner.bind("<Configure>",
                   lambda e: cv.configure(scrollregion=cv.bbox("all")))
        cv.bind("<Configure>", lambda e: cv.itemconfigure(win, width=e.width))
        self.scroll_cv = cv
        return inner

    def _info_card(self, parent, lv, wrap, padx, pady):
        t = self.t
        info = tk.Frame(parent, bg=t["card"], highlightbackground=RED,
                        highlightthickness=1)
        info.pack(fill="x", padx=padx, pady=pady)
        tk.Label(info, text=f"Mode {lv['label'].title()} ({lv['sub']})",
                 fg=RED, bg=t["card"], font=(FONT, 14, "bold"),
                 anchor="w").pack(fill="x", padx=14, pady=(12, 4))
        tk.Label(info, text=lv["info"], fg=t["text"], bg=t["card"],
                 font=(FONT, 10), justify="left", anchor="w",
                 wraplength=wrap).pack(fill="x", padx=14, pady=(0, 12))

    def _build_level(self, key):
        t = self.t
        lv = LEVELS[key]
        start = lambda: self.start_session(key)

        if self.compact:
            # ---- Tampilan HP: satu kolom, tombol MULAI tetap di bawah
            bottom = tk.Frame(self.content, bg=t["bg"])
            bottom.pack(side="bottom", fill="x", pady=10)
            RoundButton(bottom, "MULAI", start, 240, 54, t["bg"],
                        fg=t["on_red"], font_size=20, radius=16).pack()

            inner = self._make_scroll(self.content)
            self._info_card(inner, lv, max(240, self.W - 72), 20, (4, 12))
            tk.Label(inner, text="Panduan Gerakan", fg=t["text"], bg=t["bg"],
                     font=(FONT, 12, "bold"), anchor="w").pack(
                fill="x", padx=22, pady=(0, 6))
            wrap = max(150, self.W - 190)
            for ex in lv["exercises"]:
                self._exercise_card(inner, key, ex, wrap, (20, 20))
            tk.Frame(inner, bg=t["bg"], height=6).pack()
        else:
            # ---- Tampilan Laptop: kolom kiri (info + MULAI), kolom kanan (gerakan)
            left = tk.Frame(self.content, bg=t["bg"], width=LEFT_COL_W)
            left.pack(side="left", fill="y", padx=(24, 12), pady=(0, 20))
            left.pack_propagate(False)
            self._info_card(left, lv, LEFT_COL_W - 32, 0, (4, 12))
            n = len(lv["exercises"])
            tk.Label(left, fg=t["sub"], bg=t["bg"], font=(FONT, 10),
                     justify="left", anchor="w",
                     text=f"{n} gerakan\n{WORK_SEC} detik latihan per gerakan\n"
                          f"{REST_SEC // 60} menit istirahat antar gerakan"
                     ).pack(fill="x", padx=2)
            RoundButton(left, "MULAI", start, LEFT_COL_W, 58, t["bg"],
                        fg=t["on_red"], font_size=20, radius=16).pack(
                side="bottom")

            right = tk.Frame(self.content, bg=t["bg"])
            right.pack(side="left", fill="both", expand=True,
                       padx=(12, 24))
            tk.Label(right, text="Panduan Gerakan", fg=t["text"], bg=t["bg"],
                     font=(FONT, 13, "bold"), anchor="w").pack(
                fill="x", pady=(4, 6))
            inner = self._make_scroll(right)
            right_w = self.W - SIDEBAR_W - LEFT_COL_W - 24 * 2 - 24
            wrap = max(160, right_w - 200)
            for ex in lv["exercises"]:
                self._exercise_card(inner, key, ex, wrap, (0, 8))
            tk.Frame(inner, bg=t["bg"], height=6).pack()

    def _exercise_card(self, parent, level, ex, wrap, padx):
        t = self.t
        name, icon, short, extra = ex
        ident = (level, name)

        card = tk.Frame(parent, bg=t["card"], highlightbackground=RED,
                        highlightthickness=1, cursor="hand2")
        card.pack(fill="x", padx=padx, pady=5)

        icv = tk.Canvas(card, width=96, height=76, bg=t["card"],
                        highlightthickness=0, cursor="hand2")
        icv.pack(side="left", padx=(8, 4), pady=10)
        draw_icon(icv, icon, 0, 0, 0.95, t)

        right = tk.Frame(card, bg=t["card"], cursor="hand2")
        right.pack(side="left", fill="both", expand=True, padx=(4, 12), pady=10)

        tk.Label(right, text=name, fg=t["text"], bg=t["card"],
                 font=(FONT, 13, "bold"), anchor="w", cursor="hand2").pack(
            fill="x")
        desc = tk.Label(right, fg=t["sub"], bg=t["card"], font=(FONT, 9),
                        justify="left", anchor="w", wraplength=wrap,
                        cursor="hand2")
        desc.pack(fill="x", pady=(2, 2))
        tog = tk.Label(right, fg=RED, bg=t["card"], font=(FONT, 9, "bold"),
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
                            remaining=WORK_SEC, running=True)
        self.page = "timer"
        self.render()
        self.job = self.after(1000, self._tick)

    def _build_timer(self):
        t = self.t
        s = self.session
        row = tk.Frame(self.content, bg=t["bg"])
        row.pack(expand=True)

        left = tk.Frame(row, bg=t["bg"])
        left.pack(side="left")
        self.timer_cv = tk.Canvas(left, width=380, height=440, bg=t["bg"],
                                  highlightthickness=0)
        self.timer_cv.pack(pady=(0, 6))

        btns = tk.Frame(left, bg=t["bg"])
        btns.pack(pady=6)
        paused = s is not None and not s["running"]
        self.pause_btn = RoundButton(
            btns, "LANJUT" if paused else "JEDA", self._toggle_pause,
            160, 52, t["bg"], fg=t["on_red"], font_size=16)
        self.pause_btn.pack(side="left", padx=8)
        RoundButton(btns, "LEWATI", self._skip, 160, 52, t["bg"],
                    fill=t["bg"], fg=RED, outline=RED,
                    font_size=16).pack(side="left", padx=8)

        end = tk.Label(left, text="Akhiri latihan", fg=t["sub"], bg=t["bg"],
                       font=(FONT, 11, "underline"), cursor="hand2")
        end.pack(pady=10)
        end.bind("<Button-1>", lambda e: self._end_session())

        # daftar gerakan di sisi kanan (khusus tampilan Laptop)
        if not self.compact and s is not None:
            panel = tk.Frame(row, bg=t["card"], highlightbackground=RED,
                             highlightthickness=1, width=270)
            panel.pack(side="left", anchor="n", padx=(48, 0), pady=40)
            tk.Label(panel, text="Daftar Gerakan", fg=RED, bg=t["card"],
                     font=(FONT, 13, "bold"), anchor="w").pack(
                fill="x", padx=18, pady=(16, 8))
            for ex in LEVELS[s["level"]]["exercises"]:
                lbl = tk.Label(panel, text=ex[0], bg=t["card"], anchor="w",
                               font=(FONT, 12), width=22)
                lbl.pack(fill="x", padx=18, pady=3)
                self.step_labels.append(lbl)
            tk.Frame(panel, bg=t["card"], height=12).pack()

        self.draw_timer()

    def draw_timer(self):
        cv = self.timer_cv
        s = self.session
        if cv is None or s is None or not cv.winfo_exists():
            return
        t = self.t
        cv.delete("all")
        lv = LEVELS[s["level"]]
        exs = lv["exercises"]
        n = len(exs)
        work = s["phase"] == "work"
        total = WORK_SEC if work else REST_SEC
        frac = max(0.0, s["remaining"] / total)
        cur = exs[s["idx"]]

        cv.create_text(190, 20, fill=t["sub"], font=(FONT, 11, "bold"),
                       text=f"{lv['label']}  \u2022  GERAKAN {s['idx'] + 1} / {n}")
        cv.create_text(190, 56, fill=t["text"], font=(FONT, 22, "bold"),
                       text=cur[0] if work else "Istirahat")

        cx, cy, r = 190, 235, 128
        box = (cx - r, cy - r, cx + r, cy + r)
        cv.create_arc(*box, start=225, extent=-270, style="arc",
                      outline=t["track"], width=16)
        if frac > 0:
            cv.create_arc(*box, start=225, extent=-270 * frac, style="arc",
                          outline=RED, width=16)

        # ikon di dalam lingkaran (saat istirahat tampilkan gerakan berikutnya)
        icon_key = cur[1] if work else exs[min(s["idx"] + 1, n - 1)][1]
        draw_icon(cv, icon_key, cx - 45, cy - 100, 0.9, t)

        m, sec = divmod(max(0, s["remaining"]), 60)
        cv.create_text(cx, cy + 28, text=f"{m:02d}:{sec:02d}", fill=t["text"],
                       font=(FONT, 44, "bold"))
        status = "LATIHAN" if work else "ISTIRAHAT"
        if not s["running"]:
            status = "DIJEDA"
        cv.create_text(cx, cy + 74, text=status, fill=RED,
                       font=(FONT, 13, "bold"))

        if not work:
            nxt = exs[min(s["idx"] + 1, n - 1)][0]
            cv.create_text(190, 420, fill=t["sub"], font=(FONT, 11),
                           text=f"Selanjutnya: {nxt}")
        else:
            cv.create_text(190, 420, fill=t["sub"], font=(FONT, 11),
                           text=f"Tahan gerakan selama {WORK_SEC} detik")

        # daftar gerakan (tampilan Laptop)
        for i, lbl in enumerate(self.step_labels):
            name = exs[i][0]
            if i < s["idx"]:
                lbl.config(text=f"\u2713  {name}", fg=t["sub"],
                           font=(FONT, 12))
            elif i == s["idx"]:
                lbl.config(text=f"\u25CF  {name}", fg=RED,
                           font=(FONT, 12, "bold"))
            else:
                lbl.config(text=f"\u25CB  {name}", fg=t["text"],
                           font=(FONT, 12))

    def _tick(self):
        self.job = None
        s = self.session
        if s is None:
            return
        if s["running"]:
            s["remaining"] -= 1
            if s["remaining"] <= 0:
                self._advance()
            elif s["remaining"] <= 3:
                self.bell()
        if self.session is not None:
            self.draw_timer()
            self.job = self.after(1000, self._tick)

    def _advance(self):
        """Pindah fase: latihan -> istirahat -> gerakan berikutnya -> selesai."""
        s = self.session
        n = len(LEVELS[s["level"]]["exercises"])
        self.bell()
        if s["phase"] == "work":
            if s["idx"] >= n - 1:
                self._finish()
                return
            s["phase"], s["remaining"] = "rest", REST_SEC
        else:
            s["idx"] += 1
            s["phase"], s["remaining"] = "work", WORK_SEC

    def _toggle_pause(self):
        s = self.session
        if s is None:
            return
        s["running"] = not s["running"]
        if self.pause_btn is not None:
            self.pause_btn.set_text("JEDA" if s["running"] else "LANJUT")
        self.draw_timer()

    def _skip(self):
        if self.session is None:
            return
        self._advance()
        if self.session is not None:
            self.draw_timer()

    def _end_session(self):
        level = self.session["level"] if self.session else "easy"
        self._cancel_job()
        self.session = None
        self.goto(level)

    def _finish(self):
        level = self.session["level"]
        self._cancel_job()
        self.session = None
        self.goto(level)
        self._show_popup()

    # --------------------------------------------------------------- popup
    def _show_popup(self):
        t = self.t
        top = tk.Toplevel(self)
        top.title("Latihan Selesai")
        top.configure(bg=t["bg"])
        top.resizable(False, False)
        top.transient(self)
        w, h = 340, 240
        x = self.winfo_x() + (self.winfo_width() - w) // 2
        y = self.winfo_y() + (self.winfo_height() - h) // 2
        top.geometry(f"{w}x{h}+{x}+{y}")

        box = tk.Frame(top, bg=t["card"], highlightbackground=RED,
                       highlightthickness=2)
        box.pack(fill="both", expand=True, padx=10, pady=10)
        tk.Label(box, text="Latihan Selesai!", fg=RED, bg=t["card"],
                 font=(FONT, 17, "bold")).pack(pady=(22, 10))
        tk.Label(box, text=POPUP_TEXT, fg=t["text"], bg=t["card"],
                 font=(FONT, 12), wraplength=270, justify="center").pack(
            padx=16)
        RoundButton(box, "SIAP", top.destroy, 140, 44, t["card"],
                    fg=t["on_red"], font_size=15, radius=14).pack(pady=20)
        top.grab_set()


if __name__ == "__main__":
    CaliSphere().mainloop()
