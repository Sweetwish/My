from colorama import init
from colorama import Fore, Back, Style
init() #Подключение модуля колорама для подсветки текста
print (Back.MAGENTA)


print("Привет! Я Sweetwish,a это мой первый калькулятор. =D")
what=input("Что делаем? (+,-,*,/): ")
print (Back.GREEN)
a=float(input("Введи первое число: "))
b=float(input("Введи второе число: "))
print (Back.CYAN)
if what=="+":
	c=a+b
	print("Результат:"+str(c))
elif what=="-":
	c=a-b
	print("Результат:"+str(c))
elif what=="*":
	c=a*b
	print("Результат:"+str(c))

elif what=="/":
	c=a/b
	print("Результат:"+str(c))
else:
	print("Сорян,что-то пошло не так =( Попробуй снова!")

input() 
