
def inserirSala( cinema, c ):
    cinema.append(c)
    return cinema

def listar(cinema):
    for e in cinema:
        print(e)
    return

def menu():
    c=int(input("\n (1) Listar Salas  \n (2) Listar Disponibilidade \n (3) Verificar Disponibilidade \n (4) Reservar Bilhete \n (5) Adicionar Nova Sala \n (6) Cancelar Bilhete \n (7) Eliminar Sala \n (0) Sair \n"))
    return c

def disponivel(cinema, filme , lugar):
    res=-1
    i=0
    while res==-1 and i<len(cinema):
        if filme == cinema[i][2]:
            res=i
            for e in cinema[i][1]:
                if e==lugar:
                    print(f"O lugar {lugar} esta OCUPADO")
                    return print(f"Os lugares oculpados nesta sala sao: {cinema[res][1]}")
                    
        i+=1
    print(f"Os lugares oculpados nesta sala sao: {cinema[res][1]}")
    return print(f"O lugar {lugar} esta LIVRE")

def vendebilhete( cinema, filme, lugar ):
    res=-1
    i=0
    while res==-1 and i<len(cinema):
        if filme == cinema[i][2]:
            res=i
        i+=1
    if res ==-1:
        return print("O filme nao foi encontrado")
    for e in cinema[res][1]:
        if e==lugar:
            return print("O lugar esta oculpado!")
    cinema[res][1].append(lugar)
    return cinema

def listardisponibilidade(cinema):
    for e in cinema:
        print(f"CinemasBP - {e[2]} - {e[0]-len(e[1])} Lugares Disponiveis")
    return

def criarsala( nome, lugares):
    res=(int(lugares), [], nome)
    return res

def cancelarbilhete(cinema, filme, lugar):
    res = -1
    for i in range(len(cinema)):
        if cinema[i][2] == filme:
            res = i
            break
    if res == -1:
        print("O filme nao foi encontrado")
        return cinema
    i = 0
    found = False
    while i < len(cinema[res][1]) and not found:
        if str(cinema[res][1][i]) == lugar:
            valor = cinema[res][1][i]
            cinema[res][1].remove(valor)
            print(f"O lugar {lugar} esta agora LIVRE!")
            found = True
        else:
            i += 1
    if not found:
        print("O lugar nao esta OCUPADO")
    return cinema

def eliminarsala(cinema, filme):
    for e in cinema:
        if e[2] == filme:
            cinema.remove(e)
            print(f"A sala do filme {filme} foi removida")
            return cinema
    print("O filme nao foi encontrado")
    return cinema
        