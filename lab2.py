import math
#Zadanie1
print('Zadanie 1')
przyklad1 = math.exp(10)
print(przyklad1)

przyklad2 = math.pow(math.log(5+math.pow(math.sin(8),2)),1/6)
print(przyklad2)

przyklad3 = math.floor(3.55)
print(przyklad3)

przyklad4 = math.ceil(4.80)
print(przyklad4)

#Zadanie 2
print('ZADANIE 2')
a="MICHALINA"
b="SOBKIEWICZ"
x = a.capitalize()
y = b.capitalize()
print(x)
print(y)

#Zadanie3
print('ZADANIE 3')
tekst= "Oh oh oh oh oh, oh oh oh oh, oh oh oh Caught in a bad romance Oh oh oh oh oh, oh oh oh oh, oh-oh-oh Caught in a bad romance"
licz = tekst.count('oh')
print(licz)

#Zadanie4
print('ZADANIE 4')
imie=['M','i','c','h','a','l','i','n','a']
print(imie[0])
print(imie[8])

#Zadanie5
print('ZADANIE 5')
podziel=tekst.split() #to jest zapisywane w liście
print(podziel)
print(podziel[12])

#Zadanie6
print('ZADANIE 6')

ciag1 = "abcde"
print(ciag1)
print("{}".format(ciag1))

liczba2 = 293.12391
print(liczba2)
print("{:.3f}".format(liczba2))
#przed f ilosc liczb ktore maja byc wyswietlone po przecinku

liczba3 = 0xff1e
print(liczba3)
print('0x{:x}'.format(liczba3))
print('{:x}'.format(liczba3))
#w zależności czy duzy czy maly x wynik wyswietli sie wielkimi badz malymi literami

#Zadanie7
print('ZADANIE 7')
sporty=['siatkowka', 'pilka reczna', 'gimnastyka artystyczna']
sporty.reverse()
print(sporty)
sporty.extend(['koszykowka','pilka nozna'])
print(sporty)

#Zadanie8
print('ZADANIE 8')
slownik = {'str': 'strona', 'itp': 'i tym podobne', 'itd':'i tak dalej', 'RP':'Rzeczpospolita Polska'}
print(slownik)
print(slownik.keys())
print(slownik.values())

#Zadanie9
print('ZADANIE 9')
rokwydaniagry = {'TheSims1': '2000', 'TheSims2': '2004', 'TheSims3': '2009', 'TheSims4': '2014'}
iloscelementow = len(rokwydaniagry)
print(iloscelementow)

#Zadanie10
print('ZADANIE 10')
zdanie = input("Wpisz jakieś zdanie: ")
liczba_a = 0
for znak in zdanie:
    if znak == 'a' or znak == 'A':
        liczba_a += 1
print("Liczba wystąpień litery 'a':", liczba_a)

#Zadabnie11
print('ZADANIE 11')
a= int(input("Podaj liczbe a"))
b= int(input("Podaj liczbe b rozna od a"))
c= int(input("Podaj liczbe c rozna od a i b"))

if a > b and a > c:
    print("Największa liczba to: ", a)

elif b > a and b > c:
    print("Największa liczba to: ", b)

else:
    print("Największa liczba to: ", c)

#Zadanie12
print('ZADANIE 12')
liczby = [2, 4.5, 6, 7.8, 9]

for i in range(len(liczby)):
    liczby[i] = liczby[i] ** 2

print(liczby)

#Zadanie13
print('ZADANIE 13')
lista_parzystych = []
licznik = 0

while licznik < 10:
    liczba = int(input("Podaj liczbę: "))
    if liczba % 2 == 0:
        lista_parzystych.append(liczba)
    licznik += 1

print("Parzyste liczby to:", lista_parzystych)
