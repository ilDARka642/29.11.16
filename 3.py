import turtle as tur
def kohh(n,x):
    if n==0:
        return
    if n==1:
        tur.forward(x)
        tur.left(60)
        tur.forward(x)
        tur.right(120)
        tur.forward(x)
        tur.left(60)
        tur.forward(x)
    if n>0:
        kohh(n-1,x)
        tur.left(60)
        kohh(n-1,x)
        tur.right(120)
        kohh(n-1,x)
        tur.left(60)
        kohh(n-1,x)
tur.penup()
tur.goto(-200, 200)
tur.pendown()
tur.speed(50)
for i in range(3):
    kohh(4,10)
    tur.right(120)
input()