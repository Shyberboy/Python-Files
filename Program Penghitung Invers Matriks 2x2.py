matriks_awal = []
matriks_invers = [[0, 0],[0, 0]]

for i in range(2):
    matriks_awal.append([])
    for j in range(2):
        matriks_awal[i].append(int(input(f"Elemen matriks ({i+1}, {j+1}): ")))

print("Matriks awal")
for i in range(2):
    for j in range(2):
        print(matriks_awal[i][j], end="\t")
    print()

determinan = matriks_awal[0][0] * matriks_awal[1][1] - matriks_awal[0][1] * matriks_awal[1][0]
print(f"Determinan dari matriks awal adalah {determinan}")

matriks_invers[0][0] += matriks_awal[1][1] / determinan
matriks_invers[0][1] -= matriks_awal[0][1] / determinan
matriks_invers[1][0] -= matriks_awal[1][0] / determinan
matriks_invers[1][1] += matriks_awal[0][0] / determinan

print("Invers dari matriks awal")
for i in range(2):
    for j in range(2):
        print(matriks_invers[i][j], end="\t")
    print()