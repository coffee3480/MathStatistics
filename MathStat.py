#Метод вычисления среднего арифметического
def arithmetic_average(a=[]):
    av=sum(a)/len(a)
    return av

#Метод вычисления факториала числа
def factorial(a):
    if((a%1 != 0)| (a<0)):
        warning="Cannot calculate factorial because the given number isn't natural!"
        return warning
    if(a==0):
        return 1
    fact=1
    while(a>1):
        fact=fact*a
        a=a-1
    return fact

#Метод вычисления вероятности. Пример: Игральный кубик бросают 1 раз. Вероятность того, что выпадет 1 или 2:
#m - число успешных исходов, n - общее число исходов.
#probability(2,6)
# = 1/3
def probability(m,n):
    if((m<0)|(n<0)):
        warning="Values shouldn't be negative."
        return warning
    if(n==0):
        warning='Cannot devide by zero.'
        return warning
    prob=m/n
    return prob


#Формулы комбинаторики:
#Combinatorics:
#Перестановки без повторений
def permutations(n):
    return factorial(n)
def P(n):
    return factorial(n)

#Размещения:
def subset_permutation(n,k):
    return Factorial(n)/Factorial(n-k)
def S(n,k):
    return Factorial(n)/Factorial(n-k)

#Перестановки с повторениями
def permutations_with_repetition(n,m):
    return n**m
def A(n,m):
    return n**m

