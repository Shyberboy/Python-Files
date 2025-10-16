matriks_a = []
matriks_b = []
matriks_perkalian = []

baris_a = int(input("Banyak baris matriks A: "))
kolom_a = int(input("Banyak kolom matriks A: "))
baris_b = int(input("Banyak baris matriks B: "))
kolom_b = int(input("Banyak kolom matriks B: "))

if baris_a <= 0 or kolom_a <= 0 or baris_b <= 0 or kolom_b <= 0:
    print("Mohon masukkan jumlah baris dan kolom yang valid.")
elif kolom_a != baris_b:
    print(f"Matriks A({baris_a}x{kolom_a}) dan B({baris_b}x{kolom_b}) tidak dapat dikalikan karena banyak kolom matriks A tidak sama dengan baris matriks B.")
else:
    print("Silakan masukkan matriks A...")
    for i in range(baris_a):
        matriks_a.append([])
        for j in range(kolom_a):
            matriks_a[i].append(int(input(f"Elemen A({i+1}, {j+1}): ")))

    print("Matriks A")
    for i in range(baris_a):
        for j in range(kolom_a):
            print(matriks_a[i][j], end='\t')
        print()

    print("Sekarang input matriks B yang akan dikalikan ke matriks A...")
    for i in range(baris_b):
        matriks_b.append([])
        for j in range(kolom_b):
            matriks_b[i].append(int(input(f"Elemen B({i+1}, {j+1}): ")))

    print("Matriks B")
    for i in range(baris_b):
        for j in range(kolom_b):
            print(matriks_b[i][j], end='\t')
        print()

    for i in range(baris_a):
        matriks_perkalian.append([])
        for j in range(kolom_b):
            matriks_perkalian[i].append(0)
            for k in range(kolom_a):
                matriks_perkalian[i][j] += matriks_a[i][k] * matriks_b[k][j]

    print("Berikut matriks hasil perkalian matriks A x B: ")
    print("Matriks A x B")
    for i in range(baris_a):
        for j in range(kolom_b):
            print(matriks_perkalian[i][j], end='\t')
        print()