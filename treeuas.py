# Struktur data pohon keputusan dengan atribut root, right, left
class NodePohon:
    def __init__(self, root=None, right=None, left=None, nilai=None):
        self.root = root        # nama fitur / pertanyaan
        self.right = right      # cabang jawaban 1 (Setuju / Ya)
        self.left = left        # cabang jawaban 0 (Tidak Setuju / Tidak)
        self.nilai = nilai      # nilai tipe MBTI (daun)

    def to_dict(self):
        if self.nilai is not None:
            return {"nilai": self.nilai}
        return {
            "root": self.root,
            "right": self.right.to_dict(),
            "left": self.left.to_dict()
        }

    @staticmethod
    def from_dict(data):
        if "nilai" in data:
            return NodePohon(nilai=data["nilai"])
        return NodePohon(
            root=data["root"],
            right=NodePohon.from_dict(data["right"]),
            left=NodePohon.from_dict(data["left"])
        )

# Fungsi prediksi
def prediksi(pohon, jawaban_user):
    if pohon.nilai is not None:
        return pohon.nilai
    nilai_fitur = jawaban_user.get(pohon.root)
    if nilai_fitur == 1:
        return prediksi(pohon.right, jawaban_user)
    else:
        return prediksi(pohon.left, jawaban_user)

# Pertanyaan per dimensi
pertanyaan_per_dimensi = {
    "Introvert": [
        "Saya lebih nyaman menyendiri daripada berada di keramaian.",
        "Saya merasa lelah setelah banyak bersosialisasi.",
        "Saya suka merenung dan berpikir sendiri.",
        "Saya sering menghindari pembicaraan basa-basi.",
        "Saya lebih memilih komunikasi lewat tulisan daripada bicara langsung."
    ],
    "Sensing": [
        "Saya lebih fokus pada fakta daripada teori.",
        "Saya memperhatikan detail kecil dalam pekerjaan saya.",
        "Saya percaya pada pengalaman langsung daripada intuisi.",
        "Saya lebih suka instruksi yang jelas dan praktis.",
        "Saya mengandalkan panca indera untuk memahami dunia."
    ],
    "Thinking": [
        "Saya lebih memprioritaskan logika daripada perasaan dalam mengambil keputusan.",
        "Saya merasa nyaman memberi kritik jika diperlukan.",
        "Saya lebih percaya pada keadilan daripada belas kasihan.",
        "Saya memilih keefisienan daripada keharmonisan.",
        "Saya memisahkan emosi dari analisis saat bekerja."
    ],
    "Judging": [
        "Saya suka merencanakan sesuatu jauh-jauh hari.",
        "Saya merasa tidak nyaman jika jadwal berubah.",
        "Saya suka membuat daftar tugas (to-do list) dan mengikutinya.",
        "Saya merasa puas setelah menyelesaikan pekerjaan tepat waktu.",
        "Saya suka semua hal berjalan sesuai rencana."
    ]
}

# Penjelasan hasil MBTI
penjelasan_mbti = {
    "ISTJ": "ISTJ (Logistician): Tipe ini dikenal sangat bertanggung jawab, terorganisir, dan berorientasi pada fakta. Cocok untuk pekerjaan yang memerlukan struktur dan perencanaan.",
    "ISFJ": "ISFJ (Defender): Tipe ini sangat peduli, setia, dan suka membantu. Mereka cenderung diam namun perhatian pada kebutuhan orang lain.",
    "INTJ": "INTJ (Architect): Tipe ini strategis, logis, dan suka merancang masa depan. Mereka lebih nyaman dengan teori dan konsep besar.",
    "INFJ": "INFJ (Advocate): Tipe ini idealis, visioner, dan sangat peduli dengan nilai-nilai kemanusiaan. Mereka memiliki intuisi yang tajam.",
    "ESTJ": "ESTJ (Executive): Tipe ini pemimpin alami, suka mengambil alih tanggung jawab, dan mengatur segala sesuatu dengan efisien.",
    "ESFJ": "ESFJ (Consul): Mereka ramah, suka bersosialisasi, dan peduli terhadap kesejahteraan kelompok. Sangat cocok jadi pendukung sosial.",
    "ENTP": "ENTP (Debater): Mereka inovatif, suka tantangan, dan sangat komunikatif. Senang mencoba hal-hal baru dan memecahkan masalah secara kreatif.",
    "ENFP": "ENFP (Campaigner): Energik, penuh semangat, dan sangat ekspresif. Mereka suka menjalin hubungan dan menginspirasi orang lain."
}

# Struktur pohon keputusan dengan atribut root, right, left
root = NodePohon(
    root="Introvert",
    right=NodePohon(
        root="Sensing",
        right=NodePohon(
            root="Thinking",
            right=NodePohon(nilai="ISTJ"),
            left=NodePohon(nilai="ISFJ")
        ),
        left=NodePohon(
            root="Judging",
            right=NodePohon(nilai="INTJ"),
            left=NodePohon(nilai="ENTP")
        )
    ),
    left=NodePohon(
        root="Sensing",
        right=NodePohon(
            root="Thinking",
            right=NodePohon(nilai="ESTJ"),
            left=NodePohon(nilai="ESFJ")
        ),
        left=NodePohon(
            root="Judging",
            right=NodePohon(nilai="INFJ"),
            left=NodePohon(nilai="ENFP")
        )
    )
)

def main():
    print("=== Tes MBTI Sederhana ===\n")
    jawaban_dimensi = {}

    # Loop per dimensi dan pertanyaan
    for dimensi, daftar_pertanyaan in pertanyaan_per_dimensi.items():
        skor = 0
        print(f"\nDimensi: {dimensi}")
        for idx, pertanyaan in enumerate(daftar_pertanyaan, start=1):
            while True:
                try:
                    jawab = input(f"{idx}. {pertanyaan} (0=tidak setuju / 1=setuju): ").strip()
                    if jawab not in ["0", "1"]:
                        print("Mohon masukkan angka 0 atau 1 saja.")
                        continue
                    skor += int(jawab)
                    break
                except Exception as e:
                    print("Input tidak valid, coba lagi.")
        # Jika setuju 3 atau lebih berarti 1, kalau kurang berarti 0
        jawaban_dimensi[dimensi] = 1 if skor >= 3 else 0

    # Prediksi hasil MBTI
    hasil = prediksi(root, jawaban_dimensi)
    print("\nHasil Prediksi Tipe MBTI Kamu:", hasil)

    # Penjelasan tipe MBTI
    print("\nPenjelasan Tipe Kamu:")
    print(penjelasan_mbti.get(hasil, "Penjelasan tidak tersedia."))

if __name__ == "__main__":
    main()
