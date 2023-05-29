import numpy as np

print('ZADANIE 1')
#Za pomocą funkcji arange stwórz tablicę numpyskładającą się z 20 kolejnych wielokrotności liczby 4.

tablica = np.arange(4, 4*21, 4)
#pierwsza współrzędna- zaczynamy od 4
#druga współrzędna- ilość wyrazów: 4*20 (20 kolejnych wielokrotności)
#trzecia współrzędna- skok co 4
print(tablica)

print('\nZADANIE 2')
#Stwórz listę składającą się z wartości zmiennoprzecinkowych
#a następnie zapisz do innej zmiennej jej kopię przekonwertowaną na typ int32

a=np.array([1.241,3.425,2.252,8.213])
print(a.dtype)
a=a.astype('int')
print(a.dtype)

print('\nZADANIE 3')
#Napisz funkcję, która będzie:
# -Przyjmowała jeden parametr ‘n’ w postaci liczby całkowitej
# -Zwracała tablicę Numpy o wymiarach n*n kolejnych potęg liczby 2
def tablica_poteg(n):
    potegi = np.arange(n*n)
    #utworzenie listy o ilosci zmiennych n*n (np 16 dla n=4)

    potegi = potegi.reshape((n,n))
    #przekształcenie na tablice wielkości nxn

    potegi = np.power(2, potegi)
    #kazdy z elementow zamieniamy na 2^element
    #spróbuj zakomentować tą linijke i zobacz jak wygląda bez tego podnoszenia

    return potegi

n = 4
wynik = tablica_poteg(n)
print(wynik)

print('\nZADANIE 4')
#Napisz funkcję, która będzie przyjmowała 2 parametry:
#liczbę, która będzie podstawą operacji potęgowania oraz ilość kolejnych potęg do wygenerowania
#Korzystając z funkcji logspace generuj tablicę jednowymiarową kolejnych potęg podanej liczby
#np. generuj(2,4) -> [2,4,8,16]

def generuj(podstawa, ilosc):
    potegi = np.logspace(0, ilosc-1, num=ilosc, base=podstawa)
    #start- ustawiamy na 0
    #stop- ustawiamy na ilosc-1 (bo indeksujemy od 0) (na której wartości mamy sie zatrzymać)
    #num- ustawiamy na ilosc (ile wartosci chcemy wygenerowac)
    #base- ustawiamy na podstawa (do której wartosci chcemy potegowac liczby)
    return potegi

podstawa = 2
ilosc = 4
wynik = generuj(podstawa, ilosc)
print(wynik)

print('\nZADANIE 4')
#Napisz funkcję, która:
#Na wejściu przyjmuje jeden parametr określający długość wektora
#Na podstawie parametru generuj wektor, ale w kolejności odwróconej
#Generuj macierz diagonalną z w/w wektorem na przekątnej oddalonej o 2 w górę od głównej przekątnej macierzy
def generuj_macierz(dlugosc):
    wektor = np.arange(dlugosc, 0, -1)
    #utworzenie wektora z wartosciami malejącymi
    macierz = np.diag(wektor, 2)
    #utworzenie macierzy gdzie wartosci wektora na przekątnej
    #2- przesunięcie przekątnej o 2 wierze do góry

    return macierz

dlugosc = 5
wynik = generuj_macierz(dlugosc)
print(wynik)

print('\nZADANIE 6')
#Stwórz skrypt który na wyjściu wyświetli macierz numpy (tablica wielowymiarowa) w postaci wykreślanki,
#gdzie jedno słowo będzie wypisane w kolumnie, jedno w wierszu i jedno po ukosie.
#Jedno z tych słów powinno być wypisane od prawej do lewej.

#nw czy dobrze
imiona = ["leon", "klaudia", "michalina"]
dl_max = ""
krotsze = []
for i in imiona:
    if len(i) > len(dl_max):
        dl_max = i
for i in imiona:
    if len(i) < len(dl_max):
        krotsze.append(i)

mat = np.diag([a for a in dl_max])
mat = np.flip(mat)
for i in range(len(krotsze[0])):
    mat[0][i + 1] = krotsze[0][i]
for i in range(len(krotsze[1])):
    mat[i + 1][0] = krotsze[1][i]
print(mat)


print('\nZADANIE 7')
#Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:
#[[2 4 6]
#[4 2 4]
#[6 4 2]]

#Przy założeniach:
#funkcja przyjmuje parametr n, który określa wymiary macierzy jako n*n
#i umieszcza wielokrotność liczby 2 na kolejnych jej przekątnych rozchodzących się od głównej przekątnej.


def generate_matrix(n):
    matrix = np.zeros((n, n), dtype=int)
    #tworzenie macierzy nxn wypełnioną zerami

    for i in range(n):
        matrix[i, i] = 2

        for j in range(1, n - i):
            matrix[i, i + j] = 2 * (j + 1)
            matrix[i + j, i] = 2 * (j + 1)

    return matrix

n = 5
result = generate_matrix(n)
print(result)

print('\nZADANIE 8')


def divide_array(arr, kierunek):
    if kierunek == "pionowo":
        if arr.shape[0] % 2 != 0:
            print("Nie można podzielić tablicy pionowo - nieparzysta liczba wierszy.")
            return None

        half = arr.shape[0] // 2
        return arr[:half, :], arr[half:, :]

    elif kierunek == "poziomo":
        if arr.shape[1] % 2 != 0:
            print("Nie można podzielić tablicy poziomo - nieparzysta liczba kolumn.")
            return None

        half = arr.shape[1] // 2
        return arr[:, :half], arr[:, half:]

    else:
        print("Nieprawidłowy kierunek podziału. Dozwolone wartości: 'pionowo' lub 'poziomo'.")
        return None


# Przykładowe użycie
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
kierunek = "pionowo"

result = divide_array(arr, kierunek)
if result is not None:
    arr1, arr2 = result
    print("Pierwsza część:")
    print(arr1)
    print("Druga część:")
    print(arr2)

print('\nZADANIE 9')

start = 1  # Początkowa wartość ciągu
step = 2   # Różnica między kolejnymi wartościami

# Generowanie ciągu arytmetycznego
sequence = np.arange(start, start + 5*5*step, step)

# Reshape do macierzy 5x5
matrix = sequence.reshape((5, 5))

print(matrix)