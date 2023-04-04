#1.LISTY
print('--------LISTY--------')
#a. Deklarowanie listy nazwa_listy=[]
Liczby_całkowite=[-3,-2,-1,0,1,2,3]
print(Liczby_całkowite)

#b.Dodawanie elementów na koniec listy nazwa_listy.append
Liczby_całkowite.append(4)
print(Liczby_całkowite)

#c.Dodawnie elementów w konkretne miejsce listy nazwa_listy.insert
Liczby_całkowite.insert(0, -4)
Liczby_całkowite.insert(9, 5)
print(Liczby_całkowite)

#d. Usuwanie ostatniego lub wybranego elementu z listy nazwa_listy.pop
Liczby_całkowite.pop()
print(Liczby_całkowite)
Liczby_całkowite.pop(0)
print(Liczby_całkowite)

#e. Usuwanie elementu po jego nazwie nazwa_listy.remove
#(jeżeli jest kilka takich samych wartości to usuwa pierwszy napotkany)
Liczby_całkowite.remove(0)
print(Liczby_całkowite)

#f. Usuwanie elementu po konkretnym indeksie  del nazwa_listy[numer indeksu]
del Liczby_całkowite[0]
print(Liczby_całkowite)

#g. Dodanie sekwencji elementów na koniec listy nazwa_listy.extend
Liczby_całkowite.extend((5,6,7,8))
print(Liczby_całkowite)

#h. Odwraacanie kolejności listy nazwa_listy.reverse()
Liczby_całkowite.reverse()
print(Liczby_całkowite)

#i. Sortowanie elementów w liście
Liczby_naturalne=[2,6,4,8,3,7,5,9]
Liczby_naturalne.sort()
print(Liczby_naturalne)

#j. Wyświetlanie długości listy
print(len(Liczby_całkowite))

print('\n')

#2. SŁOWNIK- przechowuje dane w postaci klucz:wartość, gdzie klucz to indeks
print('--------SŁOWNIK--------')
#a. Deklaracja słownika nazwa_slownika={klucz:wartosc, klucz:wartosc, klucz:wartosc,...}
slownik={1:'jabłko',2:'banan',3:'wiśnia', 4.5:10, 'ktos':'cos', 4.6:'wartosc'}
print(slownik)

#b.Dodanie nowego klucza wraz z wartością
slownik[4]='gruszka'
print(slownik)

#c.Wyswietlanie wartosci po kluczu print(nazwa_slownika[wartoscklucz])
print(slownik[4])
print(slownik[4.6])

#d. Usuwanie wartosci po kluczu nazwa_slownika.pop(wartoscklucza)
slownik.pop(4.6)
print(slownik)

#e. Wyswietlanie wszystkich kluczy ze slownika
print(slownik.keys())

#e. Wyswietlanie wszystkich warosci ze slownika
print(slownik.values())

#f.Usunięcie całej pary klucz:wartość
del slownik[1]
print(slownik)

print('\n')

#3. WPROWADZANIE DANYCH
print('--------WPROWADZANIE DANYCH--------')

#a.Komenda wejścia- input
# napis = input('Wpisz dowolny napis: ')
# print(napis)
#
# #b. Wyświetlanie typu wprowadzonej wartosci
# print(type(napis))
#
# #Tu dane domyślnie są w typie string
# #Jeżeli chcemy dodać liczbe musimy dokonac jej rzutowania na odpowiedni typ
#
# liczba=input("Wpisz jakąś liczbe: ")
# print(liczba)
# print(type(liczba))
# #tu konsola zwraca informacje że to string
# liczba=int(liczba)
# print(type(liczba))

print('\n')

#4. INSTRUKCJE WARUNKOWE
print('---------INSTRUKCJE WARUNKOWE--------')

#a. Operatory porównawcze
# == -operator równości, sprawdza czy x jest równy y
# != -sprawdza czy jeden obiekt różni się od drugiego, sprawdza czy x  różni się od y
# >-większy niż, sprawdza czy x jest większy od y
# < -mniejszy niż, sprawdza czy x jest mniejszy od y
# >= -większy niż lub równy, sprawdza czy x jest większy lub równy y
# <= -mniejszy niż lub równy, sprawdza czy x jest mniejszy lub równy y

#b. Składnia

# if warunek_1:
#     Instrukcje_1
# elif warunek_2:
#     Instrukcje_2:
# ...
# elif warunek_n:
#     Instrukcje_n
# else:
#     Inne_instrukcje

