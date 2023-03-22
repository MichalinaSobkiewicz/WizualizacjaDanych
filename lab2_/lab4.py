import random
#ZADANIE 1
liczby1 = [random.randint(0,30) for i in range(30)]
liczby2 = [2 * liczba for liczba in liczby1]
with open("liczby.txt","w") as plik:
    for liczba in liczby2:
        plik.write(str(liczba) + "\n")

#ZADANIE 2
with open("liczby.txt","r") as plik:
 lines = plik.readlines()
for line in lines:
 print(line.strip())

#ZADANIE 3
with open("Zadanie 3.txt","w+") as plik:
    for i in range(10):
        plik.write("Oops i did it again,\n")

otworz=open("Zadanie 3.txt","r")
linia=otworz.readlines()
otworz.close()

print(linia)

#ZADANIE 4
class NaZakupy:
    nazwa_produktu=''
    ilosc=''
    jednostka_miary=''
    cena_jed='zl'
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        self.nazwa = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka = jednostka_miary
        self.cena = cena_jed

    def wyswietl_produkt(self):
        return nazwa+' '+ilosc+' '+jednostka+' '+cena+' zl'

    def ile_produktow(self):
        return ilosc+' '+jednostka
    def ile_kosztuje(self):
        wynik=int(ilosc) * int(cena)
        return str(wynik)


nazwa=input("Podaj nazwe produktu: ")
ilosc=input("Podaj ilosc: ")
jednostka=input("Podaj jednostkę miary:")
cena=input("Podaj cenę jednostkową: ")

nowy=NaZakupy(nazwa_produktu=str(nazwa),ilosc=int(ilosc),jednostka_miary=str(jednostka),cena_jed=int(cena))

print(nowy.wyswietl_produkt())

print("Ilosc Produktow: "+nowy.ile_produktow())

print("Koszt: "+nowy.ile_kosztuje()+" zl")

#ZADANIE 5
class CiagArytmetyczny:
    def __init__(self):
        self.elementy = []
    def wyswietl_dane(self):
        print("Elementy ciągu:", self.elementy)
    def pobierz_elementy(self):
        n = int(input("Liczba elementów ciągu: "))
        self.elementy = [float(input(f"Podaj {i}-ty element ciągu: ")) for i in range(1,n+1)]
    def pobierz_parametry(self):
        a1 = float(input("Pierwszy element ciągu: "))
        r = float(input("Różnica ciągu: "))
        n = int(input("Liczba elementów do wygenerowania: "))
        self.elementy = [a1 + i*r for i in range(n)]
    def policz_sume(self):
        suma = sum(self.elementy)
        print("Suma elementów ciągu: ", suma)
    def policz_elementy(self,a,r,n):
        self.elementy = [a + i * r for i in range(n)]
        print("Elementy ciągu: ", self.elementy)
ciag = CiagArytmetyczny()
ciag.pobierz_elementy()
ciag.wyswietl_dane()
ciag.pobierz_parametry()
ciag.wyswietl_dane()
ciag.policz_sume()
ciag.policz_elementy(1,3,5)