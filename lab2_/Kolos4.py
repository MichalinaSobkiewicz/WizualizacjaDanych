# import math
# #ZAD1
# expression = (math.log(20) + math.cos(45) + math.exp(1))**(1/3)
# rounded_result = round(expression, 2)
# print(rounded_result)
# #ZAD2
# # Utworzenie listy z liczbami
# liczby = [5, 10, 3, 8, 2, 7]
#
# # Utworzenie nowej listy bez minimalnej liczby
# nowa_lista = [x for x in liczby if x != min(liczby)]
#
# # Wyświetlenie obu list
# print("Pierwsza lista: ", liczby)
# print("Nowa lista: ", nowa_lista)
# #ZAD3
słownik = {1:2.5, 2.5:3.7, 3.5:4, 4.4:5.8}
def filtruj_zmiennoprzecinkowe(słownik):
    zmiennoprzecinkowe = []
    for klucz, wartość in słownik.items():
        if isinstance(klucz, float) and isinstance(wartość, float):
            zmiennoprzecinkowe.append((klucz, wartość))
    return zmiennoprzecinkowe

wynik=filtruj_zmiennoprzecinkowe(słownik)
print(wynik)

# #ZAD4
# with open('tekst.txt', 'r', encoding='utf-8') as plik:
#     znaki = plik.read()
#     fragment = znaki[17:58]
#     ilosc_c = znaki.count('c')
#     plik.close()
#     print("Wczytany fragment: ", fragment)
#     print("Ilość wystąpień litery 'c': ", ilosc_c)
#

#ZAD5
try:
    a1 = int(input("Podaj pierwszy wyraz ciągu: "))
    n = int(input("Podaj numer wyrazu do obliczenia: "))
    q = int(input("Podaj iloraz ciągu: "))
except ValueError:
    print("Podano niepoprawne wartości")
else:
    an = a1 * q ** (n - 1)
    with open("wynik.txt", "w") as f:
        f.write(str(an))
    plik.close()
