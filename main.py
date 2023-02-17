from module import Kategoria

kategoriak:list[Kategoria] = []
file = open(file='titanic.txt', mode='r', encoding='utf-8')
for s in file: kategoriak.append(Kategoria(s))

print(f'2. feladat: {len(kategoriak)} db')

osz:int = 0
for k in kategoriak:
    osz += (k.eltuntek + k.tulelok)
print(f'3. feladat: {osz} fő')

ksz:str = input('4. feladat: Kulcsszó: ')
vt:bool = False
for k in kategoriak:
    if ksz in k.nev:
        print('\tVan találat!')
        vt = True
        break
else: print('\tNincs találat!')

if vt:
    print('5. feladat:')
    for k in kategoriak:
        if ksz in k.nev:
            print(f'\t{k.nev} {k.tulelok + k.eltuntek} fő')

sh:list[str] = []
for k in kategoriak:
    if k.eltuntek > (k.eltuntek + k.tulelok) * .6:
        sh.append(k.nev)
print('6. feladat:')
for n in sh:
    print(f'\t{n}')

m:int = 0
for i in range(1, len(kategoriak)):
    if kategoriak[i].tulelok > kategoriak[m].tulelok:
        m = i
print(f'7. feladat: {kategoriak[m].nev}')