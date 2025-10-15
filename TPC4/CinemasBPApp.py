import CinemasBP as cn
sala1 = (150, [], "a")
sala2 = (200, [], "b")
cinema1 = []
...

res =1
cinema1 = cn.inserirSala(cinema1,sala1)
cinema1 = cn.inserirSala(cinema1,sala2)
while res!=0:
    res=cn.menu()
    if res == 1:
        cn.listar(cinema1)
    if res == 2:
        cn.listardisponibilidade(cinema1)

    if res == 3:
        cn.disponivel(cinema1, input("Qual o filme que deseja saber a disponibilidade???"), input("Qual o lugar da sala que deseja saber a disponibilidade???"))

    if res == 4:
        cn.vendebilhete(cinema1, input("Qual o filme que deseja ver?"), input("Qual o lugar que deseja?"))
    if res == 5:
        novasala= cn.criarsala(input("Nome do filme?"), input("Tamanho da sala?"))
        cn.inserirSala(cinema1, novasala )
    if res == 6:
        cn.cancelarbilhete(cinema1, input("Qual o filme que deseja remover a reserva???"), str(input("Qual o lugar da sala que deseja cancelar???")))
    if res ==7:
        cn.eliminarsala(cinema1, input("Qual o filme reproduzido na sala deseja remover???"))
    if res ==0:
        break
    


 



