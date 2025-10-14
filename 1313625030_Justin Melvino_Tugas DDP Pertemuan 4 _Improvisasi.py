print("Selamat datang di program analisis nilai-nilai siswa")
print("Dibuat oleh Justin Melvino")

list_nama_siswa = []
list_nilai_siswa = []
jumlah_nilai = 0

n = int(input("Masukkan banyak siswa yang ingin dianalisis: "))
if n <= 0:
    print("Banyak siswa yang diinput adalah bilangan asli, minimal 1.")
else:
    x = 0
    while x < n:
        nama_siswa = str(input(f"Masukkan nama siswa ke-{x+1}: "))
        nilai_siswa = int(input(f"Masukkan nilai dari {nama_siswa}: "))
        if nilai_siswa < 0:
            print("Tolong masukkan nilai yang valid (harus bernilai positif dan tidak berkoma).")
        elif 0 <= nilai_siswa <= 100:
            list_nama_siswa.append(nama_siswa)
            list_nilai_siswa.append(nilai_siswa)
            x += 1
        else:
            print("Tolong masukkan nilai yang tidak lebih dari 100.")
    for i in range(n):
        print(f"{i+1}. {list_nama_siswa[i]} \t {list_nilai_siswa[i]}")
        jumlah_nilai += list_nilai_siswa[i]
    rata_rata = jumlah_nilai / n
    print(f"Rata-rata nilai dari {n} siswa tersebut adalah {rata_rata}.")

    siswa_remedial = ""
    for i in range(n):
        if list_nilai_siswa[i] < rata_rata:
            siswa_remedial += list_nama_siswa[i] + ", "
        else:
            continue
    print(f"Kepada siswa yang bernama {siswa_remedial}mohon segera mengikuti remedial.")

    nama_juara = list_nama_siswa[0]
    nilai_juara = list_nilai_siswa[0]
    banyak_juara = 1

    for i in range(1, n):
        if list_nilai_siswa[i] > nilai_juara:
            nilai_juara = list_nilai_siswa[i]
            nama_juara = list_nama_siswa[i]
            banyak_juara = 1
        elif list_nilai_siswa[i] == nilai_juara:
            nama_juara += " dan " + list_nama_siswa[i]
            banyak_juara += 1
        else:
            continue
    
    if banyak_juara == n:
        print("Semua siswa nilainya sama, berarti sayang sekali tidak ada juara :(")
    else:
        print(f"Selamat kepada {nama_juara} karena telah menjadi juara dengan nilai tertinggi di kelas, yaitu {nilai_juara}.")
    