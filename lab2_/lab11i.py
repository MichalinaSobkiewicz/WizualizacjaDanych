import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import PIL

# y=np.arange(2,9,2)
# plt.plot(y)
# plt.show()
#
# x=np.array([1,2,3,4])
# y=x**2
#
# plt.plot(x,y,'ro-')
# plt.show()
#
# plt.axis([0,6, 0,20])
# plt.plot(x,y, 'r-')
# plt.plot(x,y, 'o-')
# plt.axis([0,6, 0,20])
# plt.show()
#
# # a=np.arange(0,5,0.2)
# # plt.plot(a,a, 'r-', a, a**2, 'bs', a, a**3, 'g*')
# # plt.legend(labels=['liniowa', 'kwadratowa', 'szescienna'], loc='center left')
# # plt.show()
#
# a=np.arange(0,5,0.2)
# #plt.plot(a,a, 'r-', a, a**2, 'bs', a, a**3, 'g*')
# plt.plot(a,a,'r-', label='liniowa')
# plt.plot(a,a**2,'bs', label='kwadratowa')
# plt.plot(a,a**3, 'g*', label='szescienna')
# plt.legend(loc='center left')
#
#
# plt.xlabel('x')
# plt.ylabel('y')
#
# plt.title('wykres fajny')
# plt.savefig('lab11.png')
# plt.show()
#
# img= PIL.Image.open('lab11.png')
# img= img.convert('RGB')
# img.save('wykres.jpg')
#
# b=np.arange(0,10.1,0.1)
# plt.plot(b, np.sin(b), 'pink', label='sinus', linewidth=5)
# plt.show()

#
# data={'a': np.arange(50),
#       'c': np.random.randint(0,50,50),
#       'd': np.random.randn(50)}
# data['b']=data['a'] + 10 * np.random.randn(50)
# data['d']=np.abs(data['d']) * 100
#
# plt.scatter('a', 'b', c='c', s='d', data=data, cmap='plasma')
# plt.xlabel('a')
# plt.ylabel('b')
# plt.show()
#
#
# x1= np.arange(0,2,0.02)
# x2= np.arange(0,2,0.02)
# y1= np.sin(2*np.pi * x1)
# y2= np.cos(2*np.pi * x2)
#
# plt.subplot(4,2,1)
# plt.plot(x1, y1)
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Wykres sinusa')
#
# plt.subplot(4,2,8)
# plt.plot(x1,y2)
# plt.xlabel('x')
# plt.ylabel('cos(x')
# plt.title('Wykres cosinusa')
# plt.subplots_adjust(hspace=0.5)
# plt.show()

# x1=np.arange(0,2,0.02)
# x2=np.arange(0,2,0.02)
#
# y1=np.sin(2*np.pi*x1)
# y2=np.cos(2*np.pi*x2)
#
#
# fig, axs=plt.subplots(3,2)
# axs[0,0].plot(x1, y1,'r')
# axs[0,0].set_xlabel('x')
# axs[0,0].set_ylabel('y')
# axs[0,0].set_title('wykres sin(x)')
#
# axs[1,1].plot(x2,y2,'g')
# axs[1,1].set_xlabel('x')
# axs[1,1].set_ylabel('cos(x)')
# axs[1,1].set_title('wykres cos(x)')
#
# axs[2,0].plot(x1,y1,'r')
# axs[2,0].set_xlabel('x')
# axs[2,0].set_ylabel('sin(x)')
# axs[2,0].set_title('wykres sin(x)')
#
# fig.delaxes(axs[0,1])
# fig.delaxes(axs[1,0])
# fig.delaxes(axs[2,1])
# plt.show()

# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
#         'Kontynent': ['Europa','Azja','Ameryka Południowa'],
#         'Populacja': [11190846, 1303171035, 207847528]}
# df= pd.DataFrame(data)
# grupa= df.groupby('Kontynent').agg({'Populacja':[sum]})
# grupa.plot(kind='bar', xlabel='Kontynent', ylabel='Populacja',
#            legend=True,title='Populacja na kontynentach', rot=0)
# plt.show()

df=pd.read_csv('dane.csv', header=0, sep=';',decimal='.')
print(df)
grupa=df.groupby('Imie i nazwisko').\agg({'Wartosc zamowienia':['sum']})
grupa.plot(kind='pie', subplots=True, autopct= '%.2f%', fontsize=20, colors=['red','green'])
plt.show()