"""
CaliSphere - Pemandu hidup sehat dengan olahraga kalistenik
GUI minimalis (Tkinter, tanpa library tambahan)
Palet warna: Merah, Hitam, Abu
Jalankan: python calisphere.py
"""

import tkinter as tk
from tkinter import messagebox

# ----------------------------------------------------------------- Konfigurasi
WORK_SECONDS = 45
REST_SECONDS = 120
RED = "#D32F2F"
RED_HOVER = "#B71C1C"
POPUP_TEXT = "Lakukan latihan ini 4 kali seminggu dan gunakan sisa hari untuk istirahat"

THEMES = {
    "dark": dict(bg="#121212", panel="#1f1f1f", fg="#f2f2f2",
                 sub="#9a9a9a", line="#353535", btn="#2b2b2b", btn_hover="#3a3a3a"),
    "light": dict(bg="#f1f1f1", panel="#ffffff", fg="#151515",
                  sub="#666666", line="#d2d2d2", btn="#dcdcdc", btn_hover="#c8c8c8"),
}

# ----------------------------------------------------------------- Ikon gerakan
# Pose digambar sebagai stick figure pada kanvas 80x60.
# "h" = kepala, "p" = garis bersambung, "s" = properti (bar/dinding), "g" = lantai
POSES = {
    "wall_pushup": [("s", 68, 4, 68, 56), ("g",), ("h", 56, 17),
                    ("p", [(10, 54), (30, 38), (50, 25)]), ("p", [(50, 25), (66, 30)])],
    "knee_pushup": [("g",), ("h", 66, 30),
                    ("p", [(14, 44), (24, 52), (36, 42), (58, 36)]), ("p", [(58, 36), (58, 52)])],
    "squat": [("g",), ("h", 34, 10),
              ("p", [(34, 17), (30, 34), (46, 36), (40, 52)]), ("p", [(34, 20), (54, 22)])],
    "lunge": [("g",), ("h", 36, 8), ("p", [(36, 15), (36, 34)]),
              ("p", [(52, 52), (52, 36), (36, 34), (24, 44), (14, 52)])],
    "plank": [("g",), ("h", 68, 28), ("p", [(12, 50), (58, 34)]),
              ("p", [(58, 34), (56, 50), (68, 50)])],
    "pushup": [("g",), ("h", 68, 28), ("p", [(10, 52), (58, 32)]), ("p", [(58, 32), (58, 52)])],
    "pullup": [("s", 10, 8, 70, 8), ("h", 40, 17), ("p", [(28, 8), (40, 24), (52, 8)]),
               ("p", [(40, 24), (40, 42)]), ("p", [(36, 54), (40, 42), (44, 54)])],
    "dips": [("s", 44, 32, 72, 32), ("g",), ("h", 36, 12), ("p", [(36, 19), (36, 38)]),
             ("p", [(32, 54), (36, 38), (40, 54)]), ("p", [(36, 22), (46, 32)])],
    "bulgarian": [("g",), ("s", 4, 42, 18, 42), ("s", 4, 42, 4, 54), ("h", 36, 8),
                  ("p", [(36, 15), (36, 34)]),
                  ("p", [(52, 52), (52, 36), (36, 34), (24, 40), (14, 40)])],
    "pike": [("g",), ("h", 60, 42), ("p", [(12, 52), (34, 16), (54, 36), (58, 52)])],
    "adv_plank": [("g",), ("h", 68, 28), ("p", [(8, 40), (58, 34)]),
                  ("p", [(58, 34), (58, 52)]), ("p", [(58, 34), (74, 30)])],
    "handstand": [("g",), ("h", 48, 44), ("p", [(40, 54), (40, 38), (40, 10), (37, 2)])],
    "archer": [("g",), ("h", 40, 18), ("p", [(40, 26), (40, 46)]),
               ("p", [(6, 52), (40, 28), (54, 40), (62, 52)])],
    "flag": [("s", 14, 4, 14, 56), ("h", 26, 16), ("p", [(14, 14), (22, 26), (70, 26)]),
             ("p", [(14, 36), (22, 26)])],
    "lpose": [("g",), ("h", 28, 10), ("p", [(28, 17), (28, 38), (68, 38)]),
              ("p", [(28, 22), (28, 52)])],
    "pistol": [("g",), ("h", 34, 10), ("p", [(34, 17), (32, 36), (40, 38), (36, 52)]),
               ("p", [(32, 36), (68, 38)]), ("p", [(34, 20), (52, 22)])],
}

