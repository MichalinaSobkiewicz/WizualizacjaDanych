import math
#ZADANIE 1 ZESTAW A
# print("Podaj liczby całkowite a, b i c")
# try:
#     a = int(input("Podaj pierwszą liczbę całkowitą: "))
#     b = int(input("Podaj drugą liczbę całkowitą: "))
#     c = int(input("Podaj trzecią liczbę całkowitą: "))
# except ValueError:
#     print("Wprowadzona wartość nie jest liczbą całkowitą.")
#     exit()
#
# result = a*a + a*b + b*b
#
# with open("zadanie1.txt", "w") as file:
#     file.write(str(result))
#     #przekonwertowanie intów na stringa, bo funkcja write przyjmuje tylko stringi

#ZADANIE 2 ZESTAW A
# lista1= [3,2,7,8]
# lista2= [7,2,8,1]
# def suma_list(lista1, lista2):
#     lista3 = []
#     for i in range(len(lista1)):
#     #dla iteratora z zakresu wielkości listy1
#         lista3.append(lista1[i] + lista2[i])
#         #append- dodawanie obiektów do listy
#     return lista3
# print(suma_list(lista1,lista2))

#ZADANIE 3 ZESTAW A
with open('plik.txt', mode='r', encoding='utf-8') as file:
    text = file.read()

fragment = text[99:134]
#wyodrębnienie fragmentu o długości 35 znaków zaczynając od 100 znaku
# print(text)


print(fragment)
duze_literki = []
for char in fragment:
    if char.isupper():
        duze_literki.append(char)

if duze_literki:
    print("Duże litery w fragmencie to:", ", ".join(duze_literki))
    print("Liczba dużych liter w fragmencie to:", len(duze_literki))
else:
    print("W fragmencie nie ma żadnych dużych liter.")

#ZADANIE 4 ZESTAW A
lista3 = [1,2,3,4,5,6,7,8,9,10]
a = 4
lista4 = []
for i in range(len(lista3)):
    if lista3[i] > a:
        lista4.append(lista3[i])
print(lista4)

#ZADANIE 5 ZESTAW A
wynik = math.pow(pow(math.e,3) + pow(math.cos(39),2),1/5) + math.pow(2/7,3) + math.pi
print(round(wynik,2))