#c. Przykładowy program- pobranie dwóch liczb całkowitych
#sprawdzanie która jest większa
#zamiana na typ string przy wyświetlaniu

# a = input("podaj pierwszą liczbę: ")
# b = input("podaj pierwszą liczbę: ")
#
# a = int(a)
# b = int(b)
# #Rzutowanie zmiennych na konkretny typ
# if a > b:
#     print("liczba " + str(a) + " jest większa")
# elif a < b:
#     print("liczba " + str(b) + " jest większa")
#
# else:
#     print("wprowadzone liczby są równe")
#
# #d. Operatory logiczne AND (&) i OR (|)
# #Pobieramy 4 liczby całkowite i sprawdzamy czy a jest wieksze od b i czy c jest wieksze od d
# a = input("podaj pierwszą liczbę: ")
# b = input("podaj drugą liczbę: ")
# c = input("podaj trzecią liczbę: ")
# d = input("podaj czwartą liczbę: ")
#
# a = int(a)
# b = int(b)
# c = int(c)
# d = int(d)
# if (a > b) & (c > d):
#     print("liczba a jest większa od liczby b i liczba c jest większa od liczby d")
#
# else:
#     print("liczba a jest mniejsza od liczby b lub liczba c jest mniejsza od liczby d")

print('\n')

#5.INSTRUKCJA ITERACYJNA FOR
print('--------INSTRUKCJA ITERACYJNA FOR--------')

#Przykład 1- wyświetlanie wartości z zakresu
for x in range(1,6,1):
    print(x)
    #gdzie poszczególne liczby in range(a,b,c) to
    #a-skąd zaczynamy odliczanie
    #b-wartość na której kończymy
    #c-wielkość powiększania argumentów- liczba całkowita!
    #pamietaj że odliczanie poszczególnych argumenów zaczyna sie od 0
for z in range(0,10,2):
    print(z)

print('\n')

#Przykład 2- wyświetlanie wszystkich elementów z listy
lista1=['gruszka',2,6,7.5]
for x in lista1:
    print(x)

print('\n')

#Przykład 3- wyświetlanie elementów z listy. Po skończeniu wyświetl komunikat "koniec listy"
for x in lista1:
    print(x)
else:
    print('Koniec listy')

print('\n')

#5.INSTRUKCJA ITERACYJNA WHILE
print('--------INSTRUKCJA ITERACYJNA WHILE--------')
#Przykład1- wyświetlanie liczb z zakresu 0-10, po zakonczeniu pętli wyswietl kompunikat ile liczb zostało wyswietlonych

z=0
while z != 10:
    print(z)
    z += 1
else:
    print('wyświetlonych zostało '+str(z)+ ' liczb')

#INSTRUKCJA BREAK I CONTINUE
#a. Instrukcja berak
#przerywa działanie pętli w której się znajduje
#(ale nie wszystkich pętli jeśli pętle zagnieżdżamy)

#Przykład 1- Sprwadzamy czy różnica między podaną liczbą a liczbą z listy równa będzie 0
lista2 = [4, 6, 2, 3, 5, 9, 1]
print("Podaj liczbę a sprawdzę czy róźnica między wpisaną liczbą a liczbą z listy równa się 0")
liczba = input("wpisz swoją liczbe: ")
licznik = 0
while licznik < len(lista2):
    if int(liczba) - lista2[licznik] == 0:
        print(liczba + " -" + str(lista2[licznik]) + " = 0")
        print('{} -{} = 0'.format(liczba, lista2[licznik]))
        break
    else:
        licznik+=1
else:
    print("Żadna z liczb, które są w liści nie dała odpowiedniego wyniku")

#b. Instrukcja continue
#kończy przebieg aktualnej iteracji pętli
# i przechodzi do następnego przebiegu.

print('\n')
#INSTRUKCJE ITERACYJNE ZAGNIEŻDŻENIA
print('--------INSTRUKCJE ITERACYJNE ZAGNIEŻDŻENIA--------')
#Zagnieżdżenie- umieszczenie instrukcji warunkowej bądź pętli jedna w drugiej
#Przykład 1- Tworzymy dwie listy i robimy sumę poszczególnych elementów
lista = [4, 6, 2, 3, 5, 9, 1]
lista2 = [7, 3, 4, 6]
suma = []
for a in lista:
    for b in lista2:
        wynik = a + b
        suma.append(wynik)
print(suma)

liczby = [1, 2, 2, 2, 2, 3]
licznik = 0
while licznik != len(liczby):
    if liczby[licznik] == 2:
        liczby.pop(licznik)
    else:
        licznik += 1