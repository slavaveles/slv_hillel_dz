# За допомогою циклу for:
#
# Знайти максимальне число в списку але не більше 100
print('# максимальне число в списку але не більше 100')
l = [500,0,101,10,50,51,99,150,400,-100,-30]

m = l[0]

for i in l:
    if (i > m or m > 100) and i <= 100:
        m = i

if m <= 100:
    print(f"MAX = {m}")
else:
    print('No solution')

# Знайти суму всіх чисел в списку що діляться на 3
print('# суму всіх чисел в списку що діляться на 3')
l = [1,2,3,4,5,6,7,8,9,11,12]

s = 0
for i in l:
    if i%3 ==0:
        s += i
print(f"Sum of 3d multiples = {s}")

# Вивести квадрати чисел від 10 до 30

print('# квадрати чисел від 10 до 30')
for i in range (10,30) : # if condition is 30 inclusive then range (10, 31)
    print(f"{i}-square  = {i**2}")

# Є список слів, знайти слово в якому к-ть букв найбільша.

print('# знайти слово в якому к-ть букв найбільша')
l = ["mom", "dad", "granny", "sister", "brother", "son", "daughter"]
m = len(l[0])
longestword = l[0]
for i in l:
    if len(i) > m :
        longestword = i

print(longestword)

# Порахувати і вивести на екран окремо суму парних і непарних чисел списку

print('# на екран окремо суму парних і непарних чисел списку')
l = [1,2,3,4,23,22,2,4]

s_even = 0
s_odd = 0

for i in l:
    if i % 2 == 0:
        s_even += i
    else:
        s_odd += i
print(f"s_even = {s_even}")
print(f"s_odd = {s_odd}")

# Задачи на if:
#
# Розв'язати квадратне рівняння ax^2 +bx +c = 0 ( a,b,c вводяться з клавіатури ). Якщо забули як розв'язувати то
# почитайте https://miyklas.com.ua/p/algebra/8/kvadratni-rivniannia-14001/formuli-koreniv-kvadratnogo-rivniannia-14004/re-d9b52c91-9c99-47f5-869d-b44161760768

print('# Розв\'язати квадратне рівняння ax^2 +bx +c = 0 ( a,b,c вводяться з клавіатури )')
a = float(input("pls enter a:"))
b = float(input("pls enter b:"))
c = float(input("pls enter c:"))

D = b*b - 4.0*a*c
#print(D)

if D < 0:
    print('no real roots')
else:
    d = D**0.5
    print(f"x1 = {(-b + d) / a*2.0}")
    print(f"x2 = {(-b - d) / a*2.0}")

# Знайти мінімум з трьох чисел.

print('# Знайти мінімум з трьох чисел')
a = float(input("pls enter a:"))
b = float(input("pls enter b:"))
c = float(input("pls enter c:"))

l = [a,b,c]

m = l[0]
for i in l:
     if i < m:
         m = i
print(f"min = {m}")

# Користувач з клавіатури вводить рік, потрібно написати Yes, якщо рік високосний, No в іншому випадку.

print('#...Yes, якщо рік високосний, No в іншому випадку.')
year = int(input("pls enter year: "))
if year % 4 != 0 or (year % 4 == 0 and year % 100 == 0 and year % 400 != 0):
    print('No')
else :
    print('Yes')

# Користувач з клавіатури вводить бал в цифровій формі ( від 0 до 100 ), потрібно вивести в консоль бал згідно болонської системи:
# 1. Нижче 25 – F
#
# 2. 25 - 45 – E
#
# 3. 45 - 50 – D
#
# 4. 50 - 60 – C
#
# 5. 60 - 80 – B
#
# 6. Више 80 – A

print('# бал згідно болонської системи')
grade = int(input("Enter numerical grade: "))

if grade < 25:
    print(f"grade {grade} = F")
elif grade < 45:
    print(f"grade {grade} = E")
elif grade < 50:
    print(f"grade {grade} = D")
elif grade < 60:
    print(f"grade {grade} = C")
elif grade < 80:
    print(f"grade {grade} = B")
else:
    print(f"grade {grade} = A")

