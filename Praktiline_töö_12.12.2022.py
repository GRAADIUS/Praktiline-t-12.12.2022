from math import *
from random import *
#1
C=float(input("введите длину окружности: "))
D=round(C/pi,2)
print("диаметр дерева:", D)
print()
#2
A=float(input("введите ширину участка:"))
B=float(input("введите длину участка:"))
D=round(sqrt(A**2+B**2),2)
print("диагональ участка:",D)
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
km=(litrid/kilomeetrid)*100
print(f"kütusekulu {km}")
print()
#9
m=int(input("minutid:"))
m=m/60
tee=m*29,9
print(f"jõuab {tee} km")
#10
m=int(input("sisesta ´aja minutes"))








