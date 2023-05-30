import numpy as np

print('ZADANIE 1')
#utwórz dwie macierze1x3 różnych wartości a następnie wykonaj operację mnożenia.
matrix1 = np.array([1, 2, 3])
matrix2 = np.array([4, 5, 6])

result = np.dot(matrix1, matrix2)
print(result)

print('\nZADANIE 2')
matrix_3x3 = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])

matrix_4x4 = np.array([[10, 11, 12, 13],
                       [14, 15, 16, 17],
                       [18, 19, 20, 21],
                       [22, 23, 24, 25]])
#axis=0 - kolumna
#axis=1 - wiersz
min_columns_3x3 = np.min(matrix_3x3, axis=0)
min_rows_3x3 = np.min(matrix_3x3, axis=1)
min_columns_4x4 = np.min(matrix_4x4, axis=0)
min_rows_4x4 = np.min(matrix_4x4, axis=1)

print("Najniższe wartości dla każdej kolumny w macierzy 3x3:")
print(min_columns_3x3)
print("Najniższe wartości dla każdego rzędu w macierzy 3x3:")
print(min_rows_3x3)
print("Najniższe wartości dla każdej kolumny w macierzy 4x4:")
print(min_columns_4x4)
print("Najniższe wartości dla każdego rzędu w macierzy 4x4:")
print(min_rows_4x4)

print('\nZADANIE 3')
#iloczyn macierzy o innych rozmiarach

print('\nZADANIE 4')
#Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite, a druga liczby rzeczywiste.
# Następnie wykonaj na nich operację mnożenia.
x = np.array([8, 2, 6], dtype=int)
y = np.array([4.2, 5.4, 2.8], dtype=float)

z = x * y
print(z)

print('\nZADANIE 5')
#Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej
#z jej wartości i zapisz do zmiennej “a”.
jo = np.array([[2, 8, 5], [6, 3, 9]])

t = np.sin(jo)


print(t)


print('\nZADANIE 6')
#Utwórz nową macierz 2x3 różnych wartości a następnie
#wylicz cosinus dla każdej z jej wartości i zapisz do zmiennej “b”.

macierz= np.array([[2, 7, 4], [1, 8, 10]])
wynik = np.cos(macierz)
print(wynik)

print('\nZADANIE 7')
#Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b.
a = np.array([[1, 2, 3], [4, 5, 6]])
a = np.sin(a)

b = np.array([[0.5, 1.5, 2.5], [3.5, 4.5, 5.5]])
b = np.cos(b)
c= a+b
print(c)

print('\nZADANIE 8')
#Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.
macierzfajna = np.array([[7, 2, 5], [2, 1, 8], [2, 8, 3]])
for row in macierzfajna:
    print(row)

print('\nZADANIE 9')
#Wygeneruj macierz 3x3 i wyświetl w pętli każdy element korzystając z
# opcji “spłaszczenia” macierzy. (użyj funkcji flat())
a = np.array([[2, 6, 8], [0, 5, 8], [2, 1, 5]])
for element in a.flat:
    print(element)

print('\nZADANIE 10')
#Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego?
macierzx= np.arange(81).reshape(9, 9)
# zmiana kształtu na macierz 3x27
b = macierzx.reshape(3, 27)
# zmiana kształtu na macierz 27x3
c = macierzx.reshape(27, 3)
# zmiana kształtu na macierz 81x1 (wektor)
d = macierzx.reshape(81, 1)
#
e = macierzx.reshape(1, 81)

print('\nZADANIE 11')
#Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4. Wygeneruj w ten sposób
# jeszcze kombinacje 4x3 i 2x6. Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?
wektor = np.array([6, 2, 5, 7, 1, 7, 9, 8, 4, 10, 2, 14])

# przekształcenie wektora na macierz 3x4 i odwrotnie (4x3)
macierz1 = wektor.reshape((3, 4))
print(macierz1)

macierz2 = wektor.reshape((4, 3))
print(macierz2)

#przekształcanie na macierz 2x6
macierz3 = wektor.reshape((2, 6))

#spłaszczanie macierzy
macierz1p=macierz1.flatten()
macierz2p=macierz2.flatten()
macierz3p=macierz3.flatten()

print('---')
print(macierz1p)
print('---')
print(macierz2p)
print('---')
print(macierz3p)


