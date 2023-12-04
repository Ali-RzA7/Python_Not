from turtle import *

shape("blank")

color("red", "green")

begin_fill()
hideturtle()
pensize(2)

# Kare
for i in range(4):
    forward(50)
    left(90)
# Üçgen
for i in range(3):
    forward(50)
    lt(120)
#Daire
circle(100)

#Japon bayrağı
for i in range(2):
    forward(150)
    right(90)
    forward(100)
    right(90)    

penup() # çizim olmaz
goto(75, -80)
pendown() # çizim başlar

N = int(input("Köşe Sayısı: "))
açı = 360/N
for i in range(N):
    forward(50)
    left(açı)
    
end_fill()