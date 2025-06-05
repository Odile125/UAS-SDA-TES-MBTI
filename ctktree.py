import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# ==== Struktur Data & Logika MBTI ====

class NodePohon:
    def __init__(self, root=None, right=None, left=None, nilai=None):
        self.root = root
        self.right = right
        self.left = left
        self.nilai = nilai

root_pohon = NodePohon(
    root="I",
    right=NodePohon(
        root="S",
        right=NodePohon(
            root="T",
            right=NodePohon(
                root="J",
                right=NodePohon(nilai="ISTJ"),
                left=NodePohon(nilai="ISTP")
            ),
            left=NodePohon(
                root="P",
                right=NodePohon(nilai="ISFJ"),
                left=NodePohon(nilai="ISFP")
            )
        ),
        left=NodePohon(
            root="F",
            right=NodePohon(
                root="J",
                right=NodePohon(nilai="INFJ"),
                left=NodePohon(nilai="INFP")
            ),
            left=NodePohon(
                root="P",
                right=NodePohon(nilai="INTJ"),
                left=NodePohon(nilai="INTP")
            )
        )
    ),
    left=NodePohon(
        root="E",
        right=NodePohon(
            root="S",
            right=NodePohon(
                root="T",
                right=NodePohon(
                    root="J",
                    right=NodePohon(nilai="ESTJ"),
                    left=NodePohon(nilai="ESTP")
                ),
                left=NodePohon(
                    root="P",
                    right=NodePohon(nilai="ESFJ"),
                    left=NodePohon(nilai="ESFP")
                )
            ),
            left=NodePohon(
                root="F",
                right=NodePohon(
                    root="J",
                    right=NodePohon(nilai="ENFJ"),
                    left=NodePohon(nilai="ENFP")
                ),
                left=NodePohon(
                    root="P",
                    right=NodePohon(nilai="ENTJ"),
                    left=NodePohon(nilai="ENTP")
                )
            )
        )
    )
)

pertanyaan_per_dimensi = {
    "I": [
        "Saya lebih suka menyendiri di waktu luang.",
        "Saya merasa capek setelah banyak interaksi sosial."
    ],
    "E": [
        "Saya senang bertemu orang baru.",
        "Saya merasa bersemangat setelah berbicara dengan banyak orang.",
        "Saya cenderung berbicara daripada mendengarkan."
    ],
    "S": [
        "Saya fokus pada fakta, bukan kemungkinan.",
        "Saya lebih suka pengalaman langsung daripada teori."
    ],
    "N": [
        "Saya suka membayangkan masa depan.",
        "Saya tertarik pada ide-ide abstrak.",
        "Saya sering memikirkan berbagai kemungkinan."
    ],
    "T": [
        "Saya membuat keputusan berdasarkan logika.",
        "Saya suka berargumen untuk menemukan kebenaran."
    ],
    "F": [
        "Saya mempertimbangkan perasaan orang lain.",
        "Saya lebih peduli hubungan daripada kebenaran logis.",
        "Saya merasa tidak nyaman jika membuat orang lain kecewa."
    ],
    "J": [
        "Saya suka membuat rencana dan mengikuti jadwal.",
        "Saya merasa gelisah jika rencana berubah."
    ],
    "P": [
        "Saya lebih suka fleksibel daripada membuat rencana.",
        "Saya santai menghadapi perubahan rencana.",
        "Saya sering menyelesaikan tugas di menit terakhir."
    ]
}

penjelasan_mbti = {
    "ISTJ": "ISTJ (Logistician): Tanggung jawab, logis, dan realistis.",
    "ISFJ": "ISFJ (Defender): Setia, hangat, dan suka menolong.",
    "INFJ": "INFJ (Advocate): Idealistik, introspektif, dan visioner.",
    "INTJ": "INTJ (Architect): Strategis, independen, dan tegas.",
    "ISTP": "ISTP (Virtuoso): Praktis, logis, dan suka tantangan teknis.",
    "ISFP": "ISFP (Adventurer): Tenang, artistik, dan fleksibel.",
    "INFP": "INFP (Mediator): Penuh empati, idealis, dan sensitif.",
    "INTP": "INTP (Logician): Analitis, imajinatif, dan ingin tahu.",
    "ESTP": "ESTP (Entrepreneur): Spontan, energik, dan praktis.",
    "ESFP": "ESFP (Entertainer): Ceria, ekspresif, dan suka menghibur.",
    "ENFP": "ENFP (Campaigner): Kreatif, ramah, dan penuh semangat.",
    "ENTP": "ENTP (Debater): Inovatif, suka berdebat, dan dinamis.",
    "ESTJ": "ESTJ (Executive): Terorganisir, realistis, dan pemimpin alami.",
    "ESFJ": "ESFJ (Consul): Sosial, empatik, dan suportif.",
    "ENFJ": "ENFJ (Protagonist): Inspiratif, bertanggung jawab, dan perhatian.",
    "ENTJ": "ENTJ (Commander): Ambisius, strategis, dan tegas."
}

