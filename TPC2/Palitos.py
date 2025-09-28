import random as random
x=21
jogador=input("Quer jogar em primeiro ou segundo lugar? (1/2) ")
while jogador!="1" and jogador!="2":
    print("Número inválido")
    jogador=input("Quer jogar em primeiro ou segundo lugar? (1/2) ")
if jogador == "1":
    while x > 0:
        y=5
        n = int(input("Quantas peças você quer tirar? (1,2,3,4) "))
        while n not in [1,2,3,4] or n > x:
            print("Número inválido")
            n = int(input("Quantas peças você quer tirar? (1,2,3,4) "))
        x -= n
        print("Restam",x,"peças")
        if x <= 0:
            print("Você perdeu!")
            break
        y -= n
        print("O computador tirou",y,"peças")
        x -= y
        print("Restam",x,"peças")
elif jogador == "2":
    while x > 0:
        if x==1:
            print("o computador tirou 1 peça")
            print("O computador perdeu!")
            break
        elif x % 5 == 1:
            y = random.randint(1, 4)
            print("O computador tirou", y, "peças")
            x -= y
        else:
            y = x % 5
            if y == 0:
                y = 4
                print("O computador tirou", y, "peças")
                x -= y
            else:
                print("O computador tirou", y-1, "peças")
                x -= y-1
        print("Restam", x, "peças")
        n = int(input("Quantas peças você quer tirar? (1,2,3,4) "))
        while n not in [1, 2, 3, 4] or n > x:
            print("Número inválido")
            n = int(input("Quantas peças você quer tirar? (1,2,3,4) "))
        x -= n
        print("Restam", x, "peças")
        if x == 0:
            print("Você perdeu!")
            break

