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

# df = pd.read_csv('wine.data')
#
# print(df)
#
# randomowe = [np.random.randint(0, len(df)-1) for _ in range(100)]
# df2 = df.iloc[randomowe]
#
# grupy = df2.groupby('Class').size()
#
# plt.pie(grupy, labels=grupy.index, autopct='%1.1f%%')
# plt.legend()
# plt.title("Udział klas")
# plt.show()

print('ZADANIE 4')
# df1 = pd.read_csv('wine.data')
# plt.show()
#
# plot = sns.barplot(data=df1, x='Class', y='Alcohol',
#                    errorbar=None, hue='Class', estimator=np.mean,
#                    dodge=False, palette=['red', 'green', 'yellow'])
# plot.legend(title='Klasa')
# plot.set(title='Średnie Wartośći Alkoholu')
#
# plt.show()