from libs import (
    datetime, difflib, random, time, sys, winsound, os, threading,
    msvcrt
)

#ini gua ravael bukan ai yah ini cuma buat catatan kita udh kelar tinggal dialog dialog masing masing aja


admin_mode = False  # ADMIN MODE

data_load = "data.txt"

def load_data(): #ini buat load data password
    try:
        with open(data_load, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []
    
def statistik_data():
    data = load_data()
    total = len(data)
    kuat = sum(1 for d in data if "KUAT" in d)
    gagal = sum(1 for d in data if "GAGAL" in d)

    print("=== STATISTIK PASSWORD ===")
    print(f"Total Percobaan : {total}")
    print(f"Password Kuat   : {kuat}")
    print(f"Password Gagal  : {gagal}")
    
def hapus_data():
    with open("data.txt", "w") as file:
        file.write("")
    print("Semua data berhasil dihapus.")

    



MERAH = "\033[91m"
HIJAU = "\033[92m"
BIRU = "\033[94m"
UNGU = "\033[95m"
CYAN = "\033[96m"
KUNING = "\033[93m"
HITAM = "\033[30m"
RESET = "\033[0m"

hum_active = False

def background_hum():
    global hum_active
    while hum_active:
        winsound.Beep(60, 60)
        time.sleep(0.6)

def beep_normal():
    winsound.Beep(440, 30)

def beep_tegang():
    winsound.Beep(220, 80)

def beep_misterius():
    winsound.Beep(650, 50)

def beep_bahaya():
    for _ in range(3):
        winsound.Beep(130, 100)
        time.sleep(0.06)

def beep_escape():
    for freq in [550, 750, 950]:
        winsound.Beep(freq, 70)
        time.sleep(0.03)

def beep_glitch():
    for _ in range(2):
        winsound.Beep(80, 20)
        winsound.Beep(1200, 20)
    time.sleep(0.1)

def ketik(teks, warna=RESET, delay=0.012, glitch=False, sound_type="normal"):
    sys.stdout.write(warna)
    for i, huruf in enumerate(teks):
        sys.stdout.write(huruf)
        sys.stdout.flush()

        if sound_type == "normal":
            if random.random() < 0.8:
                beep_normal()
        elif sound_type == "tegang":
            if i % 3 == 0:
                beep_tegang()
        elif sound_type == "misterius":
            if random.random() < 0.3:
                beep_misterius()
        elif sound_type == "bahaya":
            if i % 2 == 0:
                winsound.Beep(160, 50)

        time.sleep(delay)

        if glitch and random.random() < 0.07:
            glitch_char = random.choice(["█", "▓", "⚡"])
            sys.stdout.write(glitch_char)
            sys.stdout.flush()
            time.sleep(0.02)
            sys.stdout.write("\b")
            sys.stdout.flush()
            beep_glitch()

    sys.stdout.write(RESET + "\n")
    time.sleep(0.12)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def jumpscare():
    clear_screen()

    ketik("Kamu merasa sedang diperhatikan...", MERAH, delay=0.04)
    time.sleep(2)

    clear_screen()
    time.sleep(1)

    winsound.Beep(3500, 300)

    face1 = """
            .-\"\"\"\"-.
           / -   -   \\
          |  .-.  .-.  |
          |  | |    | |  |
          |      <         |
          |     _____      |
           \\               /
            \\             /
             `-._       _.-`
                `\"""\""`
    """

    face2 = """
            .-\"\"\"\"-.
           / -   -   \\
          |   ___    ___   |
          |   \\___/  \\___/  |
          |        <          |
          |    _________     |
           \\                /
            \\              /
             `-._        _.-`
                `\"""\""`
    """

  
    face3 = """
            .-\"\"\"\"-.
           / -   -   \\
          |    ███      ███    |
          |    ███      ███    |
          |          <            |
          |    ______________    |
           \\                   /
            \\                 /
             `-._           _.-`
                `\"""\"\"\"`
    """

    for _ in range(2):
        clear_screen()
        print(MERAH + face1 + RESET)
        winsound.Beep(2000, 80)
        time.sleep(0.2)

        clear_screen()
        print(MERAH + face2 + RESET)
        winsound.Beep(2500, 80)
        time.sleep(0.2)

        clear_screen()
        print(MERAH + face3 + RESET)
        winsound.Beep(3000, 120)
        time.sleep(0.3)

    winsound.Beep(4000, 400)
    clear_screen()



nama_guru = [
    "wisnu","ali","diani","fuad","adhie","ros","suhendra",
    "herry","yusuf","murni","afandi","maysito",
    "aliah","putri","kadirah","sukas"
]

npc_dialog = [
    "\"Kamu sudah melewati lorong ini sebelumnya.\"",
    "\"Jangan percaya pada bayanganmu sendiri.\"",
    "\"Semakin kamu berjalan, semakin jauh kamu tersesat.\"",
    "\"Lampu tidak pernah benar-benar mati.\"",
    "\"Sosok anomali sedang memperhatikan mu.\"",
    "\"Beberapa pintu hanya ilusi.\"",
    "\"Jangan terlalu sering memilih arah yang sama.\"",
    "\"Lorong ini menyukai pengulangan.\"",
    "\"Ada langkah kaki dari sosok anomali inisial JF.\"",
    "\"Anomali mulai mendekati mu, ayo cepat lari!!!.\"",
    "\"Suara langkah itu bukan milikmu.\"",
    "\"Di ujung lorong, sebuah pintu putih muncul perlahan.\"",
    "\"Cepatlah berlari sesuatu yang mengancam nyawamu sedang ada disini!!\"",
    "\"Apakah kamu yakin dengan jalan yang kamu pilih?.\"",
    "\"Tidak ada yang bisa membantumu selain diri mu sendiri.\"",
    "\"Hanya diri mu sendiri yang dapat di andalkan.\"",
    "\"Ayo cepat lah sebentar lagi kamu menemukan jalan keluarnya.\"",
    "\"Tidak semua jalan yang kamu pilih benar.\"",
]

npc_characters = {

    "Pria Pendek Itu": {
        "nama_asli" : "Alzai7",
        "ketauan_namanya": False,
        "appearance": [
            "Seorang pria pendek dengan jas laboratorium lusuh.",
            "Matanya cekung dan terlihat tidak tidur berhari-hari.",
            "Ia membawa buku catatan penuh simbol aneh."
        ],
        "questions": {
            "Siapa kamu sebenarnya?": {
                "responses": [
                    "Namaku Alzai7.",
                    "Aku dulu peneliti dimensi ini.",
                    "Identitasku tidak lagi penting.",
                    "Kamu tidak punya hak untuk menanyaiku soal itu."
                ],
                "trust": 1,
                "replace_with": {
                    "Peneliti? Apa yang sedang kamu teliti?": {
                        "responses": [
                            "Teori tentang celah antar dimensi.",
                            "Hal-hal yang seharusnya tidak dibuka tetap tertutup."
                        ],
                        "trust": 1
                    }
                }
            },
            "Kenapa kamu bisa di sini?": {
                "responses": [
                    "Eksperimenku gagal.",
                    "Bukan urusanmu.",
                    "Aku membuka celah yang salah.",
                    "Aku terlalu penasaran."
                ],
                "trust": 1,
                "replace_with": {
                    "Apa yang terjadi saat eksperimen gagal?": {
                        "responses": [
                            "Suara aneh, bayangan yang bukan bayangan, lalu kesunyian.",
                            "Beberapa orang tidak pernah kembali sama setelah itu."
                        ],
                        "trust": 1
                    }
                }
            },
            "Bagaimana cara keluar?": {
                "responses": [
                    
                    "Jangan ulang arah tiga kali.",
                    "Tempat ini menyukai pola.",
                    "Keluar bukan soal cepat."
                ],
                "escape": 0.05,
                "replace_with": {
                    "Kenapa menghindari pengulangan arah?": {
                        "responses": [
                            "Pengulangan memberi ruang bagi sesuatu untuk menyalin jejakmu.",
                            "Jika kau terus berputar, kau memberi mereka waktu."
                        ],
                        "escape": 0.03,
                        "trust": 1
                    }
                }
            },
            "Apa rahasia tempat ini?": {
                "responses": [
                    "Ada pintu putih.",
                    "Pintu itu hanya muncul saat kamu tenang.",
                    "Tidak semua orang bisa melihatnya."
                ],
                "trust_required": 2,
                "escape": 0.1,
                "replace_with": {
                    "Mengapa pintu itu hanya muncul saat tenang?": {
                        "responses": [
                            "Pintu merespon ketenangan, bukan usaha paksa.",
                            "Kau harus berhenti berharap dan mulai menerima."
                        ],
                        "trust": 2,
                        "escape": 0.07
                    }
                }
            }
        }
    },


    "Gadis Punk Mencurigakan ": {
        "nama_asli" : "Vani",
        "ketauan_namanya": False,
        "appearance": [
            "Gadis dengan hoodie abu-abu.",
            "Matanya terus melihat ke belakang.",
            "Seperti ada yang mengikutinya."
        ],
        "questions": {
            "Siapa kamu sebenarnya?": {
                "responses": [
                    "Namaku Vani.",
                    "Aku tersesat saat mengikuti suara aneh.",
                    "Identitasku tidak lagi penting."
                ],
                "trust": 1,
                "replace_with": {
                    "Kenapa kamu menyendiri?": {
                        "responses": [
                            "Aku butuh jarak dari suara-suara itu.",
                            "Kadang sendiri satu-satunya cara agar aku tetap waras."
                        ],
                        "trust": 2
                    }
                }
            },
            "Kenapa kamu bisa di sini?": {
                "responses": [
                    "Kupikir itu temanku.",
                    "Ternyata bukan.",
                    "Aku terlalu penasaran."
                ],
                "trust": 1,
                "replace_with": {
                    "Apa yang kamu cari di sini?": {
                        "responses": [
                            "Aku tidak tahu lagi apa yang kutemukan.",
                            "Mungkin jawaban, atau sekadar tempat untuk bersembunyi."
                        ],
                        "trust": 1
                    }
                }
            },
            "Bagaimana cara keluar?": {
                "responses": [
                    "Hitung kedipan lampu.",
                    "Tiga kali berkedip = aman.",
                    "Keluar bukan soal cepat."
                ],
                "escape": 0.05,
                "replace_with": {
                    "Apa yang harus kulakukan saat lampu berkedip?": {
                        "responses": [
                            "Jangan panik, lihat sekeliling dan ikuti arah yang paling tenang.",
                            "Kadang itu hanya gangguan. Tunggu hingga berkedip lagi."
                        ],
                        "escape": 0.03,
                        "trust": 1
                    }
                }
            },
            "Apa rahasia tempat ini?": {
                "responses": [
                    "Makhluk itu meniru gerakanmu.",
                    "Jangan pernah berhenti mendadak.",
                    "Tidak semua orang bisa melihatnya."
                ],
                "trust_required": 2,
                "escape": 0.1,
                "replace_with": {
                    "Bagaimana aku bisa tahu kalau makhluk itu meniruku?": {
                        "responses": [
                            "Perhatikan bayanganmu. Jika ia bergerak selangkah setelahmu, itu tanda.",
                            "Jangan biarkan dia melihat ketakutanmu."
                        ],
                        "trust": 2,
                        "escape": 0.05
                    }
                }
            }
        }
    },

    "gadis misterius": {
        "nama_asli" : "Ila",
        "ketauan_namanya": False,
        "appearance": [
            "seorang gadis cantik dan pendiam bersandar di dinding.",
            "ia hampir tidak bersuara.",
            "tatapannya yang sendu dan juga lembut."
        ],
        "questions": {
            "Siapa kamu sebenarnya?": {
                "responses": [
                    "namaku Ila.",
                    "namaku bukanlah sebuah hal yang harus kau ingat.",
                    "karena bagiku namaku tidak lagi penting.",
                    "aku adalah orang yang selalu dilupakan.",
                    "dan itu tidaklah masalah bagiku."
                ],
                "trust": 1,
                "replace_with": {
                    "Dilupakan? Mengapa?": {
                        "responses": [
                            "karena aku memang orang yang tidak penting.",
                            "dunia tidak pernah membutuhkanku untuk ada.",
                            "dan di sini, aku akhirnya bisa menerima itu."
                        ],
                        "trust": 2
                    }
                }
            },
            "Kenapa kamu bisa di sini?": {
                "responses": [
                    "aku disini karena ingin mencari ketenangan dari dunia yang selalu berisik.",
                    "disini aku bisa merasa aman dan tidak ada yang menghinaku.",
                    "karena aku bisa menjadi diriku sendiri tanpa dituntut menjadi orang lain.",
                    "dan itu menyenangkan."
                ],
                "trust": 1,
                "replace_with": {
                    "Jadi tempat ini adalah surga bagimu?": {
                        "responses": [
                            "mungkin demikian dari sudut pandangku.",
                            "di tempat ini, aku bisa lepas dari semua tekanan.",
                            "tidak ada ekspektasi, tidak ada penilaian."
                        ],
                        "trust": 2
                    }
                }
            },
            "Bagaimana cara keluar?": {
                "responses": [
                    "berlarilah dengan tenang dan jangan panik.",
                    "ketika kau mendengar suara, abaikanlah.",
                    "jika bertemu dengan seseorang yang kau rasa adalah orang jahat, jangan mempercayainya.",
                    "kepercayaan terhadap dirimu adalah hal yang penting agar kau bisa keluar.",
                    "bila kau ingin keluar dari labirin ini, maka ikuti kata hatimu dan jalankan dengan tenang.",
                    "karena ketenangan adalah kunci agar semuanya bisa berakhir.",
                    "dan jawaban dari pertanyaanmu tidak ada di peta, tetapi ada di dirimu sendiri."
                ],
                "escape": 0.05,
                "replace_with": {
                    "Kata hati... tapi hati siapa yang harus aku percayai?": {
                        "responses": [
                            "hati yang sudah berhenti takut.",
                            "hati yang menerima keadaan tanpa membencinya.",
                            "hati yang seperti punyaku... yang sudah mati rasa."
                        ],
                        "escape": 0.08,
                        "trust": 1
                    }
                }
            },
            "Apa rahasia tempat ini?": {
                "responses": [
                    "ikuti jalan yang memang menurutmu harus untuk dilewati.",
                    "labirin ini bergerak mengikuti keinginan hatimu untuk melewatinya.",
                    "kepercayaan terhadap dirimu adalah hal yang penting agar kau bisa keluar dari sini.",
                    "karena tidak semua dinding ini aman untuk disentuh, maka gunakanlah insting yang kau punya.",
                    "maka dengan semua yang aku sudah sebutkan tadi, kau bisa memenangkan game ini."
                ],
                "trust_required": 2,
                "escape": 0.1,
                "replace_with": {
                    "Apakah kamu bisa membantu aku keluar?": {
                        "responses": [
                            "aku sendiri masih berada di sini.",
                            "dan mungkin... aku tidak ingin pergi.",
                            "tapi kau bisa. kau lebih kuat dari yang kau pikir."
                        ],
                        "escape": 0.12,
                        "trust": 2
                    }
                }
            }
        }
    },

    "Wanita Bisnis Penuh Misteri": {
        "nama_asli" : "Netta",
        "ketauan_namanya": False,
        "appearance": [
            "Perempuan dengan pakaian penuh debu.",
            "Tangannya penuh goresan."
        ],
        "questions": {
            "Siapa kamu sebenarnya?": {
                "responses": [
                    "Namaku Netta.",
                    "Aku sudah di sini lama.",
                    "Identitasku tidak lagi penting."
                ],
                "trust": 1
            },
            "Kenapa kamu bisa di sini?": {
                "responses": [
                    "Aku membuka pintu yang salah.",
                    "Pintu itu menipu.",
                    "Aku terlalu penasaran."
                ],
                "trust": 1
            },
            "Bagaimana cara keluar?": {
                "responses": [
                    "Pintu putih muncul saat kamu menyerah.",
                    "Tempat ini menyukai keputusasaan.",
                    "Keluar bukan soal cepat."
                ],
                "escape": 0.05
            },
            "Apa rahasia tempat ini?": {
                "responses": [
                    "Tidak semua pintu menyelamatkan.",
                    "Beberapa pintu membawa lebih dalam.",
                    "Tidak semua orang bisa melihatnya."
                ],
                "trust_required": 2,
                "escape": 0.1
            }
        }
    },
    
"Lanang Yang Sangat Sus": {
    "nama_asli": "Hydro",
    "ketauan_namanya": False,
    "appearance": [
        "Pria dengan senyum terlalu tenang untuk situasi seperti ini.",
        "Matanya seperti sudah tahu akhir cerita.",
        "Tidak terlihat panik. Justru seperti menunggu sesuatu."
    ],
    "questions": {

        "Kamu terlihat terlalu santai... siapa kamu sebenarnya?": {
            "responses": [
                "Santai? Tidak juga.",
                "Aku hanya sudah menerima kemungkinan terburuk.",
                "Namaku... Hydro.",
                "Atau setidaknya itu nama yang kau boleh tahu."
            ],
            "trust": 1,
            "replace_with": {
                "Hydro? Itu nama aslimu?":{
                    "responses": [
                        "Nama asli?... Ck itu tidak penting untuk mu."
                    ],
                    "trust": 2
                }
            }
        },

        "Kenapa kamu tidak panik seperti yang lain?": {
            "responses": [
                "Panik tidak pernah menyelamatkan siapa pun.",
                "Aku pernah berada di tempat yang lebih buruk.",
                "Atau mungkin... aku memang sudah tahu ini akan terjadi."
            ],
            "trust": 1,
            "replace_with": {
                "Kamu tahu ini akan terjadi?": {
                    "responses": [
                        "Hanya saja aku sudah melihat ini sebelumnya.....",
                        "Seperti dejavu..,"
                    ]
                }
            }
        },

        "Apa kamu tahu sesuatu yang tidak kami tahu?": {
            "responses": [
                "Semua orang tahu sesuatu.",
                "Hanya saja mereka pura-pura lupa.",
                "Tempat ini berbicara... kalau kau mau mendengar."
            ],
            "trust": 1,
            "replace_with": {
                "Tempat ini berbicara? Apa maksudmu?": {
                    "responses": [
                        "Dengarkan... dengarkan saja demi Tuhan.",
                        "Dengungan, bisikan, langkah... semuanya berbicara."
                    ],
                    "trust": 1
                }
            }
        },

        "Bagaimana sebenarnya cara keluar dari tempat ini?": {
            "responses": [
                "Keluar bukan tentang menemukan pintu.",
                "Ini tentang memilih siapa yang kau korbankan.",
                "Dan siapa yang kau percaya.",
                "Karena tempat ini... memakan keraguan."
            ],
            "escape": 0.07,
            "replace_with": {
                "Siapa yang harus aku korbankan?": {
                    "responses": [
                        "Orang yang paling kau tidak percayai.",
                        "Atau orang yang paling kau cintai...",
                        "Pilihan ada di tanganmu."
                    ],
                    "trust": 2,
                    "escape": 0.1
                }
            }
            }
        }
    }
}

def npc_interaction_system():
    npc_name = random.choice(list(npc_characters.keys()))
    npc = npc_characters[npc_name]
    display_name = npc_name


    clear_screen()
    ketik("Seseorang berdiri di ujung lorong...", KUNING, 0.03)

    for desc in npc["appearance"]:
        ketik(desc, CYAN, 0.02)

    print("\nApa yang ingin kamu lakukan?")
    print("1. Dekati")
    print("2. Kabur")
    print("3. Abaikan")

    pilihan = input(">> ")

    if pilihan == "2":
        ketik("Kamu memilih kabur.", MERAH)
        return -0.02

    if pilihan == "3":
        ketik("Kamu mengabaikannya.", KUNING)
        return 0

    trust = 0
    escape_bonus = 0

    clear_screen()

    while True:
        print(f"\nBerbicara dengan {display_name}:")
        question_list = list(npc["questions"].keys())

        for i, q in enumerate(question_list, 1):
            print(f"{i}. {q}")

        print(f"{len(question_list)+1}. Hentikan percakapan")

        pilih = input(">> ")
        time.sleep(0.5)
        clear_screen()

        if not pilih.isdigit():
            continue

        pilih = int(pilih)

        if pilih == len(question_list)+1:
            ketik("NPC menghilang dalam lorong...", KUNING)
            break

        if 1 <= pilih <= len(question_list):
            question = question_list[pilih-1]
            data = npc["questions"][question]

            if "trust_required" in data and trust < data["trust_required"]:
                ketik("Aku belum cukup percaya padamu.", MERAH)
                continue

            response = random.choice(data["responses"])
            ketik(response, CYAN, 0.02)
            
            if "Namaku" in response and "nama_asli" in npc:
                npc["ketauan_namanya"] = True
                display_name = npc["nama_asli"]
                ketik(f"(Sekarang kamu tahu namanya adalah {display_name})", KUNING)
            
            if "replace_with" in data:
                npc["questions"].update(data["replace_with"])

            # HAPUS pertanyaan lama
            del npc["questions"][question]

            time.sleep(0.5)
            clear_screen()

            if "trust" in data: 
                trust += data["trust"]

            if "escape" in data:
                escape_bonus += data["escape"]

    return escape_bonus

def backroom_game(password):
    global hum_active
    global admin_mode
    hum_active = False
    hum_thread = threading.Thread(target=background_hum, daemon=True)
    hum_thread.start()

    clear_screen()

    ketik("[PASSWORD SEDANG DI CEK]...", warna=KUNING, delay=0.35, sound_type="misterius")
    time.sleep(0.6)
    clear_screen()
    if admin_mode:
        ketik("ADMIN MODE DETECTED", warna=UNGU, glitch=True, sound_type="misterius")
        clear_screen()
    ketik("LoAdInG...", warna=KUNING, delay=0.40, sound_type="misterius")
    clear_screen()
    if not admin_mode:
        ketik("Mengirimkan Data User Ke Server...", warna=BIRU, delay=0.03, sound_type="misterius")
        ketik("Sistem Sedang Mempersiapkan Server Untuk Masuk...", warna=MERAH, delay=0.05, sound_type="misterius")
        clear_screen()
    else:
        ketik("Selamat Datang Kembali Sir Admin Kami Sudah Lama Menunggumu...", warna=UNGU, glitch=True, sound_type="misterius")
    clear_screen()
    if not admin_mode:
        ketik("Server Mendeteksi Adanya Gangguan Anomali Aneh...", warna=MERAH, delay=0.15, sound_type="misterius")
        ketik("Mohon Menunggu...", warna=MERAH, delay=0.20, sound_type="misterius")
        clear_screen()
    else:
        ketik("Kamu Sudah Siap Menunjukan Pada Dunia Bahwa Kekuatan Admin Mu Itu Nyataa?!", warna=MERAH, delay=0.15, sound_type="misterius")
        clear_screen()
    if not admin_mode:
        ketik("......", warna=MERAH, delay=0.35, sound_type="misterius")
        clear_screen()
        ketik("Server Has Been Hacking...", warna=MERAH, delay=0.25, sound_type="misterius")
        clear_screen()
    else:
        ketik("YESSS KING ADMIN WE DID IT AYO KALAHKAN JF!!", warna=BIRU, delay=0.25, sound_type="misterius")
        clear_screen()
        ketik("Lanjutkan...", warna=MERAH, delay=0.20, sound_type="misterius")
        clear_screen()

    while True:
        clear_screen()
        print(f"{KUNING}\n\n\n        >>> PRESS ENTER TO START <<< {RESET}")
        time.sleep(0.6)
        clear_screen()
        time.sleep(0.4)
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\r':
                break

    ketik(f"""{MERAH}
Lampu berkedip.
Dinding kuning lembab membentang tanpa akhir.
Dengungan listrik memenuhi udara.
Tidak ada pintu.
Tidak ada jendela.
Hanya maze tanpa ujung.
{RESET}""")

    event_terakhir = None
    jumlah_click = {"w":0, "a":0, "s":0, "d":0}
    
    escape_chance = 0.01
    if admin_mode:
        escape_chance = 0.35


    while True:
        print(f"\n{CYAN}Gunakan W (maju) A (kiri) S (mundur) D (kanan){RESET}")
        gerak = input(">> ").lower()

        if gerak not in ["w","a","s","d"]:
            print("Command tidak dikenali.")
            continue

        jumlah_click[gerak] += 1
        for key in jumlah_click:
            if key != gerak:
                jumlah_click[key] = 0

        if jumlah_click["w"] >= 3:
            if not admin_mode:
                ketik("Kamu jatuh ke kehampaan. Game Over.", warna=MERAH, delay=0.05, glitch=True, sound_type="tegang")
                jumpscare()
                save_password(password, "GAME_OVER")

                break
            else:
                ketik("ADMIN OVERRIDE: VOID DITOLAK", warna=UNGU)

        if jumlah_click["a"] >= 3:
            if not admin_mode:
                ketik("Sosok tanpa wajah muncul. Game Over.", warna=UNGU, delay=0.05, glitch=True, sound_type="tegang")
                save_password(password, "GAME_OVER")

                break
            else:
                ketik("ADMIN OVERRIDE: ENTITY TUNDUK", warna=UNGU)
                \
                
        if jumlah_click["a"] >= 2:
            ketik("Lihatlah sebelahmu wahai anak muda.....", warna=BIRU , delay=0.03)
            ketik("Aku melihat ada seseorang di ujung jalan....", warna=MERAH , delay=0.03 , sound_type="misterius")
            
            bonus = npc_interaction_system()
            escape_chance += bonus

            jumlah_click["a"] = 0
            if admin_mode:
                ketik("KAMU ADMIN KAMU TIDAK PERLU NPC KAN!!", warna=UNGU)
            else:
                continue
            
        if jumlah_click["w"] >= 2:
            ketik("Ada suara langkah kaki yang bergemuruh", warna=MERAH, delay=0.05, glitch=True, sound_type="tegang")
            ketik("kamu menemukan seseorang disisi jalan coba dekati!", warna=MERAH, delay=0.05, sound_type="tegang")
                
            bonus = npc_interaction_system()
            escape_chance += bonus

            jumlah_click["a"] = 0
            if admin_mode:
                ketik("KAMU ADMIN KAMU TIDAK PERLU NPC KAN!!", warna=UNGU)
            else:
                continue
                

        if jumlah_click["s"] >= 2:
            ketik("lampu tiba tiba berkedip dengan cepat tanpa aba aba...", warna=KUNING, delay=0.03)
            ketik("Kamu melihat siluet seseorang di ujung lorong.", warna=UNGU, delay=0.03, sound_type="misterius")

            bonus = npc_interaction_system()
            escape_chance += bonus

            jumlah_click["a"] = 0
            if admin_mode:
                ketik("KAMU ADMIN KAMU TIDAK PERLU NPC KAN!!", warna=UNGU)
            else:
                continue

        if jumlah_click["s"] >= 3:
            if not admin_mode:
                ketik("Lorong menutup di belakangmu. Game Over.", warna=BIRU, delay=0.05, glitch=True, sound_type="tegang")
                save_password(password, "GAME_OVER")

                break
            else:
                ketik("ADMIN OVERRIDE: DINDING TERBUKA", warna=UNGU)

        if jumlah_click["d"] >= 2:
            ketik("Lorong di sebelah kiri terasa berbeda...", warna=KUNING, delay=0.03)
            ketik("Kamu melihat siluet seseorang di ujung lorong.", warna=UNGU, delay=0.03, sound_type="misterius")

            bonus = npc_interaction_system()
            escape_chance += bonus

            jumlah_click["a"] = 0
            if admin_mode:
                ketik("KAMU ADMIN KAMU TIDAK PERLU NPC KAN!!", warna=UNGU)
            else:
                continue

        if jumlah_click["d"] >= 3:
            if not admin_mode:
                ketik("Penjaga lorong menghentikanmu. Game Over.", warna=KUNING, delay=0.05, glitch=True, sound_type="tegang")
                save_password(password, "GAME_OVER")

                break
            else:
                ketik("ADMIN OVERRIDE: PENJAGA MENUNDUK", warna=UNGU)
        while True:
            event = random.randint(1,11)
            if event != event_terakhir:
                break
                
        event_terakhir = event
        
        if event == 1:
            ketik("Lampu di atasmu berkedip pelan...", KUNING, delay=0.03, sound_type="misterius")
            clear_screen()
        elif event == 2:
            npc = random.choice(npc_dialog)
            ketik("NPC misterius muncul...", BIRU, delay=0.03, sound_type="misterius")
            time.sleep(0.5)
            clear_screen()
            ketik(npc, BIRU, delay=0.05, sound_type="normal")
        elif event == 3:
            ketik("Lorong berubah bentuk sesaat...", CYAN, delay=0.03, sound_type="misterius")
            clear_screen()
        elif event == 4:
            ketik("Kamu merasa sedang diikuti...", MERAH, delay=0.03, sound_type="tegang")
            clear_screen()
        elif event == 5:
            ketik("Bayanganmu bergerak lebih dulu...", UNGU, delay=0.03, sound_type="misterius")
            clear_screen()
        elif event == 6:
            ketik("Tanda panah muncul lalu hilang...", HIJAU, delay=0.03, sound_type="normal")
            clear_screen()
        elif event == 7:
            ketik("Bisikan samar terdengar...", KUNING, delay=0.03, sound_type="tegang")
            clear_screen()
        elif event == 8:
            ketik("Makhluk aneh berjalan di belakangmu...", MERAH, delay=0.03, sound_type="tegang")
            clear_screen()
        elif event == 9:
            ketik("Suara langkah kaki bergema dari jauh...", KUNING, delay=0.03, sound_type="tegang")
            time.sleep(0.5)
            clear_screen()
            ketik("...tapi tidak ada siapa-siapa.", KUNING, delay=0.05, sound_type="misterius")
            clear_screen()
        elif event == 10:
            ketik("Lorong tiba-tiba menjadi gelap...", HITAM, delay=0.03, sound_type="tegang")
            time.sleep(0.5)
            clear_screen()
            ketik("Kemudian lampu kembali menyala.", HITAM, delay=0.05, sound_type="normal")
        elif event == 11:
            bonus = npc_interaction_system()
            escape_chance += bonus

        if random.random() < escape_chance:
            if admin_mode:
                ketik("Portal hitam terbuka. Kamu menguasai Backroom.", UNGU, glitch=True)
                ketik("ENDING RAHASIA: THE ARCHITECT", UNGU, glitch=True)
            else:
                ketik("Kamu menemukan pintu putih dan berhasil keluar!", HIJAU, 0.05)
                save_password(password, "MENANG")

            break
        
    hum_active = False
    time.sleep(0.5)
def save_password(password, status):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("data.txt", "a") as file:
        file.write(f"{password} | {status} | {waktu}\n")


def main():
    global admin_mode

    while True:
        clear_screen()
        ketik("PASSWORD ANALYZING...", warna=KUNING, delay=0.15, sound_type="misterius")
        clear_screen()

        print(f"\n{UNGU}╔══════════════════════╗")
        print(f"║  CHECKER PASSWORD    ║")
        print(f"╚══════════════════════╝{RESET}")
        print("1. Cek Kekuatan Password")
        print("2. Lihat Data Password")
        print("3. Statistik Password")
        print("4. Hapus Data Password")
        print("5. Keluar")

        try:
            pilihan = int(input("Pilih menu (1/2/3/4/5): "))
        except ValueError:
            print("Input harus berupa angka!")
            time.sleep(1.5)
            continue

        if pilihan == 1:
            while True:
                password = input("Masukkan Password Baru Mu : ")

                password_lower = password.lower()

                if "admin" in password_lower or "root404" in password_lower:
                    admin_mode = True
                else:
                    admin_mode = False

                ada_besar = any(h.isupper() for h in password)
                ada_kecil = any(h.islower() for h in password)
                ada_angka = any(h.isdigit() for h in password)
                ada_simbol = any(not h.isalnum() for h in password)

                def mirip_nama(password, daftar_nama, threshold=0.75):
                    import re

                    def norm(s):
                        return re.sub(r"\W+", "", s).lower()

                    p = norm(password)
                    if not p:
                        return False

                    for guru in daftar_nama:
                        g = norm(guru)
                        if not g:
                            continue
                        if g in p:
                            return True

                        # jika password lebih panjang, cek setiap substring panjang nama
                        if len(p) >= len(g):
                            for i in range(len(p) - len(g) + 1):
                                window = p[i:i+len(g)]
                                ratio = difflib.SequenceMatcher(None, window, g).ratio()
                                if ratio >= threshold:
                                    return True
                        else:
                            # bila password lebih pendek, bandingkan langsung
                            if difflib.SequenceMatcher(None, p, g).ratio() >= threshold:
                                return True

                    return False

                ada_nama_guru = mirip_nama(password_lower, nama_guru)

                error = []

                if len(password) < 8:
                    error.append("Minimal 8 karakter")
                if not ada_besar:
                    error.append("Harus ada huruf kapital")
                if not ada_kecil:
                    error.append("Harus ada huruf kecil")
                if not ada_angka:
                    error.append("Harus ada angka")
                if not ada_simbol:
                    error.append("Harus ada simbol")
                if not ada_nama_guru:
                    error.append("Password harus mengandung minimal 1 nama Guru DuGaM")

                if error:
                    save_password(password, "GAGAL")
                    ketik("Password belum valid kekurangan:", warna=MERAH, delay=0.04, glitch=True, sound_type="tegang")
                    for i, e in enumerate(error, start=1):
                        ketik(f"{i}. {e}", warna=MERAH, delay=0.03, sound_type="tegang")
                else:
                    ketik("\nBERHASIL: Password yang kamu buat sudah kuat!", warna=HIJAU, delay=0.03)
                    
                    save_password(password, f"KUAT, {'KING ADMIN' if admin_mode else 'USER BIASA'}")

                    backroom_game(password)
                    break

        elif pilihan == 2:
            data = load_data()
            clear_screen()

            if not data:
                print("Belum ada password tersimpan.")
            else:
                print("=== DATA PASSWORD TERSIMPAN ===")
                for i, d in enumerate(data, 1):
                    print(f"{i}. {d}")

            input("\nTekan Enter untuk kembali...")
        elif pilihan == 3:
            clear_screen()
            statistik_data()
            input("\nTekan Enter untuk kembali...")

        elif pilihan == 4:
            hapus_data()
            input("\nTekan Enter untuk kembali...")

        elif pilihan == 5:
            ketik("Terimakasih!", warna=BIRU, delay=0.03)
            break

        else:
            print("Menu tidak tersedia.")
            time.sleep(1.5)


if __name__ == "__main__":
    main()

