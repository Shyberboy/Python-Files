n = int(input("Masukkan bilangan bulat positif: "))
jumlah = 0

if n < 1:
    print("Angkanya kurang dari sama dengan 0, tolong ulangi program dan masukkan bilangan yang valid.")
else:
    for i in range(n+1):
        jumlah += i
    print(f'Jumlah dari bilangan 1 sampai {n} adalah {jumlah}')