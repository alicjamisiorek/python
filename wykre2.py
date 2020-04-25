import matplotlib.pyplot as p
x = range(-10,11)
a=int(input('podaj a\n'))
b=int(input('podaj b\n'))
y=[]
for i in x:
    y.append(a*i+b)
p.plot(x,y)
p.title('wykres')
p.grid(True)
p.show()