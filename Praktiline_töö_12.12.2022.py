from math import *
from random import *
#1
try: #если можно выполнить
    C=float(input("введите длину окружности: "))
    if C>0:
        D=round(C/pi,2)
        print("диаметр дерева:", D)
    else:
        print("число не меньше нуля")
except:
    print("не верный формат")
print()
#2
try:
    A=float(input("введите ширину участка:"))
    B=float(input("введите длину участка:"))
    if A>0 and B>0:
        D=round(sqrt(A**2+B**2),2)
        print(f"диагональ участка: {D}")
    else:
        print("числа не меньше нуля")
except:
    print("none")
print()
#3
aeg=float(input("Сколько часов ехали? "))
teepikkus=float(input("Сколько километров вы проехали? "))
kiirus=teepikkus/aeg
print("Ваша скорость была "+str(kiirus)+" km/h ")
print()
#4
a1=int(input("esimene arv:"))
a2=int(input("teine arv:"))
a3=int(input("kolmas arv:"))
a4=int(input("neljas arv:"))
a5=int(input("viies arv:"))
XXX=float(round((a1+a2+a3+a4+a5)/5))
print("среднее значение:", XXX)
print()
#5
print("  @..@")
print(" (----)")
print("( \__/ )")
print(" ^^ "'""'" ^^ ")
print()
#6
a=randint(0,100)
b=randint(0,100)
c=randint(0,100)
print(f"a={a}\nb={b}\nc={c}")
P=a+b+c
print("периметр треугольника: {P}")
print()
#7
p=randint(1,6)
summa=(12.9*1.1)/p
print=(f"{P}-st, igaüks maksab {summa}")
#8
litrid=float(input("литры заправленного топлива:"))
kilomeetrid=float(input("пройденные километры:"))
km=round((litrid/kilomeetrid)*100,2)
print(f"kutusekulu {km}")
print()
#9
m=int(input("minutid:"))
m=m/60
tee=m*29,9
print(f"jõuab {tee} km")
print()
#10
m=int(input("sisesta ´aja minutes"))
h=m//60

m=m%60
print(f"{h}:{m}")