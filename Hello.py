#int переменная целочисленная integer
number=5
age=20

#float Вещественная (дробная) переменная
fnumber=5.7

#string Текст переменная str
name="Tanya"

#bool 
status=True

#вывод на экран
print("Что вывести на экран?")

#Экранирование если нужны именно кавычки
print("Он \"плохой\" человек")

#перевод строки
print("Привет\nмир")

#канкатенация (делать переменные одного типа)
print("Привет,меня зовут "+name+"!")
print("Мне "+str(age)+" года")

#ввод переменной
name1=input("Введите свое имя: ")
age1=input("Укажите свой возраст: ")

print("Привет "+name1+"!")
print("Тебе уже "+age1+" года")

#+,-,*,/,**(возведение в степень), % (деление по модулю) Унарный минус,округление,пи

a=5
b=10
c=a+b
print(c)
d=a-b
print(d)
e=a*b
print(e)
f=a/b
print(f)
g=a**b
print(g)
h=a%b
print(h)

#унарный минус
a=-a
print(a)

i=5.65

print(round(i))# округление
import math
i=5.65

print(math.ceil(i))# округление

import math
print(matg.pi)