import turtle
import random
import math




class Xelones(turtle.Turtle):
    aktina = 0

    def xelona(met):
        turtle.Turtle.__init__(met, shape="turtle")

    def sxedio(met, a, b, aktina=(random.randrange(10, 500, 1))):
        met.penup()
        met.setposition(a, b)
        met.pendown()
        met.circle(aktina)
        met.aktina = aktina


    def Diadikasia(met):
        suntetagmenes = [(random.randrange(0,500,1), (random.randrange(0,500,1)) )]
        for thesi in suntetagmenes:
            met.sxedio(thesi[0], thesi[1])
        return suntetagmenes[0]

    def Apotelesma(met, stath):
        athroisma = 0
        for j in range(0, len(stath)):
            for i in range(0, len(stath)):
                if j != i:
                    k = math.sqrt(abs((pow((stath[j][0]-stath[i][0]), 2) + (pow((stath[j][1]-stath[i][1]), 2)))))
                    if k <= 2*met.aktina:

                        athroisma += 1
                        break
        return athroisma





if __name__ == "__main__":
    x = Xelones()
    lista = []
    for j in  range(1, 21):
        kentro = x.Diadikasia()

        lista.append(kentro)
    turtle.getscreen()._root.mainloop()
    metritis = x.Apotelesma(lista)
    print ("O arithmos ton kuklon pou temnontai einai %s ." % (metritis,))


