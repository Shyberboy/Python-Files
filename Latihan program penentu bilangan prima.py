x = int(input("Masukkan bilangan asli (contohnya 1, 2, 3, ...): "))
faktor = ""

if x <= 0:
    print("Angkanya kurang dari sama dengan 0, tolong ulangi program dan masukkan bilangan yang valid.")
else:
    for i in range(1, x + 1):
        if x % i == 0:
            if i < x:
                faktor += f'{i}, '
            else:
                faktor += f'{i}.'
    if faktor == f'1, {x}.':
        print(f'Bilangan {x} termasuk bilangan prima karena hanya memiliki dua faktor, yaitu 1 dan {x} itu sendiri.')
    elif x == 1:
        print(f'Bilangan {x} bukan bilangan prima karena hanya memiliki 1 faktor, yaitu 1 itu sendiri.')
    else:
        print(f'Bilangan {x} bukan bilangan prima karena memiliki lebih dari 2 faktor, yaitu {faktor}')