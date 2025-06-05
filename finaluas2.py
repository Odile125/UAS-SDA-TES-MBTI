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

def tes_mbti():
    print("Tes MBTI Sederhana (jawab dengan 'y' untuk setuju, 'n' untuk tidak)\n")
    
    nama = input("Masukkan nama kamu: ")
    umur = input("Masukkan umur kamu: ")
    while not umur.isdigit():
        print("Umur harus angka.")
        umur = input("Masukkan umur kamu: ")
    
    daftar_dimensi = ["I", "E", "S", "N", "T", "F", "J", "P"]
    jawaban_dimensi = {dim: [] for dim in daftar_dimensi}
    
    for dimensi in daftar_dimensi:
        print(f"\nDimensi: {dimensi}")
        for pertanyaan in pertanyaan_per_dimensi[dimensi]:
            while True:
                jawaban = input(f"{pertanyaan} (y/n): ").lower()
                if jawaban in ['y', 'n']:
                    jawaban_dimensi[dimensi].append(1 if jawaban == 'y' else 0)
                    break
                else:
                    print("Jawaban harus 'y' atau 'n'.")
    
    hasil = {}
    pasangan = [("I","E"), ("S","N"), ("T","F"), ("J","P")]
    for sisi1, sisi2 in pasangan:
        setuju_sisi1 = sum(jawaban_dimensi[sisi1])
        setuju_sisi2 = sum(jawaban_dimensi[sisi2])
        if setuju_sisi1 > setuju_sisi2:
            hasil[sisi1] = 1
            hasil[sisi2] = 0
        else:
            hasil[sisi1] = 0
            hasil[sisi2] = 1
    
    tipe_mbti = prediksi(root_pohon, hasil)
    
    print("\n=== Hasil Tes MBTI ===")
    print(f"Nama: {nama}, Umur: {umur}")
    print(f"Tipe MBTI kamu: {tipe_mbti}")
    print(penjelasan_mbti.get(tipe_mbti, "Maaf, tipe belum ada deskripsi."))
    print("======================")

if __name__ == "__main__":
    tes_mbti()
