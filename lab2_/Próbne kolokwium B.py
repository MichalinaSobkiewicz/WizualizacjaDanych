import math

#Zadanie 1
print('-----ZADANIE 1-----')
# Dany jest plik tekst.txt. Dokonaj wczytania pliku wraz z obsługą polskich znaków oraz zapisz
# do zmiennej znaki, 40 znaków z tekstu zaczynając od 71 znaku tekstu. Następnie wyświetl tylko
# ilość litery „A” z wczytanego fragmentu, jeśli ich nie będzie wyświetl odpowiedni komunikat.

#Utwórz plik txt
#Wczytywanie pliku z obsługą polskich znaków
with open('kolos_b.txt', mode='r', encoding='utf-8') as file:
    tekst = file.read()

#Wyświetlanie znaków od 71 do 111
znaki= tekst[71:111]


#Zliczanie literek A
iloscA= znaki.count('A')


if iloscA>0:
    print('W tym tekscie literek A jest: ', iloscA)
else:
    print('W tym tekscie nie ma literek A')

print('\n')
#Zadanie 2
print('-----ZADANIE 2-----')
# Napisz skrypt, w którym utworzysz listę z liczbami, a następnie za pomocą python
# comprehension utwórz nową listę, która będzie zawierać tylko liczby zmiennoprzecinkowe, na
# koniec wyświetl obie listy.

lista= [5,2,2.3,1.8,2,5,1,8.2,9,11,14]
zmiennoprzecinkowe=[x for x in lista if isinstance(x, float)]
#dodaj x dla x z listy jeśli jest on w typie float


print("Lista wszystkich liczb: ", lista)
print("Lista liczb zmiennoprzecinkowych: ", zmiennoprzecinkowe)

#Tu utworzona nowa lista z elementów wiekszych od a
# a= 6
# wiekszeoda=[x for x in lista if x>a]
# print(wiekszeoda)

print('\n')

#Zadanie 3
#Napisz funkcje, która jako argument przyjmuje listę z liczbami dowolnego typu. Zadaniem
#funkcji jest zrobienie sumy pierwszego elementu ze wszystkimi elementami z listy, dodanie ich na
#koniec do listy wejściowej i zwrócenie jej.

print('-----ZADANIE 3-----')
lista=[2,1,3,5,7,9]
def dodaj_pierwszy(lista):
    for i in range(1, len(lista)):
        lista[i] += lista[0]
    return lista

wynik = dodaj_pierwszy(lista)
print(wynik)

print('\n')
#Zadanie 4
print('-----ZADANIE 4-----')
wynik = math.sin(56)**2 + (math.sqrt(4)*(4**2/25) + math.log(85))
wynik = round(wynik, 2)

wynik2= math.pow(pow(math.e, 3) + pow(math.cos(39), 2), 1 / 5) + math.pow(2 / 7, 3) + math.pi
wynik2 = round(wynik2, 2)

print(wynik)
print (wynik2)

print('\n')
#Zadanie 5
print('-----ZADANIE 5-----')
try:
    n = int(input("Podaj liczbę całkowitą n: "))
    suma = int(sum(range(1, n+1)))
    with open("zadanie5.txt", "w") as plik:
        plik.write(f"Suma liczb od 1 do {n}  wynosi: {suma}")
        plik.close()
    print(f"Suma liczb od 1 do {n} wynosi: {suma}")
except ValueError :
    print(f"Wystąpił błąd:")