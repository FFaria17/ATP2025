
def criarAluno(nome, id, notaTPC, notaProj, notaTeste):
    return (nome, id, [notaTPC, notaProj, notaTeste])
def criarTurma(turma):
    turma.clear()
    return turma
def menu():
    c=int(input("\n (1) Criar turma  \n (2) Inserir aluno \n (3) Listar a turma \n (4) Consultar aluno por id \n (8) Guardar turma em ficheiro \n (9) Carregar turma de ficheiro \n (0) Sair \n"))
    return c
def inserirAluno(turma):
    turma.append(criarAluno(input("Qual o nome do Aluno?"), input("Qual o id do aluno?"), float(input("Qual a nota do tpc?")),  float(input("Qual a nota do projeto?")),  float(input("Qual a nota do Teste?"))))
def listarTurma(turma):
    for e in turma:
        print(e)
    return
def consultarAluno(turma, id):
    i=0
    while i<len(turma):
        if id==turma[i][1]:
            return print(f"O Aluno com o id {id} é: {turma[i]}")   
        i+=1
    return print("Aluno nao encontrado")
        
def guardarTurma(turma,ficheiro):
    with open(ficheiro, "w") as f:
        for aluno in turma:
            nome, id, notas = aluno
            linha = f"{nome},{id},{notas[0]},{notas[1]},{notas[2]}\n"
            f.write(linha)

def carregarTurma(turma, ficheiro):
    turma.clear()
    with open(ficheiro, "r") as f:
        for linha in f:
            partes = linha.strip().split(",")
            nome = partes[0]
            id = partes[1]
            notas = [float(partes[2]), float(partes[3]), float(partes[4])]
            turma.append((nome, id, notas))
    return turma
