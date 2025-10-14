x = int(input("Masukkan bilangan bulat positif yang ingin dicari faktornya: "))
faktor_x = ""

if x < 1:
    print("Angkanya kurang dari sama dengan 0, tolong ulangi program dan masukkan bilangan yang valid.")
else:
    for i in range(1, x+1):
        if x % i == 0:
            if x == i:
                faktor_x += str(i) 
            else:
                faktor_x += str(i) + ", "
        i += 1
    print(f'Faktor dari bilangan {x} adalah {faktor_x}')