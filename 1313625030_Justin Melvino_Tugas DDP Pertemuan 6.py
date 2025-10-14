#Dibuat oleh Justin Melvino
matriks_a = [[1,2,3],[4,5,6]]
matriks_b = [[9,8,7],[6,5,4],[3,2,1]]

baris_a = len(matriks_a)
kolom_a = len(matriks_a[0])
baris_b = len(matriks_b)
kolom_b = len(matriks_b[0])

if baris_a <= 0 or kolom_a <= 0 or baris_b <= 0 or kolom_b <= 0:
    print("Mohon masukkan jumlah baris dan kolom yang valid.")
elif kolom_a != baris_b:
    print(f"Matriks A({baris_a}x{kolom_a}) dan B({baris_b}x{kolom_b}) tidak dapat dikalikan karena banyak kolom matriks A tidak sama dengan baris matriks B.")
else:
    print("Matriks A")
    for i in range(baris_a):
        for j in range(kolom_a):
            print(matriks_a[i][j], end='\t')
        print()

    print("Matriks B")
    for i in range(baris_b):
        for j in range(kolom_b):
            print(matriks_b[i][j], end='\t')
        print()

    matriks_perkalian = [[0 for x in range(kolom_b)] for x in range(baris_a)]

    for i in range(baris_a):
        for j in range(kolom_b):
            for k in range(kolom_a):
                matriks_perkalian[i][j] += matriks_a[i][k] * matriks_b[k][j]

    print("Berikut matriks hasil perkalian matriks A x B: ")
    print("Matriks A x B")
    for i in range(baris_a):
        for j in range(kolom_b):
            print(matriks_perkalian[i][j], end='\t')
        print()