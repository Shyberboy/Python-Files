def print_nama(variable):
    for name, value in globals().items():
        if value is variable:
            return name
    return None

def print_matriks(list, n):
    print(f"Berikut matriks {print_nama(list)}nya: ")
    for i in range(n):
        for j in range(n):
            print(list[i][j], end='\t')
        print()

def isi_matriks(list, n):
    for i in range(n):
        list.append([])
        for j in range(n):
            list[i].append(int(input(f"Elemen ({i+1}, {j+1}): ")))

def det3x3(list):
    return list[0][0]*list[1][1]*list[2][2] + list[0][1]*list[1][2]*list[2][0] + list[0][2]*list[1][0]*list[2][1] - (list[0][2]*list[1][1]*list[2][0] + list[0][0]*list[1][2]*list[2][1] + list[0][1]*list[1][0]*list[2][2])

awal = []
invers = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

isi_matriks(awal, 3)

print_matriks(awal, 3)

print(f"Determinan dari matriks awal adalah {det3x3(awal)}")

kofaktor = [[(awal[1][1]*awal[2][2] - awal[1][2]* awal[2][1]), (-(awal[1][0]*awal[2][2] - awal[1][2]* awal[2][0])), (awal[1][0]*awal[2][1] - awal[1][1]* awal[2][0])], 
            [(-(awal[0][1]*awal[2][2] - awal[0][2]* awal[2][1])), (awal[0][0]*awal[2][2] - awal[0][2]* awal[2][0]), (-(awal[0][0]*awal[2][1] - awal[0][1]* awal[2][0]))], 
            [(awal[0][1]*awal[1][2] - awal[0][2]* awal[1][1]), (-(awal[0][0]*awal[1][2] - awal[0][2]* awal[1][0])), (awal[0][0]*awal[1][1] - awal[0][1]* awal[1][0])]]

print_matriks(kofaktor, 3)

adjoin = [[kofaktor[0][0], kofaktor[1][0], kofaktor[2][0]], 
          [kofaktor[0][1], kofaktor[1][1], kofaktor[2][1]], 
          [kofaktor[0][2], kofaktor[1][2], kofaktor[2][2]]]

print_matriks(adjoin, 3)

for i in range(3):
    for j in range(3):
        invers[i][j] += adjoin[i][j] / det3x3(awal)

print_matriks(invers, 3)