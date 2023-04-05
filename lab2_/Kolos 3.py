#ZAD1
import math
expression = (math.exp(4) - math.log2(34))**(1/3)
rounded_result = round(expression, 2)
print(rounded_result)
#ZAD2
# Tworzenie listy z liczbami
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tworzenie nowej listy zawierającej co trzeci element z pierwszej listy za pomocą list comprehension
every_third_number = [numbers[i] for i in range(2, len(numbers), 3)]

# Wyświetlanie obu list
print("Lista z liczbami: ", numbers)
print("Co trzeci element z listy: ", every_third_number)
#ZAD3
def check_sum_and_count(numbers):
    # Obliczanie sumy pierwszego i ostatniego elementu listy
    sum_of_first_and_last = numbers[0] + numbers[-1]

    # Liczenie elementów z listy większych od sumy pierwszego i ostatniego elementu
    count = sum(1 for num in numbers if num > sum_of_first_and_last)

    # Zwracanie wyników
    return sum_of_first_and_last, count
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_result, count_result = check_sum_and_count(numbers)
print("Suma pierwszego i ostatniego elementu: ", sum_result)
print("Liczba elementów większych niż suma: ", count_result)
#ZAD4
# Otwieranie pliku z obsługą polskich znaków
with open('tekst.txt', 'r', encoding='utf-8') as file:
    # Wczytywanie tekstu z pliku
    text = file.read()

# Wycinanie fragmentu tekstu
start_index = 49
end_index = start_index + 25
fragment = text[start_index:end_index]

# Obliczanie ilości dużych liter w fragmencie tekstu
count_upper = sum(1 for letter in fragment if letter.isupper())
plik.close()
# Wyświetlanie wyników
print("Fragment tekstu: ", fragment)
print("Ilość dużych liter: ", count_upper)
#ZAD5
import math

try:
    # Wczytanie trzech liczb od użytkownika
    a = int(input("Podaj długość pierwszej przyprostokątnej: "))
    b = int(input("Podaj długość drugiej przyprostokątnej: "))
    c = int(input("Podaj długość przeciwprostokątnej: "))

    # Sprawdzenie, czy z podanych wartości można utworzyć trójkąt prostokątny
    if a > 0 and b > 0 and c > 0 and a*a + b*b == c*c:
        # Obliczenie pola trójkąta
        pole = 0.5 * a * b

        # Zapisanie wyniku do pliku
        with open("wynik.txt", "w") as file:
            file.write(f"Pole trójkąta wynosi: {pole}")

        print("Pomyślnie obliczono pole trójkąta i zapisano wynik do pliku.")

    else:
        print("Nie można utworzyć trójkąta prostokątnego o podanych bokach.")

except ValueError:
    print("Podane wartości nie są liczbami całkowitymi.")
