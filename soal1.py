file1 = open('file1.txt', 'r', encoding='utf-8')
file2 = open('file2.txt', 'r', encoding='utf-8')

baris1 = file1.readlines()
baris2 = file2.readlines()

file1.close()
file2.close()

jumlah_baris = max(len(baris1), len(baris2))

for i in range(jumlah_baris):
    teks1 = baris1[i].strip() if i < len(baris1) else ''
    teks2 = baris2[i].strip() if i < len(baris2) else ''

    if teks1 == teks2:
        print(f"Baris {i+1} SAMA: {teks1}")
    else:
        print(f"Baris {i+1} BERBEDA:")
        print("  file1:", teks1)
        print("  file2:", teks2)
    print()
