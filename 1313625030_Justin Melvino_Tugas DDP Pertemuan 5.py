ulang_program = 'y'
print("Selamat datang di program pencari faktor persekutuan oleh Justin Melvino!")

while ulang_program == 'y' or 'Y':
    a = int(input("Masukkan bilangan bulat positif pertama: "))
    b = int(input("Masukkan bilangan bulat positif kedua: "))
    faktor_persekutuan = ""
    
    # Karena faktor persekutuan dari dua bilangan harus <= bilangan terkecil dari dua bilangan tersebut, maka akan dibuat variabel batas
    if a <= b:
        batas = a
    else: 
        batas = b

    if a < 1 or b < 1:
        print("Salah satu bilangannya kurang dari sama dengan 0, tolong masukkan bilangan yang valid.")
    else:
        for i in range(1, batas+1):
            if a % i == 0 and b % i == 0:
                faktor_persekutuan += f'{i}, '
        print(f"Bilangan {a} dan {b} memiliki {faktor_persekutuan}sebagai faktor persekutuan mereka.")


    ulang_program = input("Apakah Anda ingin menggunakan program ini lagi? (y/n): ")