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
