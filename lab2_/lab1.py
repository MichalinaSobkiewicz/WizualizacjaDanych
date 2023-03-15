#ctrl + slash

#kompilator sam określa typ zmiennych
a='napis\ndrugi napis'
print(a)
b = 10
c = 4.5
print(b,c)

#liczby zespolone
d= 3+4j
print(d)

e=b+c
print(e)
f = b // c
# //-dzielenie całkowite
g = b % c
# %-dzielenie z resztą (modulo)
print(f)
print(g)

#potegowanie
i = c**2
print(i)
j= pow(5, 2)
print (j)


k = 5**1/2
m = pow(5,1/2)
print (k)
print (m)

print('b = b + 2')
b += 2
print(b)

#w liście mogą być różne typy
lista = ['a',2,4,7,1,[6,2,4], 5.5]
print(lista[0])
print(lista[1])



#Zadanie 1- dodaj elementy na pozycje

#dodawanie elementu pod konkretny numer indeksu
lista1 = [0,1,2,3,4,5,6]
lista1[0]=7

print(lista1[0])
#dodaj element na koniec listy
lista1.append(7)
print(lista1)

#dodaj kilka elementów na koniec listy
lista1.extend([8,9,10])

#usun element po indeksie
del lista1[2]
print(lista1)

#usun element po jego wartosci
lista1.remove(7)
print(lista1)

#sortowanie listy
lista1.sort()
print(lista1)

#odwracanie listy
lista1.reverse()
print(lista1)

#słownik
#przed : - klucz
# slownik = {'a': 1, 3: 1, 'a':5}
# print(slownik)
#
# print(slownik['a'])
# slownik['klucz']= 'wartosc'
# print(slownik)
#
# slownik.pop(3)
# print(slownik)
#
# print(slownik.keys())
# print(slownik.values())

#formatowanie
print('a= %(zm)d' % {'zm':12})
print('a= {}, b= {}'.format(12,14))

#if warunek:
#   instrukcja1
#   instrukcja2
#elif warunek2:
#   instrukcja1
#   instrukcja2
#else:
#   instrukcja1

# #Przykład
# a = input('podaj a: ')
# b = input('podaj b: ')
#
# print(a)
# print(b)
#
# print(type(a))
# print(type(b))
#
# a = int(a)
# b = int(b)
# print(type(a))
# print(type(b))
#
# if a > b:
#     print('a = '+ str(a))
# elif a<b:
#     print('b = ' + str(b))
# else:
#     print('a rowne b')

#zadanie 2- wczytaj 2 liczby i sprawdz czy są rowne
c = input('podaj c: ')
d = input('podaj d: ')

print(c)
print(d)

c= int(c)
d= int(d)

if c == d:
    print('liczby sa rowne')
else:
    print('liczby nie sa rowne')

#for element in sekwencja:
#   instrukcja1
#   instrukcja2
#else:
#   instrukcja1

#Przykład
#tu mozna podac 3 argumenty pierwsza liczba- argument stopu
#dwie liczby- początek i koniec
#trzy- ostatnia odpowiada co ile skaczemy
for x in range (1,6,1):
    print(x)
for x in lista:
     print(x)

#Zadanie- wyswietl wszystkie elementy z listy odnosząc sie w pętli for poprzez numery indeksów

lista3 = [2,4,6,8,10]

for x in range(len(lista3)):
    print(lista3[x])

#while warunek:
#   instrukcja1
#   instrukcja2
#else:
#   instrukcja1

#Przykład1
licznik = 0
while licznik != len(lista):
    print(lista[licznik])
    licznik += 1

#Przykład2- zagnieżdżenie pętli
liczby = [3, 45, 12, 2, 152, 12, 123]
licznik = 0

a= int(input('podaj a: '))
while licznik != len(liczby):
    if a - liczby[licznik] == 0:
        print('{} - {} = 0'.format(a,liczby[licznik]))
        break
    licznik +=1

#Zadanie3
liczbyy=[1,2,2,2,3,4]
licznikk = 0
while licznikk != len(liczbyy):
    if liczbyy[licznikk] == 2:
        liczbyy.pop(licznikk)
    else:
        licznikk += 1
for x in liczbyy:
    print(x)