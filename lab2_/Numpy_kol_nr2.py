import numpy as np
# Tablica w numpy to struktura o jednym  lub wiekszej ilosci rozmiarów
# Przechowuje dane tego samego typu

#inicjalizacja tablicy- dwa sposoby
a=np.arange(2)
print(a)

b=np.array([1.241,3.425])
print(b)

c= np.array(['gruszka', 'jabłko', 'śliwka'])
print(c)

#wypisywanie typu zmiennej tablicy
print(type(a))
print(type(b))

#sprawdzanie typu danych przechowywanych przez tablice
print(a.dtype)
print(b.dtype)

#zapisywanie kopii tablicy jako tablicy z innym typem
a=a.astype('float')
print(a.dtype)

#wypisywanie rozmiaru tablicy
print(b.shape)
print(c.shape)

#sprawdzanie ilosci wymiarów tablicy
print(a.ndim)
print(c.ndim)

#tworzenie tablicy wielowymiarowej
m = np.array([np.arange(2), np.arange(2)])
print(m.shape)
print(m.ndim)
#tablica wielowymiarowa nadal jest typem ndarray

#tworzenie macierzy przy pomocy biblioteki numpy
zera=np.zeros((5,5))
#tworzy macierz wypełnioną zerami o wymiarach 5x5
jedynki=np.ones((4,4))
#tworzy macierz wypełnioną jedynkami o wymiarach 4x4
print(zera)
print(jedynki)

print(zera.dtype)
print(jedynki.dtype)
#typem danych przechowywanych w tej macierzy jest float
#ale nie wiem dlaczego XD

#tworzenie pustej macierzy (która wcale pusta nie jest?)
pusta=np.empty((2,2))
print(pusta)
#jak se to wyprintujesz to są randomowe floaty

#do poszczególnych elementów odwołujemy sie tak jak w listach
#podajemy indeksy

poz_1=pusta[1,1]
poz_2=pusta[0,1]

print(poz_1)
print(poz_2)

#tworzenie macierzy z porządanymi danymi
macierz = np.array([[1,2],[3,4]])
#to co w nawiasie kwadratowym= wiersz
print(macierz)

#arange potrafi tworzyć ciągi liczb zmiennoprzecinkowych
liczby = np.arange(1,2,0.1)
#zaczynając od 1 tworzy ciąg liczb wiekszych o 0.1 od 1 aż do 2
print(liczby)

#podobnie działa funkcja linspace, które działanie jest równoważne tej samej funkcji w MATLAB-ie
liczby_lin = np.linspace(1,2,5)
print(liczby_lin)

#tworzenie dwóch macierzy
z = np.indices((5,3))
#5- ilość wierszy
#3- ilość kolumn
#wartości 0 (pierwsza kolumna)
#wartości 1 (druga kolumna)
#wartości 2 (trzecia kolumna)
print(z)

#Tworzenie macierzy diagonalnej
#Macierz diagonalna- taka, która ma zera wszedzie oprócz przekątnej (chociaz na przekątnej tez moze miec XD)
mat_diag = np.diag([a for a in range(5)])
print(mat_diag)
#tu automatycznie na przekątnej- wartosci od 0 do 4

mat_diag1=np.diag([a for a in range(6)])
print(mat_diag1)

print('----')
#możemypodać drugi parametr funkcji diag, który określa indeks przekątnej względem głównej przekątnej
# która zostanie wypełniona wartościami podanego wektora
mat_diag_k = np.diag([a for a in range(5)],0)
#0 - przsunięcie o 1 wiersz
#-1 - przsunięcie o 2 wiersz
#-2 - przesunięcie o 3 wiersze, itd
print(mat_diag_k)

#nupy może tworzyć tablice jednowymiarową z dowolnego typu iterowalnego
z = np.fromiter(range(51), dtype='int32')
print(z)
#wypisze liczby od 0 do 50 (range na 51 bo odlicza od 0)

#nie wiem po co to jest
znaki = b'ogolny'
z1 = np.frombuffer(znaki,dtype='S1')
print(z1)
#drukuje każdą z literek poprzedzoną b

z2 = np.frombuffer(znaki,dtype='S2')
print(z2)
#drukuje po 2 literki ze słowa poprzedzone b

#jak dasz słowo z nieparzystą ilością znaków, to nie wydrukuje tego drugiego printa

#inny sposob- to samo działanie
znaki = 'ogolna'
z3 = np.array(list(znaki))
z4 = np.array(list(znaki), dtype='S1')
z5 = np.array(list(b'ogolna'))
z6 = np.fromiter(znaki,dtype='S1')
print(z3)
print(z4)
print(z5)
print(z6)

#dodawnie, odejmowanie, mnozenie, dzielenie tablic
macierz1 = np.array([[1,2],[3,4]])
macierz2 = np.array([[4,3],[2,1]])

mat= macierz1 + macierz2
print(mat)

print(macierz1- macierz2)
print(macierz1 * macierz2)
print(macierz1/ macierz2)


print('\n INDEKSOWANIE I CIĘCIE TABLIC')

print('Funkcja SLICE')
a=np.arange(10)
print(a)
s=slice(2,7,1)
#pierwsza wartosc- od której ma sie zacząć cięcie
#druga wartosc- do kiedy ma trwac ciecie
#trzecia wartosc- co ile ma sie odbywać cięcie
print(a[s])

print('\n PRZY POMOCY CIĘCIA LIST')

print(a[2:7:2])
#od 2 do 7 co 2

print(a[1:])

print(a[2:5])
#od 2 do 5

print('\n CIĘCIE DLA TABLIC WIELOWYMIAROWYCH')
mat=np.arange(25)

#zmieniamy na wymiary 5x5:
mat=mat.reshape((5,5))
print(mat)

print('\n')
print(mat[1:]) #od 2 wiersza

print('\n')
print(mat[:,1]) #druga kolumna jako wektor- zwraca liniowo drugą kolumne

print('\n')
print(mat[:,-1]) #ostatnia kolumna- zwraca liniowo ostatnią kolumne
print(mat[:,4]) #to samo ale używam indeksu kolumny

print('\n')
print(mat[2:6, 1:3])
#pierwsze współrzędne - wiersze od 2 do 6 (bez 6)
#drugie współrzędne- wybiera kolumny o indeksach od 1 do 3 (bez 3)

print('\n')
mat=np.arange(25)
mat=mat.reshape((5,5))
print(mat[:, range(2,6,2)]) #3 i 5 kolumna
#pierwsza współrzędna- numer kolumny
#druga współrzędna- górna granica zakresu
#trzecie współrzędna- skok (co którą kolumne wybieramy)

print('\n CIĘCIE PRZY POMOCY WIERZCHOŁKÓW MACIERZY')
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)

#inicjalizacja y będącego tablicą zawierającą wierzchołki macierzy
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows,cols]
print(y)