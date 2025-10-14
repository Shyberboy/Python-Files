ulang_program = 'y'
print("Selamat datang di program pencari faktor persekutuan oleh Justin Melvino!")

while ulang_program == 'y' or 'Y':
    list_bilangan = []
    faktor_persekutuan = []
    k = 1
    n = int(input("Masukkan banyak bilangan yang ingin dicari faktor persekutuannya: "))
    while k <= n:
        bilangan = int(input(f"Masukkan bilangan ke-{k}: "))
        if bilangan < 1:
            print("Mohon masukkan bilangan asli (minimal 1).")
        else:
            list_bilangan.append(bilangan)
            k += 1
    
    batas = min(list_bilangan)

    for i in range(1, batas+1):
        if all(b % i == 0 for b in list_bilangan):
            faktor_persekutuan.append(i)
    print(f"Bilangan {list_bilangan} memiliki {faktor_persekutuan} sebagai faktor persekutuan mereka.")


    ulang_program = input("Apakah Anda ingin menggunakan program ini lagi? (y/n): ")