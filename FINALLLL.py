import tkinter as tk
from tkinter import messagebox

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
        ),
        left=None
    )
)

pertanyaan_per_dimensi = {
    "I": [
        "Saya lebih suka menyendiri di waktu luang.",
        "Saya merasa capek setelah banyak berinteraksi sosial."
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
        "Saya membuat keputusan berdasarkan logika, bukan perasaan.",
        "Saya suka berargumen untuk menemukan kebenaran."
    ],
    "F": [
        "Saya mempertimbangkan perasaan orang lain dalam keputusan.",
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
    "ISTJ": "ISTJ (Logistician): Tipe ini dikenal sangat bertanggung jawab, terorganisir, dan berorientasi pada fakta.",
    "ISFJ": "ISFJ (Defender): Tipe ini sangat peduli, setia, dan suka membantu.",
    "INFJ": "INFJ (Advocate): Tipe ini idealis, visioner, dan sangat peduli dengan nilai-nilai kemanusiaan.",
    "INTJ": "INTJ (Architect): Tipe ini strategis, logis, dan suka merancang masa depan.",
    "ISTP": "ISTP (Virtuoso): Tipe ini suka eksplorasi, praktis, dan tangkas menyelesaikan masalah.",
    "ISFP": "ISFP (Adventurer): Mereka senang kebebasan, ekspresif, dan artistik.",
    "INFP": "INFP (Mediator): Mereka idealis, penuh empati, dan tertarik pada makna hidup.",
    "INTP": "INTP (Logician): Mereka analitis, suka berpikir mendalam, dan sangat ingin tahu.",
    "ESTP": "ESTP (Entrepreneur): Berani, spontan, suka tantangan dan aksi.",
    "ESFP": "ESFP (Entertainer): Ceria, ekspresif, dan suka menghibur orang.",
    "ENFP": "ENFP (Campaigner): Energik, penuh semangat, dan sangat ekspresif.",
    "ENTP": "ENTP (Debater): Mereka inovatif, suka tantangan, dan sangat komunikatif.",
    "ESTJ": "ESTJ (Executive): Pemimpin alami, suka keteraturan dan tanggung jawab.",
    "ESFJ": "ESFJ (Consul): Mereka ramah, suka bersosialisasi, dan peduli terhadap kesejahteraan kelompok.",
    "ENFJ": "ENFJ (Protagonist): Inspiratif, peka terhadap kebutuhan orang lain, dan pemimpin alami.",
    "ENTJ": "ENTJ (Commander): Ambisius, tegas, dan sangat terorganisir."
}

def prediksi(pohon, jawaban_user):
    if pohon.nilai is not None:
        return pohon.nilai
    nilai_fitur = jawaban_user.get(pohon.root)
    if nilai_fitur == 1:
        return prediksi(pohon.right, jawaban_user)
    else:
        return prediksi(pohon.left, jawaban_user)

class MBTIGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tes MBTI GUI")
        self.geometry("550x350")
        self.resizable(False, False)
        self.configure(bg="#f0f4f8")

        # Attributes for state
        self.nama = ""
        self.umur = ""
        self.daftar_dimensi = ["I", "E", "S", "N", "T", "F", "J", "P"]
        self.jawaban_dimensi = {dim: [] for dim in self.daftar_dimensi}
        self.current_dim_index = 0
        self.current_pertanyaan_index = 0

        # Start with intro frame
        self.intro_frame = tk.Frame(self, bg="#f0f4f8")
        self.intro_frame.pack(fill="both", expand=True)

        self.create_intro_widgets()

    def create_intro_widgets(self):
        lbl_title = tk.Label(self.intro_frame, text="Tes MBTI Sederhana", font=("Arial", 20, "bold"), bg="#f0f4f8")
        lbl_title.pack(pady=20)

        frm_form = tk.Frame(self.intro_frame, bg="#f0f4f8")
        frm_form.pack(pady=10)

        lbl_nama = tk.Label(frm_form, text="Masukkan nama kamu:", font=("Arial", 12), bg="#f0f4f8")
        lbl_nama.grid(row=0, column=0, sticky="w")
        self.entry_nama = tk.Entry(frm_form, font=("Arial", 12))
        self.entry_nama.grid(row=0, column=1, padx=10, pady=5)

        lbl_umur = tk.Label(frm_form, text="Masukkan umur kamu:", font=("Arial", 12), bg="#f0f4f8")
        lbl_umur.grid(row=1, column=0, sticky="w")
        self.entry_umur = tk.Entry(frm_form, font=("Arial", 12))
        self.entry_umur.grid(row=1, column=1, padx=10, pady=5)

        self.btn_start = tk.Button(self.intro_frame, text="Mulai Tes", font=("Arial", 14), bg="#4a90e2", fg="white",
                                   command=self.start_tes)
        self.btn_start.pack(pady=20)

    def start_tes(self):
        self.nama = self.entry_nama.get().strip()
        self.umur = self.entry_umur.get().strip()

        if not self.nama:
            messagebox.showwarning("Peringatan", "Nama tidak boleh kosong.")
            return
        if not self.umur.isdigit():
            messagebox.showwarning("Peringatan", "Umur harus berupa angka.")
            return

        self.intro_frame.destroy()
        self.create_question_frame()

    def create_question_frame(self):
        self.question_frame = tk.Frame(self, bg="#f0f4f8")
        self.question_frame.pack(fill="both", expand=True)

        # Question label
        self.lbl_dimension = tk.Label(self.question_frame, text="", font=("Arial", 16, "bold"), bg="#f0f4f8")
        self.lbl_dimension.pack(pady=(30, 5))

        self.lbl_question = tk.Label(self.question_frame, text="", font=("Arial", 14), wraplength=500, bg="#f0f4f8")
        self.lbl_question.pack(pady=(0, 20))

        # Buttons for answers
        btn_frame = tk.Frame(self.question_frame, bg="#f0f4f8")
        btn_frame.pack()

        self.btn_yes = tk.Button(btn_frame, text="Ya (Y)", font=("Arial", 14), width=10, bg="#4caf50", fg="white",
                                 command=lambda: self.record_answer(1))
        self.btn_yes.grid(row=0, column=0, padx=15)

        self.btn_no = tk.Button(btn_frame, text="Tidak (N)", font=("Arial", 14), width=10, bg="#f44336", fg="white",
                                command=lambda: self.record_answer(0))
        self.btn_no.grid(row=0, column=1, padx=15)

        self.update_question()

    def update_question(self):
        if self.current_dim_index >= len(self.daftar_dimensi):
            # All questions done
            self.question_frame.destroy()
            self.show_result()
            return
    
        current_dim = self.daftar_dimensi[self.current_dim_index]
        questions = pertanyaan_per_dimensi[current_dim]

        if self.current_pertanyaan_index >= len(questions):
            # Dimension done, next dimension
            self.current_dim_index += 1
            self.current_pertanyaan_index = 0
            self.update_question()
            return

        # Update labels
        self.lbl_dimension.config(text=f"Dimensi: {current_dim}")
        self.lbl_question.config(text=questions[self.current_pertanyaan_index])

    def record_answer(self, answer):
        current_dim = self.daftar_dimensi[self.current_dim_index]
        self.jawaban_dimensi[current_dim].append(answer)
        self.current_pertanyaan_index += 1
        self.update_question()

    def show_result(self):
        hasil = {}
        pasangan = [("I","E"), ("S","N"), ("T","F"), ("J","P")]
        for sisi1, sisi2 in pasangan:
            setuju_sisi1 = sum(self.jawaban_dimensi[sisi1])
            setuju_sisi2 = sum(self.jawaban_dimensi[sisi2])
            if setuju_sisi1 > setuju_sisi2:
                hasil[sisi1] = 1
                hasil[sisi2] = 0
            else:
                hasil[sisi1] = 0
                hasil[sisi2] = 1

        tipe_mbti = prediksi(root_pohon, hasil)
        penjelasan = penjelasan_mbti.get(tipe_mbti, "Maaf, tipe belum ada deskripsi.")

        self.result_frame = tk.Frame(self, bg="#f0f4f8")
        self.result_frame.pack(fill="both", expand=True, padx=20, pady=20)

        lbl_title = tk.Label(self.result_frame, text="=== Hasil Tes MBTI ===", font=("Arial", 18, "bold"), bg="#f0f4f8")
        lbl_title.pack(pady=(0, 15))

        lbl_name_age = tk.Label(self.result_frame, text=f"Nama: {self.nama}, Umur: {self.umur}", font=("Arial", 14), bg="#f0f4f8")
        lbl_name_age.pack(pady=5)

        lbl_result = tk.Label(self.result_frame, text=f"Tipe MBTI kamu: {tipe_mbti}", font=("Arial", 16, "bold"), bg="#f0f4f8", fg="#2c3e50")
        lbl_result.pack(pady=10)

        lbl_penjelasan = tk.Label(self.result_frame, text=penjelasan, font=("Arial", 12), wraplength=500, bg="#f0f4f8", justify="left")
        lbl_penjelasan.pack(pady=10)

        btn_exit = tk.Button(self.result_frame, text="Keluar", font=("Arial", 14), bg="#e74c3c", fg="white", command=self.destroy)
        btn_exit.pack(pady=20)


if __name__ == "__main__":
    app = MBTIGUI()
    app.mainloop()