# ----------------------------------------------------------------- Data latihan
KALISTENIK = ("Kalistenik adalah latihan kekuatan yang memakai berat badan sendiri "
              "sebagai beban, tanpa alat berat. ")

LEVELS = {
    "easy": {
        "label": "Easy",
        "title": "Mode Easy - Pemula",
        "intro": KALISTENIK + "Mode Easy dirancang untuk pemula yang baru mulai berolahraga. "
                 "Gerakan di sini melatih dasar kekuatan, kestabilan, dan teknik dengan "
                 "beban ringan agar tubuh siap naik ke tingkat berikutnya.",
        "exercises": [
            ("Wall Push Up", "Push up dengan bertumpu pada dinding. Berdiri menghadap dinding, "
             "letakkan telapak tangan setinggi bahu, tekuk siku lalu dorong kembali. "
             "Melatih dada, bahu, dan trisep dengan beban paling ringan.", "wall_pushup"),
            ("Knee Push Up", "Push up dengan lutut menempel di lantai. Jaga punggung tetap lurus "
             "dari lutut hingga kepala. Membangun kekuatan dada dan lengan sebelum push up penuh.",
             "knee_pushup"),
            ("Squat", "Berdiri selebar bahu, turunkan pinggul seperti duduk di kursi, dada tegak, "
             "lutut searah jari kaki, lalu berdiri kembali. Melatih paha, bokong, dan core.",
             "squat"),
            ("Lunge", "Melangkah ke depan lalu turunkan tubuh hingga kedua lutut membentuk sudut "
             "sekitar 90 derajat, kemudian dorong kembali. Melatih paha, bokong, dan keseimbangan.",
             "lunge"),
            ("Plank", "Tahan tubuh lurus bertumpu pada kedua lengan bawah dan ujung kaki. "
             "Kencangkan perut dan bokong, jangan biarkan pinggul turun. Melatih otot inti (core).",
             "plank"),
        ],
    },
    "normal": {
        "label": "Normal",
        "title": "Mode Normal - Menengah",
        "intro": KALISTENIK + "Mode Normal untuk kamu yang sudah pernah berolahraga dan ingin "
                 "mendalami kalistenik. Gerakan di sini menuntut kekuatan tubuh bagian atas, "
                 "kontrol, dan stabilitas yang lebih besar dibanding tingkat pemula.",
        "exercises": [
            ("Regular Push Up", "Tumpu pada telapak tangan dan ujung kaki dengan tubuh lurus. "
             "Turunkan dada hingga hampir menyentuh lantai lalu dorong ke atas. "
             "Melatih dada, bahu, trisep, dan core.", "pushup"),
            ("Pull Up", "Menggantung pada bar dengan pegangan selebar bahu, tarik tubuh hingga dagu "
             "melewati bar lalu turun perlahan. Melatih punggung, bisep, dan bahu.", "pullup"),
            ("Dips", "Bertumpu pada dua bar sejajar atau kursi kokoh, turunkan tubuh dengan menekuk "
             "siku lalu dorong kembali ke atas. Melatih trisep, dada bawah, dan bahu.", "dips"),
            ("Bulgarian Split Squat", "Satu kaki di depan, kaki belakang diletakkan di bangku. "
             "Turunkan tubuh dengan lutut depan terkontrol. Melatih paha, bokong, dan "
             "keseimbangan satu kaki.", "bulgarian"),
            ("Pike Push Up", "Posisi tubuh seperti huruf V terbalik, tekuk siku hingga kepala turun "
             "mendekati lantai lalu dorong kembali. Fokus pada bahu sebagai persiapan handstand.",
             "pike"),
            ("Advanced Plank", "Plank dengan variasi lebih sulit, misalnya mengangkat satu tangan "
             "atau satu kaki secara bergantian sambil menjaga pinggul tetap stabil.", "adv_plank"),
        ],
    },
    "hard": {
        "label": "Hard",
        "title": "Mode Hard - Lanjut",
        "intro": KALISTENIK + "Mode Hard khusus untuk atlet tingkat lanjut yang sudah sangat "
                 "berpengalaman. Gerakan di sini membutuhkan kekuatan ekstrem, kontrol tubuh, "
                 "dan keseimbangan tinggi. Lakukan pemanasan penuh dan hentikan jika terasa nyeri.",
        "exercises": [
            ("Hand Stand", "Berdiri dengan tangan, tubuh lurus vertikal dan kaki ke atas. "
             "Butuh kekuatan bahu, core, dan keseimbangan yang sangat baik. "
             "Boleh dibantu dinding.", "handstand"),
            ("Archer Push Up", "Push up dengan tangan terbuka lebar: satu lengan menekuk saat lengan "
             "lainnya lurus ke samping, lalu bergantian. Jembatan menuju push up satu tangan.",
             "archer"),
            ("Human Flag", "Menahan tubuh horizontal pada tiang vertikal hanya dengan kekuatan "
             "lengan dan core. Salah satu gerakan kalistenik paling sulit.", "flag"),
            ("L Pose", "L-sit: bertumpu pada kedua tangan, tubuh terangkat dan kaki lurus ke depan "
             "sejajar lantai membentuk huruf L. Melatih core, hip flexor, dan trisep.", "lpose"),
            ("Pistol Squat", "Squat dengan satu kaki sementara kaki lainnya lurus ke depan. "
             "Butuh kekuatan, mobilitas pergelangan kaki, dan keseimbangan yang tinggi.", "pistol"),
        ],
    },
}


