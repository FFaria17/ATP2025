import Metereologia as met
tabMeteo = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]

i=met.menu()

while i != 0:
    if i==1:
        print(met.medias(tabMeteo))
    elif i==2:
        met.guardaTabMeteo(tabMeteo, "metereologia.txt")
        print("A tabela foi guardada no ficheiro metereologia.txt")
    elif i==3:
        tabMeteo=met.carregaTabMeteo("metereologia.txt")
        print(tabMeteo)
    elif i==4:
        print(met.minMin(tabMeteo))
    elif i==5:
        print(met.amplTerm(tabMeteo))
    elif i==6:
        print(met.maxChuva(tabMeteo))
    elif i==7:
        print(met.diasChuvosos(tabMeteo, float(input("Escolhe o valor limite"))))
    elif i==8:
        print(met.maxPeriodoCalor(tabMeteo, float(input("Escreva o limite desejado"))))
    elif i==9:
        met.grafTabMeteo(tabMeteo)
    i=met.menu()