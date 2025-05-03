nama_file = 'soal.txt'
print("nama file1:", nama_file)

with open(nama_file, 'r', encoding='utf-8') as file:
    for baris in file:
        if '||' in baris:
            soal, kunci = baris.strip().split('||')
            soal = soal.strip()
            kunci = kunci.strip().lower()
            print(soal)
            jawaban = input("Jawab: ").strip().lower()
            if jawaban == kunci:
                print("Jawaban benar!\n")
            else:
                print("Jawaban salah!\n")