#Сочетания без повторений:
def combinations(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))
def C(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

#Сочетания с повторениями:
def combinations_with_repetition(n,m):
    return factorial(n+m-1) / (factorial(m)*factorial(n-1))
def F(n,m):
    return factorial(n+m-1) / (factorial(m)*factorial(n-1))

#Разбиения:
def partition(n, m=[]):
    M=1
    for i in range(len(m)):
        M=M*factorial(m[i])
    return factorial(n) / M

#Бином Ньютона:
def binomial_theorem(a,b,n):
    X=0
    for i in range(n+1):
        X = X + C(n,i)*(a**i)*(b**(n-i))
    return X



#Формула испытаний Бернулли
#Пример: вероятность рождения мальчика - 0.55, рождается 10 детей, найти вероятность того, что родится 6 мальчиков.
#n - общее число испытаний = 10
#k - число успешных испытаний = 6
#p - вероятность успеха = 0.55
#bernoulli(10,6,0.55)
# = 0.24
def bernoulli(n,k,p):
    return C(n,k) * (p**k) * ((1-p)**(n-k))

#Наиболее вероятное число успешных испытаний.
#n - число испытаний
#p - вероятность успеха
#Пример: стрелок стреляет в мишень 10 раз, точность стрелка = 0.85. Какое ожидаемое количество попаданий?
#successful_tries(10,0.85)
# = 8 или 9
def successful_tries(n,p):
    s1=int((n*p-(1-p))//1)
    s2=int((n*p+p)//1)
    values=[]
    while(s1<=s2):
        values.append(s1)
        s1=s1+1
    return values

    

#Формула Пуассона
#Used when n is great and p is small... Used for rare events, accurate for np<=10
def poisson(n,k,p):
    lambd=n*p
    if(lambd<=10):
        return ((lambd**k) * (2.71828**(-lambd))) / Factorial(k)
    else:
        warning="This isn't an appropriate example for using Poisson's formule"
        return warning

#Формула Гаусса
def gauss_function(n,k,p):
    x = (k-np) / ((n*p*q)**(0.5))
    return x

#Формула Муавра-Лапласа
def moivre_laplace(n,k,p):
    return (1/((n*p*(1-p)**(0.5)))) * (gauss_function(n,k,p))



#Формула полной вероятности
#Пример: мимо заправки проезжают ТС. Среди них 70% автомобилей, 20% грузовиков и 10% автобусов.
#30% автомобилей, 40% грузовиков и 50% автобусов заезжают на заправку, чтобы заправиться.
#Едет ТС. Найти вероятность того, что оно заедет за заправку.
#full_probability([0.7, 0.2, 0.1], [0.3, 0.4, 0.5])
# = 0.34
def full_probability(a,b):
    if(len(a)!=len(b)):
        warning="Warning! Length(a) must be equal to Length(b)."
        return warning
    for i in range(len(a)):
        if((isinstance(a[i], float)!=True) | (isinstance(b[i], float)!=True)):
            warning="Warning! List elements should be float."
            return warning
    c=0
    for i in range(len(a)):
        c = c + (a[i]*b[i])
    return c

#Формула Байеса
#Аналогично примеру в формуле полной вероятности, но вопрос ставится с условием наступления первой гипотезы:
#Какова вероятность, что следующее проезжающее ТС будет грузовиком и заедет на заправку?
#index - индекс элементов массивов, отвечающих за выполнение первой гипотезы. В данном случае первое событие - ТС - грузовик.
#Следовательно, нас интересуют вторые элементы из двух массивов. То есть элементы с индексом 1.
#bayes([0.7, 0.2, 0.1], [0.3, 0.4, 0.5], 1)
# = 0.24
def bayes(a,b,index):
    return (a[index]*b[index]) / full_probability(a,b)

#Математическое ожидание:
def expected_value(a):
    if(len(a)!=2):
        warning="Warning! The incomming array to calculate expected value must have 2 rows."
        return warning
    if(round(sum(a[1]),2)!=1):
        warning="Warning! Summary of probabilities must be equal to 1."
        return warning
    M=0
    for j in range(len(a[0])):
            M = M + (a[0][j]*a[1][j])
    return M
def Ex(a):
    if(len(a)!=2):
        warning="Warning! The incomming array to calculate expected value must have 2 rows."
        return warning
    if(round(sum(a[1]),2)!=1):
        warning="Warning! Summary of probabilities must be equal to 1."
        return warning
    M=0
    for j in range(len(a[0])):
            M = M + (a[0][j]*a[1][j])
    return M

#Дисперсия:
def variance(a):
    X=0
    for j in range(len(a[0])):
            X = X + (((a[0][j])**2)*a[1][j])
    return X - (Ex(a)**2)
def var(a):
    X=0
    for j in range(len(a[0])):
            X = X + (((a[0][j])**2)*a[1][j])
    return X - (Ex(a)**2)

#Стандартное отклонение:
def standard_deviation(a):
    return var(a)**(0.5)
def sd(a):
    return var(a)**(0.5)


#Вариационные ряды для дискретных величин (другие - непрерывные величины)
#Принимает на вход массив данных, выдает на выход вариационный ряд, т.е. таблицу со значением,
#числом вхождений и частотой.
#Пример: на вход поступает набор оценок за экзамен: vs([5,4,3,2,3,4,3])
#На выходе получается следующая таблица:
#   2       3       4       5       - отсортированные значения в порядке возрастания
#   1       3       2       1       - количество вхождений каждой оценки
#   0.14    0.43    0.29    0.14    - частоты
def variational_series(a):
    a=sorted(a)
    k=1
    rep=[]
    for i in range(len(a)-1):
        if(a[i]==a[i+1]):
            k=k+1
        else:
            rep.append(k)
            k=1
    rep.append(k)
    a=sorted(set(a))
    fr=[]
    for i in range(len(rep)):
        fr.append(rep[i]/sum(rep))
    result=[[0 for j in range(len(rep))] for i in range(3)]
    result[0]=a
    result[1]=rep
    result[2]=fr
    return result


def vs(a):
    a=sorted(a)
    k=1
    rep=[]
    for i in range(len(a)-1):
        if(a[i]==a[i+1]):
            k=k+1
        else:
            rep.append(k)
            k=1
    rep.append(k)
    a=sorted(set(a))
    fr=[]
    for i in range(len(rep)):
        fr.append(rep[i]/sum(rep))
    result=[[0 for j in range(len(rep))] for i in range(3)]
    result[0]=a
    result[1]=rep
    result[2]=fr
    return result

#Среднее арифметическое вариационного ряда
def variational_series_arithmetic_average(a):
    M=0
    for i in range(len(a[0])):
        M=M+a[0][i]*a[2][i]
    return M


def vs_av(a):
    M=0
    for i in range(len(a[0])):
        M=M+a[0][i]*a[2][i]
    return M

#Метод вычисления медианы
def midpoint(a=[]):
    if(isinstance(a[0], list)!= True):
        asorted=sorted(a)#Сортируем поступивший на вход массив в порядке возрастания
        #Если в массиве нечётное число элементов, то принимает центральное значение в качестве медианы
        if((len(asorted) % 2) != 0):
            midpointIndex = int((len(asorted)-1)/2)
            midpoint = asorted[midpointIndex]
        else: #Если в массиве чётное число элементов, то в качестве медианы берём среднее арифметическое между двумя центральными значениями.
            ind1=(len(asorted)/2)-1
            ind2=len(asorted)/2
            midpoint = (asorted[int(ind1)]+a[int(ind2)])/2
    else:
        if((len(a[0]) % 2) != 0):
            midpointIndex = int((len(a[0])-1)/2)
            midpoint = a[0][midpointIndex]
        else: 
            ind1=(len(a[0])/2)-1
            ind2=len(a[0])/2
            midpoint = (a[0][int(ind1)]+a[0][int(ind2)])/2
    return midpoint

#Мода вариационного ряда
def variational_series_mode(a):
    b=a[1]
    m=0
    c=[]
    for i in range(len(b)):
        if(b[i]>m):
            m=b[i]
    for i in range(len(b)):
        if(b[i]==m):
            c.append(a[0][i])
    if(len(c)==1):
        return c[0]
    else:
        return c


def vs_mode(a):
    b=a[1]
    m=0
    c=[]
    for i in range(len(b)):
        if(b[i]>m):
            m=b[i]
    for i in range(len(b)):
        if(b[i]==m):
            c.append(a[0][i])
    if(len(c)==1):
        return c[0]
    else:
        return c

#Сортировка В.Р. по частоте
def variational_series_sort_by_rate(a):
    while(a[1]!=sorted(a[1])):
        for j in range(len(a[1])-1):
            if(a[1][j]>a[1][j+1]):
            
                a1=a[0][j]
                a2=a[1][j]
                a3=a[2][j]
            
                a[0][j]=a[0][j+1]
                a[1][j]=a[1][j+1]
                a[2][j]=a[2][j+1]
            
                a[0][j+1]=a1
                a[1][j+1]=a2
                a[2][j+1]=a3
    
    return a


def vs_sort_by_rate(a):
    while(a[1]!=sorted(a[1])):
        for j in range(len(a[1])-1):
            if(a[1][j]>a[1][j+1]):
            
                a1=a[0][j]
                a2=a[1][j]
                a3=a[2][j]
            
                a[0][j]=a[0][j+1]
                a[1][j]=a[1][j+1]
                a[2][j]=a[2][j+1]
            
                a[0][j+1]=a1
                a[1][j+1]=a2
                a[2][j+1]=a3
    
    return a

#Сортировка В.Р. по значению
def variational_series_sort_by_value(a):
    while(a[0]!=sorted(a[0])):
        for j in range(len(a[0])-1):
            if(a[0][j]>a[0][j+1]):
            
                a1=a[0][j]
                a2=a[1][j]
                a3=a[2][j]
            
                a[0][j]=a[0][j+1]
                a[1][j]=a[1][j+1]
                a[2][j]=a[2][j+1]
            
                a[0][j+1]=a1
                a[1][j+1]=a2
                a[2][j+1]=a3
    
    return a


def vs_sort_by_value(a):
    while(a[0]!=sorted(a[0])):
        for j in range(len(a[0])-1):
            if(a[0][j]>a[0][j+1]):
            
                a1=a[0][j]
                a2=a[1][j]
                a3=a[2][j]
            
                a[0][j]=a[0][j+1]
                a[1][j]=a[1][j+1]
                a[2][j]=a[2][j+1]
            
                a[0][j+1]=a1
                a[1][j+1]=a2
                a[2][j+1]=a3
    
    return a





#Дисперсия, стандартное отклонение вар ряда
def variational_series_variance(a):
    vssd=0
    for i in range(len(a[2])):
        vssd = vssd + a[2][i]*((a[0][i]-variational_series_arithmetic_average(a))**2)
    return vssd


def vs_var(a):
    vssd=0
    for i in range(len(a[2])):
        vssd = vssd + a[2][i]*((a[0][i]-variational_series_arithmetic_average(a))**2)
    return vssd

  
def variational_series_standart_deviation(a):
    return ((variational_series_variance(a))**(0.5))


def vs_sd(a):
    return ((variational_series_variance(a))**(0.5))





