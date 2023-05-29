import numpy as np
#Za pomocą funkcji arange stwórz tablicę numpy składającą się z 20 kolejnych wielokrotności liczby 4.
zad1 = np.arange(4, 81, 4)
print(zad1)
# Stwórz listę składającą się z wartości zmiennoprzecinkowych a następnie zapisz do innej zmiennej jej kopię
# przekonwertowaną na typ int32
zad2 = np.array([1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0])
zad2 = zad2.astype('int32')
print(zad2)
# Napisz funkcję, która będzie:•Przyjmowała jeden parametr ‘n’ w postaci liczby całkowitej•Zwracała tablicę Numpy
# o wymiarach n*n kolejnych potęg liczby 2
zad3 = np.array([2**a for a in range(9)]).reshape((3, 3))
print(zad3)
# Napisz funkcję, która będzie przyjmowała 2 parametry: liczbę, która będzie podstawą operacji potęgowania oraz ilość
# kolejnych potęg do wygenerowania. Korzystając z funkcji logspace generuj tablicę jednowymiarową kolejnych potęg podanej
# liczby, np. generuj(2,4) -> [2,4,8,16]
def zad4(base, n):
    return np.logspace(0, n-1, n, base=base)
ars = zad4(2, 4)
print(ars)

# Napisz funkcję, która:•Na wejściu przyjmuje jeden parametr określający długość wektora
# •Na podstawie parametru generuj wektor, ale w kolejności odwróconej
# •Generuj macierz diagonalną z w/w wektorem na przekątnej oddalonej o 2 w górę od głównej przekątnej macierzy
print('zadanie 5')
zad5 = np.arange(10)
zad5 = zad5[::-1]
print(zad5)
zad5 = np.diag(zad5, k=2)
print(zad5)

# Stwórz skrypt który na wyjściu wyświetli macierz numpy (tablica wielowymiarowa) w postaci wykreślanki, gdzie jedno słowo
# będzie wypisane w kolumnie, jedno w wierszu i jedno po ukosie. Jedno z tych słów powinno być wypisane od prawej do lewej.
print('zadanie 6')
zad6 = np.array([['k', 'o', 't'], ['p', 's', 'z'], ['r', 'y', 'x']])
print(np.fliplr(zad6).diagonal(offset=-1)[::-1])
print(zad6.diagonal())
print(np.flipud(zad6).diagonal(offset=2))

# print('zadanie 6')
# malina= np.array(list('malina'))
# malina= np.array(list('mrówka'))
# malina= np.array(list('armata'))
#
# wykreślanka= np.diag ()

# Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:[[2 4 6][4 2 4][6 4 2]]Przy założeniach:funkcja
# przyjmuje parametr n, który określa wymiary macierzy jako n*n i umieszcza wielokrotność liczby 2 na kolejnych jej
# przekątnych rozchodzących się od głównej przekątnej.
print('zadanie7')
def genmacierz(n):
    #zerowa macierz
    matrix = np.zeros((n, n), dtype=int)

    # Uzupełnianie macierzy o kolejne wielokrotności liczby 2 na przekątnych
    for i in range(n):
        matrix[i, i] = 2 * (i + 1)
        if i < n - 1:
            matrix[i, i + 1] = 2 * (i + 1)
            matrix[i + 1, i] = 2 * (i + 1)

    return matrix

print(genmacierz(2))
print('zadanie 8')
# Napisz funkcję, która:
# •jako parametr wejściowy będzie przyjmowała tablicę wielowymiarową numpy oraz parametr ‘kierunek’,
# •parametr kierunek określa czy tablica wejściowa będzie dzielona w pionie czy poziomie
# •funkcja dzieli tablicę wejściową na pół (napisz warunek, który wyświetli komunikat, że ilość wierszy lub kolumn,
# w zależności od kierunku podziału, nie pozwala na operację)
zad8 = np.arange(16).reshape((4, 4))
#do poprawy
print(zad8)
print(zad8[:2, :2])

# Wykorzystaj poznane na zajęciach funkcje biblioteki Numpy i stwórz macierz 5x5, która będzie zawierała kolejne
# wartości ciągu arytmetycznego.
zad9 = np.arange(1, 26).reshape((5, 5))
#do poprawy'
print(zad9)