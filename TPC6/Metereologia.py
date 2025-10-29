import matplotlib.pyplot as plt

def medias(tabMeteo):
    res = []
    x=0
    while x< len(tabMeteo):
        med= (tabMeteo[x][1]+ tabMeteo[x][2])/2
        res.append((tabMeteo[x][0], med))
        x+=1
    return res

def guardaTabMeteo(t, fnome):
    f = open(fnome, "w", encoding='utf-8')
    for dia in t:
        data, tempMin, tempMax, prec = dia
        linha = f"{data[0]},{data[1]},{data[2]},{tempMin},{tempMax},{prec}\n"
        f.write(linha)
    f.close()
    return

def carregaTabMeteo(fnome):
    res = []
    f= open(fnome, encoding='utf-8')
    for linha in f:
        campos=linha.split(",")
        res.append(((int(campos[0]),int(campos[1]),int(campos[2])), float(campos[3]), float(campos[4]), float(campos[5])))
    f.close()
    return res

def minMin(tabMeteo):
    minima=tabMeteo[0][1]
    i=0
    while i<len(tabMeteo):
        if minima>tabMeteo[i][1]:
            minima=tabMeteo[i][1]
        i+=1
    return minima

def amplTerm(tabMeteo):
    res=[]
    for e in tabMeteo:
        res.append((e[0],e[2]-e[1]))
    return res 

def maxChuva(tabMeteo):
    max_prec=tabMeteo[0][3]
    i=0
    while i<len(tabMeteo):
        if max_prec<tabMeteo[i][3]:
            max_prec=tabMeteo[i][3]
            max_data=tabMeteo[i][0]
        i+=1
    return (max_data, max_prec)

def diasChuvosos(tabMeteo, p):
    res=[]
    print(p)
    for e in tabMeteo:
        if e[3]>=p:
            res.append((e[0],e[3]))
    return res

def maxPeriodoCalor(tabMeteo, p):
    res=0
    max=0
    for e in tabMeteo:
        if e[3]<p:
            res+=1
        else:
            if max <=res:
                max=res
    if max ==0:
        return res
    else:
        return max

def extraiTMin(t):
    res=[]
    for _,tmin,_,_ in t:
        res.append(tmin)
    return res

def extraiTMax(t):
    res=[]
    for _,_,tmax,_ in t:
        res.append(tmax)
    return res

def extraiPrecip(t):
    res=[]
    for _,_,_,precip in t:
        res.append(precip)
    return res

def grafTabMeteo(t):
    #Tmin
    x1 = list(range(1,len(t)+1))
    y1= extraiTMin(t)
    plt.plot(x1,y1, label="Tempreatura Minima")

    #Tmax
    x2 = list(range(1,len(t)+1))
    y2= extraiTMax(t)
    plt.plot(x2,y2, label="Tempreatura Maxima")
    
    #Precip
    x3=  list(range(1,len(t)+1))
    y3= extraiPrecip(t)
    plt.plot(x3,y3, label="Tempreatura Maxima")

    plt.title("Metrologia")
    plt.legend()
    plt.show()
    return

def menu():
    return int(input(f" 1- Temperatura media \n 2- Guardar Tabela \n 3- Carregar tabela \n 4- Temperatura minima \n 5- Amplitude termica \n 6- Precipitaçao Maxima \n 7- Dias com precipitaçao acima de x \n 8- Numero consecutivo de dias com precipitaçao abaixo de X \n 9- Grafico da tabela \n 0- Sair \n"))