import numpy as np

print('zadanie 1')
a= np.array([10,12,14])
b= np.array([16,18,20])
c = a*b
print(c)

print('zadanie 2')
c= np.array([[10,11,12],[13,14,15],[16,17,18]])
d= np.array([[18,21,76,13],[12,56,23,65], [25,1,64,2],[14,98,25,25]])
najmniejsza_wier_c= np.min(c, axis=1)
najmniejsza_kol_c= np.min(c, axis=0)

najmniejsza_wier_d= np.min(d, axis=1)
najmniejsza_kol_d= np.min(d, axis=0)
print('-----')
print(najmniejsza_wier_c)

print('-----')
print(najmniejsza_kol_c)

print('-----')
print(najmniejsza_wier_d)

print('-----')
print(najmniejsza_kol_d)

print('zadanie 3')
x = np.dot(a, b)
print(x)

print('zadanie 4')
hihi = np.array([8, 2, 6], dtype=int)
haha = np.array([4.2, 5.4, 2.8], dtype=float)

hoho = hihi * haha

print(c)

print('zadanie 5')
jo = np.array([[2, 8, 5], [6, 3, 9]])

t = np.sin(jo)

print(t)

print('zadanie 6')
macierz= np.array([[2, 7, 4], [1, 8, 10]])
wynik = np.cos(macierz)
print(wynik)

print('zadanie 7')
a = np.array([[1, 2, 3], [4, 5, 6]])
a = np.sin(a)

b = np.array([[0.5, 1.5, 2.5], [3.5, 4.5, 5.5]])
b = np.cos(b)

c= a+b
print(c)

print('zadanie 8')
macierzfajna = np.array([[7, 2, 5], [2, 1, 8], [2, 8, 3]])
for row in macierzfajna:
    print(row)

print('zadanie 9')
a = np.array([[2, 6, 8], [0, 5, 8], [2, 1, 5]])

for element in a.flat:
    print(element)

print('zadanie 10')
macierzx= np.arange(81).reshape(9, 9)
# zmiana kształtu na macierz 3x27
b = macierzx.reshape(3, 27)
# zmiana kształtu na macierz 27x3
c = macierzx.reshape(27, 3)
# zmiana kształtu na macierz 81x1 (wektor)
d = macierzx.reshape(81, 1)

print('zadanie 11')
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