def prediksi(pohon, jawaban_user):
    if pohon.nilai is not None:
        return pohon.nilai
    nilai_fitur = jawaban_user.get(pohon.root)
    if nilai_fitur == 1:
        return prediksi(pohon.right, jawaban_user)
    else:
        return prediksi(pohon.left, jawaban_user)

# ==== GUI ====

class MBTIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tes MBTI - GUI")
        self.root.geometry("320x450")  # Ukuran iPhone 13

        self.nama = ""
        self.umur = ""
        self.jawaban_dimensi = {k: [] for k in pertanyaan_per_dimensi.keys()}
        self.index_dimensi = 0
        self.index_pertanyaan = 0
        self.dimensi_urut = list(pertanyaan_per_dimensi.keys())

        self.frame = tk.Frame(root, bg="white")
        self.frame.pack(fill="both", expand=True)

        self.show_home()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def show_home(self):
        self.clear_frame()

        try:
            img = Image.open("hs1.png")
            img = img.resize((390, 300), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            label_img = tk.Label(self.frame, image=photo, bg="white")
            label_img.image = photo
            label_img.pack(pady=10)
        except:
            tk.Label(self.frame, text="Gambar 'hs1.png' tidak ditemukan", bg="white", fg="red").pack(pady=10)

        tk.Label(self.frame, text="Selamat Datang di Tes MBTI", font=("Helvetica", 18, "bold"), bg="white").pack(pady=10)
        tk.Button(self.frame, text="Kenali Dirimu", font=("Helvetica", 14), command=self.show_form).pack(pady=10)

    def show_form(self):
        self.clear_frame()
        tk.Label(self.frame, text="Masukkan Nama:", bg="white").pack()
        self.entry_nama = tk.Entry(self.frame)
        self.entry_nama.pack()

        tk.Label(self.frame, text="Masukkan Umur:", bg="white").pack()
        self.entry_umur = tk.Entry(self.frame)
        self.entry_umur.pack()

        tk.Button(self.frame, text="Mulai Tes", command=self.start_test).pack(pady=10)

    def start_test(self):
        self.nama = self.entry_nama.get()
        self.umur = self.entry_umur.get()
        if not self.nama or not self.umur.isdigit():
            messagebox.showerror("Error", "Nama dan umur wajib diisi dengan benar.")
            return
        self.index_dimensi = 0
        self.index_pertanyaan = 0
        self.jawaban_dimensi = {k: [] for k in pertanyaan_per_dimensi.keys()}
        self.show_question()

    def show_question(self):
        self.clear_frame()
        dimensi = self.dimensi_urut[self.index_dimensi]
        pertanyaan = pertanyaan_per_dimensi[dimensi][self.index_pertanyaan]
        tk.Label(self.frame, text=f"Dimensi: {dimensi}", font=("Helvetica", 14), bg="white").pack(pady=10)
        tk.Label(self.frame, text=pertanyaan, wraplength=350, font=("Helvetica", 12), bg="white").pack(pady=10)
        tk.Button(self.frame, text="Ya", width=15, command=lambda: self.answer(1)).pack(pady=5)
        tk.Button(self.frame, text="Tidak", width=15, command=lambda: self.answer(0)).pack(pady=5)

    def answer(self, nilai):
        dimensi = self.dimensi_urut[self.index_dimensi]
        self.jawaban_dimensi[dimensi].append(nilai)
        self.index_pertanyaan += 1

        if self.index_pertanyaan >= len(pertanyaan_per_dimensi[dimensi]):
            self.index_dimensi += 1
            self.index_pertanyaan = 0

        if self.index_dimensi >= len(self.dimensi_urut):
            self.show_result()
        else:
            self.show_question()

    def show_result(self):
        hasil = {}
        pasangan = [("I", "E"), ("S", "N"), ("T", "F"), ("J", "P")]
        for sisi1, sisi2 in pasangan:
            if sum(self.jawaban_dimensi[sisi1]) > sum(self.jawaban_dimensi[sisi2]):
                hasil[sisi1] = 1
                hasil[sisi2] = 0
            else:
                hasil[sisi1] = 0
                hasil[sisi2] = 1
        tipe = prediksi(root_pohon, hasil)

        self.clear_frame()
        tk.Label(self.frame, text=f"Hasil MBTI untuk {self.nama} ({self.umur} tahun):", bg="white", font=("Helvetica", 14)).pack(pady=10)
        tk.Label(self.frame, text=f"Tipe MBTI kamu: {tipe}", font=("Helvetica", 18, "bold"), bg="white", fg="blue").pack(pady=10)
        tk.Label(self.frame, text=penjelasan_mbti.get(tipe, ""), wraplength=360, bg="white", font=("Helvetica", 12)).pack(pady=10)

# ==== Jalankan Aplikasi ====
if __name__ == "__main__":
    root = tk.Tk()
    app = MBTIApp(root)
    root.mainloop()
