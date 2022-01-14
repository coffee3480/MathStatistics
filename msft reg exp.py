import requests
import re
from bs4 import BeautifulSoup
from lxml import html
import brewer2mpl as b2mpl
import pandas as pand
import numpy as np
import matplotlib.pyplot as plt

#Задача: с сайта finance.yahoo.com получить данные о стоимости акций Microsoft
#Построить график значений стоимости по времени со скользящим средним.
#Вычислить среднее и медианное значения.



#  В данном случае получение данных происходит при помощи Web-scrapping


#<td class="Ta(end) Fw(600) Lh(14px)" data-test="PREV_CLOSE-value" data-reactid="42">329.49</td>


#Вытаскиваем значение с сайта
url='https://finance.yahoo.com/quote/MSFT?p=MSFT'
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }


r = requests.get(url).text


soup = BeautifulSoup(r, 'lxml')

quotes=soup.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')
#print(quotes)
html_text=str(quotes)
result=re.findall(r'>\d\d\d\.\d\d<',html_text)
#print(result)
a=result[0]
a=a.replace('>', '')
a=a.replace('<', '')
#print(a)



#Записываем новое значение в текстовый файл, если оно не равно последнему
try:
    f = open('msft.txt', 'r')
    txt1=[]
    for line in f:
        line=line.replace('\n','')
        line=float(line)
        txt1.append(line)
    b=float(a)
    if(txt1[len(txt1)-1]==b):
        print('Значение повторяется! Оно не будет занесено в файла, так как, скорее всего', end='')
        print(', вы запускаете программу слишком часто и пытаетесь повторно добавить предыдущее значение.')
        f.close()
    else:
        f.close()
        f = open('msft.txt', 'a')
        f.write(a+'\n')
        f.close()

except FileNotFoundError:
    f = open('msft.txt', 'a')
    f.write(a+'\n')
    f.close()







#Метод поиска среднего арифметического: принимает на вход массив, выдает значение среднего арифметического
def ArithmeticAverage(a=[]):
    av=(sum(a)) / (len(a))
    return av

#Метод вычисления медианного значения: принимает на вход массив, выдает значение медианы
def Midpoint(a=[]):
    asorted=sorted(a)#Сортируем поступивший на вход массив в порядке возрастания
    #Если в массиве нечётное число элементов, то принимает центральное значение в качестве медианы
    if((len(asorted) % 2) != 0):
        midpointIndex = (len(asorted)-1)/2
        midpoint = asorted[midpointIndex]
    else: #Если в массиве чётное число элементов, то в качестве медианы берём среднее арифметическое между двумя центральными значениями.
        ind1=(len(asorted)/2)-1
        ind2=len(asorted)/2
        midpoint = (asorted[int(ind1)]+a[int(ind2)])/2
    return midpoint


#Метод формирования running average:
def RunningAverage(a):
    RunAv=[]
    for i in range(len(a)-14, len(a)):
        RunAv.append(round(sum(a[(i-14):i])/14, 2))
    return RunAv

#Изъятие данных из файла
try:
    f = open('msft.txt', 'r')
    Msft=[]
    for line in f:
        line=line.replace('\n','')
        line=float(line)
        Msft.append(line)
except FileNotFoundError:
    print('File not found?!?!?!')
print(Msft)

y1=[]
for i in range(len(Msft)):
    y1.append(i)

RunAv = RunningAverage(Msft)




plt.plot(y1, Msft)
plt.show()

ind1=int(len(Msft)-14)
ind2=int(len(Msft))
Msft2=Msft[ind1:ind2]
y2=[]
for i in range(1,15):
    y2.append(i)

plt.plot(y2, Msft2)
plt.plot(y2, RunAv)
plt.show()












