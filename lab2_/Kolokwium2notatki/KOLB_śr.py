import numpy as np
import matplotlib.pyplot as plt

print('ZADANIE 1')
#Za pomocą biblioteki matplotllib utwórz wykres liniowy funkcji f(x) = cos(x)/x^2, dla x w przedziale [3,7],
#wartości x zmieniają się co 0.25. Dodaj odpowiednie etykiety
#do osi wykresu, tytuł linii, legendę, oraz tytuł wykresu.
#Dodatkowo wyświetl oba wektory przekazywane na wykres.
#Ustaw zakres oś x na granice przedziału

# Utwórz wektor x z wartościami od 3 do 7 z krokiem 0.25
x = np.arange(2.75, 7.25, 0.25)

# Oblicz wartości funkcji f(x)
fodx = np.cos(x) / x**2

# Utwórz wykres liniowy
plt.plot(x, fodx, 'b-', label='f(x)=cos(x)/x^2')

# Dodaj etykiety osi
plt.xlabel('x')
plt.ylabel('y')

# Ustaw zakres osi x
plt.xlim(3, 7)

# Dodaj tytuł wykresu
plt.title('Wykres funkcji')

# Dodaj legendę
plt.legend()

# Wyświetl oba wektory przekazywane na wykres
plt.show()

print('\n ZADANIE 2- pierwszy wykres')
#Odwzorowywanie funkcji

#definiowanie funkcji kwadratowej
def f(x):
    return 5 * x**2 + 3 * x + 2

#określenie zakresów
plt.axis([-4, 4, 0, 100])

# Tworzenie wektora x
x = np.linspace(-10, 10, 100)
# Zakres od -10 do 10, 100 równoodległych punktów

# Obliczanie wartości funkcji f(x) dla każdego punktu x
y = f(x)

# Tworzenie wykresu
plt.plot(x, y)

# Dodawanie etykiet osi
plt.xlabel('x')
plt.ylabel('wykres funkcji')

plt.plot(x, y, label='f(x) = (5 * x**2) * 3 * x + 2')  # Dodanie etykiety do krzywej

# Dodawanie tytułu wykresu
plt.title('Pierwszy Wykres')

plt.legend(loc='upper right')

# Wyświetlanie wykresu
plt.show()

print('\n ZADANIE 2- drugi wykres')
#Odwzorowywanie funkcji
x = np.linspace(-10, 10, 100)
y = (-2 * x ** 3) + 5
plt.axis([-4, 4, -100, 100])
plt.plot(x, y, 'g-', linewidth=5, label='-2x^3 + 5')

plt.xlabel('x')
plt.ylabel('wykres funkcji')
plt.title('Drugi wykres')

plt.legend(loc='upper center')

plt.show()

print('\n ZADANIE 3')
# używając biblioteki pandas wczytaj zawartości pliku 'wine.data' do ramki danych i wykonaj następujące kroki:
# -Utwórz nową ramkę danych, gdzie znajdzie się sto losowych wierszy, wiersze mogą się powtarzać.
# -na nowej ramce danych dokonaj grupowania danych  po kolumnie class.
# -na wykresie kołowym przedstaw  procentowy udział każdej z klasy

# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Wczytanie pliku 'wine.data' do ramki danych
# df = pd.read_csv('wine.data', header=None)
#
# # Utworzenie nowej ramki danych z 100 losowymi wierszami
# random_df = df.sample(n=100, replace=True)
#
# # Grupowanie danych po kolumnie 'class'
# grouped = random_df.groupby(0).size()
#
# # Tworzenie wykresu kołowego z procentowym udziałem każdej klasy
# plt.pie(grouped, labels=grouped.index, autopct='%1.1f%%')
#
# # Dodanie tytułu wykresu
# plt.title('Procentowy udział klas')
#
# # Wyświetlenie wykresu
# plt.show()

print('ZADANIE 4')
import seaborn as sns


# # Wczytanie pliku 'wine.data' do ramki danych
# df = pd.read_csv('wine.data', header=None)
#
# # Nadanie nazw kolumn
# df.columns = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity', 'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'OD280_OD315', 'proline']
#
# # Stworzenie wykresu kolumnowego
# sns.barplot(data = df , x='class', y='alcohol',  errorbar=None , hue='Class' , palette = ['red','green','yellow'])
#
# # Dodanie etykiet osi i tytułu wykresu
# plt.xlabel('Class')
# plt.ylabel('Średnia wartość alkoholu')
# plt.title('Średnia wartość alkoholu dla każdej klasy')
#
# # Wyświetlenie wykresu
# plt.show()