# ----------------------------------------------------------------- Aplikasi
class CaliSphere:
    def __init__(self, root):
        self.root = root
        self.root.title("CaliSphere")
        self.root.geometry("920x720")
        self.root.minsize(780, 640)

        self.mode = "dark"
        self.screen = "home"          # home | guide | timer
        self.level = None             # easy | normal | hard
        self.scroll_canvas = None

        # state timer
        self.steps = []
        self.step_idx = 0
        self.remaining = 0
        self.paused = False
        self.after_id = None
        self.timer_canvas = None

        self.root.bind_all("<MouseWheel>", self._on_wheel)
        self.root.bind_all("<Button-4>", self._on_wheel)
        self.root.bind_all("<Button-5>", self._on_wheel)

        self.build_layout()

    # ------------------------------------------------------------ util
    @property
    def T(self):
        return THEMES[self.mode]

    def button(self, parent, text, command, bg, fg, hover,
               font=("Helvetica", 11, "bold"), padx=20, pady=9):
        lbl = tk.Label(parent, text=text, bg=bg, fg=fg, font=font,
                       padx=padx, pady=pady, cursor="hand2")
        lbl.bind("<Enter>", lambda e: lbl.config(bg=hover))
        lbl.bind("<Leave>", lambda e: lbl.config(bg=bg))
        lbl.bind("<Button-1>", lambda e: command())
        return lbl

    def _on_wheel(self, event):
        if self.screen != "guide" or not self.scroll_canvas:
            return
        if event.num == 4 or event.delta > 0:
            self.scroll_canvas.yview_scroll(-2, "units")
        elif event.num == 5 or event.delta < 0:
            self.scroll_canvas.yview_scroll(2, "units")

    def draw_icon(self, canvas, pose_key, color):
        sub = self.T["sub"]
        k = 1.1
        for item in POSES[pose_key]:
            kind = item[0]
            if kind == "g":
                canvas.create_line(4 * k, 54 * k, 76 * k, 54 * k, fill=sub, width=2)
            elif kind == "s":
                canvas.create_line(*[v * k for v in item[1:]], fill=sub, width=3,
                                   capstyle="round")
            elif kind == "h":
                x, y = item[1] * k, item[2] * k
                r = 5 * k
                canvas.create_oval(x - r, y - r, x + r, y + r, outline=color, width=3)
            elif kind == "p":
                pts = [c * k for p in item[1] for c in p]
                canvas.create_line(*pts, fill=color, width=3, capstyle="round",
                                   joinstyle="round")

    # ------------------------------------------------------------ layout utama
    def build_layout(self):
        for w in self.root.winfo_children():
            w.destroy()
        self.scroll_canvas = None
        self.timer_canvas = None
        T = self.T
        self.root.configure(bg=T["bg"])

        # Bar atas: judul (kiri) + tombol mode cerah/gelap (kanan atas)
        top = tk.Frame(self.root, bg=T["bg"])
        top.pack(side="top", fill="x", padx=24, pady=(16, 8))
        tk.Label(top, text="CaliSphere", bg=T["bg"], fg=RED,
                 font=("Helvetica", 20, "bold")).pack(side="left")
        toggle_text = "Mode Cerah" if self.mode == "dark" else "Mode Gelap"
        self.button(top, toggle_text, self.toggle_theme, T["btn"], T["fg"],
                    T["btn_hover"], font=("Helvetica", 10, "bold"),
                    padx=14, pady=6).pack(side="right")

        # Bar bawah: Easy (kiri) | Normal (tengah) | Hard (kanan)
        bottom = tk.Frame(self.root, bg=T["bg"])
        bottom.pack(side="bottom", fill="x", padx=24, pady=(8, 18))
        for c in range(3):
            bottom.columnconfigure(c, weight=1, uniform="nav")
        placements = [("easy", "w"), ("normal", ""), ("hard", "e")]
        for col, (key, sticky) in enumerate(placements):
            active = (self.level == key and self.screen in ("guide", "timer"))
            bg = RED if active else T["btn"]
            fg = "#ffffff" if active else T["fg"]
            hv = RED_HOVER if active else T["btn_hover"]
            b = self.button(bottom, LEVELS[key]["label"].upper(),
                            lambda k=key: self.show_guide(k), bg, fg, hv,
                            padx=34, pady=11)
            b.grid(row=0, column=col, sticky=sticky)

        tk.Frame(self.root, bg=T["line"], height=1).pack(side="bottom", fill="x", padx=24)

        # Area konten
        self.content = tk.Frame(self.root, bg=T["bg"])
        self.content.pack(side="top", fill="both", expand=True, padx=24, pady=8)
        self.render_screen()

    def render_screen(self):
        for w in self.content.winfo_children():
            w.destroy()
        self.scroll_canvas = None
        self.timer_canvas = None
        if self.screen == "home":
            self.build_home()
        elif self.screen == "guide":
            self.build_guide()
        else:
            self.build_timer()

    def toggle_theme(self):
        self.mode = "light" if self.mode == "dark" else "dark"
        self.build_layout()

    # ------------------------------------------------------------ layar awal
    def build_home(self):
        T = self.T
        box = tk.Frame(self.content, bg=T["bg"])
        box.place(relx=0.5, rely=0.45, anchor="center")
        tk.Label(box, text="CaliSphere", bg=T["bg"], fg=RED,
                 font=("Helvetica", 40, "bold")).pack()
        tk.Label(box, text="Pemandu hidup sehat dengan olahraga kalistenik",
                 bg=T["bg"], fg=T["fg"], font=("Helvetica", 14)).pack(pady=(6, 18))
        tk.Label(box, text="Pilih tingkat latihan pada menu di bawah:\n"
                           "Easy (kiri)  |  Normal (tengah)  |  Hard (kanan)",
                 bg=T["bg"], fg=T["sub"], font=("Helvetica", 11), justify="center").pack()

    # ------------------------------------------------------------ panduan gerakan
    def show_guide(self, level):
        self.cancel_timer()
        self.level = level
        self.screen = "guide"
        self.build_layout()

    def build_guide(self):
        T = self.T
        data = LEVELS[self.level]

        canvas = tk.Canvas(self.content, bg=T["bg"], highlightthickness=0)
        sb = tk.Scrollbar(self.content, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        inner = tk.Frame(canvas, bg=T["bg"])
        win = canvas.create_window((0, 0), window=inner, anchor="nw")
        inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind("<Configure>", lambda e: canvas.itemconfig(win, width=e.width))
        self.scroll_canvas = canvas

        # Keterangan paling atas
        head = tk.Frame(inner, bg=T["panel"], padx=20, pady=16)
        head.pack(fill="x", pady=(0, 14), padx=(0, 6))
        tk.Label(head, text=data["title"], bg=T["panel"], fg=RED,
                 font=("Helvetica", 16, "bold"), anchor="w").pack(fill="x")
        tk.Label(head, text=data["intro"], bg=T["panel"], fg=T["fg"],
                 font=("Helvetica", 11), justify="left", anchor="w",
                 wraplength=640).pack(fill="x", pady=(8, 0))

        # Daftar gerakan: ikon + penjelasan
        for i, (name, desc, pose) in enumerate(data["exercises"], 1):
            row = tk.Frame(inner, bg=T["panel"], padx=16, pady=12)
            row.pack(fill="x", pady=5, padx=(0, 6))
            ic = tk.Canvas(row, width=88, height=66, bg=T["panel"], highlightthickness=0)
            ic.pack(side="left", padx=(0, 16))
            self.draw_icon(ic, pose, RED)
            txt = tk.Frame(row, bg=T["panel"])
            txt.pack(side="left", fill="x", expand=True)
            tk.Label(txt, text=f"{i}. {name}", bg=T["panel"], fg=T["fg"],
                     font=("Helvetica", 13, "bold"), anchor="w").pack(fill="x")
            tk.Label(txt, text=desc, bg=T["panel"], fg=T["sub"],
                     font=("Helvetica", 10), justify="left", anchor="w",
                     wraplength=520).pack(fill="x", pady=(3, 0))

        # Tombol mulai latihan
        info = (f"{len(data['exercises'])} gerakan  |  {WORK_SECONDS} detik latihan  |  "
                f"istirahat {REST_SECONDS // 60} menit antar gerakan")
        tk.Label(inner, text=info, bg=T["bg"], fg=T["sub"],
                 font=("Helvetica", 10)).pack(pady=(14, 6))
        self.button(inner, "Mulai Latihan", self.start_workout, RED, "#ffffff",
                    RED_HOVER, font=("Helvetica", 13, "bold"),
                    padx=40, pady=12).pack(pady=(0, 20))

    # ------------------------------------------------------------ timer
    def start_workout(self):
        self.cancel_timer()
        exercises = LEVELS[self.level]["exercises"]
        self.steps = []
        for i in range(len(exercises)):
            self.steps.append(("work", i, WORK_SECONDS))
            if i < len(exercises) - 1:
                self.steps.append(("rest", i, REST_SECONDS))
        self.step_idx = 0
        self.remaining = self.steps[0][2]
        self.paused = False
        self.screen = "timer"
        self.build_layout()
        self.after_id = self.root.after(1000, self.tick)

    def cancel_timer(self):
        if self.after_id is not None:
            try:
                self.root.after_cancel(self.after_id)
            except tk.TclError:
                pass
            self.after_id = None

    def build_timer(self):
        T = self.T
        wrap = tk.Frame(self.content, bg=T["bg"])
        wrap.place(relx=0.5, rely=0.5, anchor="center")

        self.lbl_phase = tk.Label(wrap, text="", bg=T["bg"], fg=RED,
                                  font=("Helvetica", 14, "bold"))
        self.lbl_phase.pack()
        self.lbl_name = tk.Label(wrap, text="", bg=T["bg"], fg=T["fg"],
                                 font=("Helvetica", 22, "bold"))
        self.lbl_name.pack(pady=(2, 10))

        self.timer_canvas = tk.Canvas(wrap, width=260, height=260, bg=T["bg"],
                                      highlightthickness=0)
        self.timer_canvas.pack()

        self.lbl_info = tk.Label(wrap, text="", bg=T["bg"], fg=T["sub"],
                                 font=("Helvetica", 11))
        self.lbl_info.pack(pady=(10, 14))

        btns = tk.Frame(wrap, bg=T["bg"])
        btns.pack()
        self.btn_pause = self.button(btns, "Jeda", self.toggle_pause, RED, "#ffffff",
                                     RED_HOVER, padx=26)
        self.btn_pause.pack(side="left", padx=5)
        self.button(btns, "Lewati", self.skip_step, T["btn"], T["fg"],
                    T["btn_hover"], padx=26).pack(side="left", padx=5)
        self.button(btns, "Kembali", lambda: self.show_guide(self.level), T["btn"],
                    T["fg"], T["btn_hover"], padx=26).pack(side="left", padx=5)
        self.draw_timer()

    def draw_timer(self):
        if self.screen != "timer" or not self.timer_canvas:
            return
        T = self.T
        kind, idx, total = self.steps[self.step_idx]
        exercises = LEVELS[self.level]["exercises"]
        working = kind == "work"
        color = RED if working else T["sub"]

        if working:
            self.lbl_phase.config(text="LATIHAN", fg=RED)
            self.lbl_name.config(text=exercises[idx][0])
            self.lbl_info.config(text=f"Gerakan {idx + 1} dari {len(exercises)}")
        else:
            self.lbl_phase.config(text="ISTIRAHAT", fg=T["sub"])
            self.lbl_name.config(text="Tarik napas, minum air")
            self.lbl_info.config(text=f"Berikutnya: {exercises[idx + 1][0]}")
        self.btn_pause.config(text="Lanjut" if self.paused else "Jeda")

        c = self.timer_canvas
        c.delete("all")
        pad = 14
        box = (pad, pad, 260 - pad, 260 - pad)
        c.create_oval(*box, outline=T["line"], width=10)
        extent = 359.9 * (self.remaining / total)
        c.create_arc(*box, start=90, extent=extent, style="arc", outline=color, width=10)
        m, s = divmod(self.remaining, 60)
        c.create_text(130, 130, text=f"{m:02d}:{s:02d}", fill=T["fg"],
                      font=("Helvetica", 44, "bold"))

    def tick(self):
        self.after_id = None
        if self.screen != "timer":
            return
        if not self.paused:
            self.remaining -= 1
            if self.remaining <= 0:
                self.root.bell()
                self.next_step()
                return
            self.draw_timer()
        self.after_id = self.root.after(1000, self.tick)

    def next_step(self):
        self.step_idx += 1
        if self.step_idx >= len(self.steps):
            self.finish_workout()
            return
        self.remaining = self.steps[self.step_idx][2]
        self.draw_timer()
        self.after_id = self.root.after(1000, self.tick)

    def toggle_pause(self):
        self.paused = not self.paused
        self.draw_timer()

    def skip_step(self):
        self.cancel_timer()
        self.next_step()

    def finish_workout(self):
        self.cancel_timer()
        messagebox.showinfo("CaliSphere", POPUP_TEXT)
        self.show_guide(self.level)


if __name__ == "__main__":
    root = tk.Tk()
    CaliSphere(root)
    root.mainloop()