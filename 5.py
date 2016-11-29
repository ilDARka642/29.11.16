import turtle as tur

def levi(n,x):
    if n==0:
        return
    if n==1:
        tur.left(45)
        tur.forward(x)
        tur.right(90)
        tur.forward(x)
        tur.left(45)
    else:
        tur.left(45)
        levi(n-1,x)
        tur.right(90-(n-2)*45)
        levi(n-1,x)

tur.penup()
tur.goto(-200, 0)
tur.pendown()
tur.speed(5000000)
levi(12,5)
input()