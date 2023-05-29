import numpy as np
import pandas as pd

print('-----SERIES (serie danych)-----')
#serie danych- jednowymiarowa tablica z etykietami mogąca przechowywać dowolny typ danych
s = pd.Series([1,3,5,np.nan, 6,8])
#np. nan- dana pusta
print(s)

s=pd.Series([10,12,8,12], index=['a','b','c','d'])
#definiowanie indeksów- domyślnie definiuje od 0
print(s)

print('-----DATA FRAME (ramka danych)-----')
#ramka danych-dwuwymiarowa struktura z etykietami
#mogąca przechowywać kolumny z różnymi typami danych

data= {'Kraj': ['Polska','Niemcy','Austria', 'Czechy'],
       'Stolica': ['Warszawa', 'Berlin', 'Wiedeń', 'Praga'],
       'Populacja':[381245032, 827194712, 471882441,1536454123]}

df= pd.DataFrame((data), index=['panstwo1', 'panstwo2', 'panstwo3','panstwo4'])
print(df)

print('-----')

#ramka danych przechowuje typ każdej kolumny, można to sprawdzić:
print(df.dtypes)

print('-----TWORZENIE SERII DANYCH-----')
daty = pd.date_range('20230426', periods=5)
print(daty)
#wydrukuje 5 dat od 26.04.2023 w góre

df= pd.DataFrame(np.random.randn(5,4), index=daty,
                 columns=list('ABCD'))
#obiekt data frame o wymiarach 5 na 4 gdzie indeksami są wcześniej utworzone daty
#kolumny są zapełniony losowami liczbami pobranymi z rozkładu normalnego
#o średniej 0 i odchyleniu standardowym 1 (to ten fragment random.randn())
#columns= list('nazwykolumn') odpowiada za nazwanie każdej kolumny
print(df)

print('-----TWORZENIE DATA FRAMEÓW Z ZEWNĘTRZNYCH ŹRÓDEŁ DANYCH CSV I XLSX-----')

#biblioteka Pandas umożliwia również tworzenie DataFrame'ów z zewnętrznych źródeł danych
#CSV, odczyt i zapis

print('format CSV')
# df = pd.read_csv('dane.csv', header=0, sep=";",decimal=',')print(df)
# df.to_csv('plik.csv', index=False)

print('format XLSX- Excel')
#wymagana jestbiblioteka openpyxl
plikexcel= pd.ExcelFile('danefajne.xlsx')
df= pd.read_excel(plikexcel, header=0)
print(df)

df.to_excel('dane2.xlsx', sheet_name='arkusz pierwszy')
#zapis do innego pliku

print('------')
print('------')
print('------')

print('-----POBIERANIE DANYCH ZE STRUKTUR-----')

seria=pd.Series([3,6,9,12], index=['a','b', 'c', 'd'])
print(seria)

data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11190846, 1303171035, 207847528]}

df = pd.DataFrame(data)
print(df)

print('\n')

#drukowanie pojedynczego elementu serii- odnosimy się do nazwy indeksu
print(seria['a']) #drukuje 3
print(seria['b']) #drukuje 6
print(seria['c']) #drukuje 9
print(seria['d']) #drukuje 12

print('\n')

#drukowanie pojedynczego elementu serii- inny sposób (też odnosimy się do nazwy indeksu)
print(seria.c)
print(seria.d)

print(df[0:0])
#wydrukuje
print(df[1:3])

