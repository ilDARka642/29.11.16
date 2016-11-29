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
        tur.color('red')
    else:
        kohh(n-1,x)
        tur.left(60)
        kohh(n-1,x)
        tur.right(120)
        kohh(n-1,x)
        tur.left(60)
        kohh(n-1,x)
        tur.color('green')
tur.penup()
tur.goto(-500, 0)
tur.pendown()
tur.speed(1)
kohh(4,10)
input()