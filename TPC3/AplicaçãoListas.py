import random as rm
lista=[]
def criarlista(n):
    res=[]
    i=0
    while i<n:
        res.append(rm.randint(1,100))
        i+=1
    return res

def lerlista(n):
    res=[]
    x=0
    while x < n:
        res.append(int(input(f"Qual o elemento {x+1} ? ")))
        x+=1
    return res

def somalista(lista):
    x=0
    for e in lista:
        x+=e
    return x      

def medialista(lista):
    med = somalista(lista)/len(lista)
    return med

def maiorlista(lista):
    max=lista[0]
    for e in lista:
        if e>max:
            max=e
    return max

def menorlista(lista):
        min=lista[0]
        for e in lista:
            if e<min:
                min=e
        return min

def ordemcrescente(lista):
    i = 0
    while i < len(lista) - 1:
        if lista[i] > lista[i+1]:
            return False
        i += 1
    return True

def ordemdecrescente(lista):
    i = 0
    while i < len(lista) - 1:
        if lista[i] < lista[i+1]:
            return False
        i += 1
    return True

def encontrarelemento(lista, n):
    posicoes = []
    i = 0
    while i < len(lista):
        if lista[i] == n:
            posicoes.append(i)
        i += 1
    if len(posicoes) == 0:
        return [-1]
    return posicoes

#def encontrarelemento(lista, n):
 #   posicoes = []
  #  for e in lista:
   #     if e == n:
    #        posicoes.append(lista.index(e))
    #if len:
    #    return [-1]
    #return posicoes

    

comando=int(input("(1) Criar Lista \n(2) Ler Lista \n(3) Soma \n(4) Media \n(5) Maior \n(6) Menor \n(7) Ordem crescente \n(8) Ordem decrescente \n(9) Procurar elemento \n(0) Sair: "))

while comando != 0:
    if comando == 1:
        lista=criarlista(int(input("Quantos elementos tem a lista? ")))
        print(lista)
    elif comando == 2:
        lista=lerlista(int(input("Quantos elementos tem a lista? ")))
        print(lista)
    elif comando == 3:
        if len(lista) == 0:
            print("A lista está vazia")
        else:
            print(somalista(lista))
    elif comando == 4:
        if len(lista) == 0:
            print("A lista está vazia")
        else:
            print(medialista(lista))
    elif comando == 5:
        if len(lista) == 0:
            print("A lista está vazia")
        else:
            print(maiorlista(lista))
    elif comando == 6:
        if len(lista) == 0:
            print("A lista está vazia")
        else:
            print(menorlista(lista))
    elif comando == 7:
        if len(lista) == 0:
            print("A lista está vazia")
        elif ordemcrescente(lista):
            print(f"A lista {lista} esta por odem crescente")
        else:
            print(f"A lista {lista} NAO esta por ordem crescente")
    elif comando == 8:
        if len(lista) == 0:
            print("A lista está vazia")
        elif ordemdecrescente(lista):
            print(f"A lista {lista} esta por odem decrescente")
        else:
            print(f"A lista {lista} NAO esta por ordem decrescente")
    elif comando == 9:
        if len(lista) == 0:
            print("A lista está vazia")
        else:
            print(f"O elemento esta na posição {encontrarelemento(lista, int(input("Qual o elemento a procurar? ")))}")
        
    comando=int(input("(1) Criar Lista \n(2) Ler Lista \n(3) Soma \n(4) Media \n(5) Maior \n(6) Menor \n(7) Ordem crescente \n(8) Ordem decrescente \n(9) Procurar elemento \n(0) Sair: "))
print(f"A lista guardada neste momento é {lista}")





         
         
         























