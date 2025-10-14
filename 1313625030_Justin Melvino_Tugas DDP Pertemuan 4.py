print("Selamat datang di program analisis nilai-nilai siswa")
print("Dibuat oleh Justin Melvino")

list_nama_siswa = ['Adrian', 'Calvin', 'Darrell', 'Elroy', 'Fathi', 'Haikal', 'Nabil', 'Reynaldo', 'Sacrum', 'Zaki']
list_nilai_siswa = [84, 77, 80, 62, 96, 63, 83, 78, 90, 75]

jumlah_nilai = 0
n = len(list_nilai_siswa)

for i in range(n):
    print(i+1, list_nama_siswa[i], "\t", list_nilai_siswa[i])
    jumlah_nilai += list_nilai_siswa[i]

rata_rata = jumlah_nilai / n
print("Rata-rata nilai dari", n, "siswa tersebut adalah", rata_rata, ".")

siswa_remedial = ""
for i in range(n):
    if list_nilai_siswa[i] < rata_rata:
        siswa_remedial += list_nama_siswa[i] + ", "
    else:
        continue
print("Kepada siswa yang bernama", siswa_remedial, "mohon segera mengikuti remedial.")

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
    print("Selamat kepada", nama_juara, "karena telah menjadi juara dengan nilai tertinggi di kelas, yaitu", nilai_juara, ".")