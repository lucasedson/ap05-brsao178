# 2. Crie um programa que permita a um professor registrar as notas de uma turma. 
# O programa deve continuar solicitando notas até que o professor digite 'fim'. 
# Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. 
# No final, deve exibir a média da turma. Notas = [] -> len(Notas)​
lista_notas_alunos = []
def registrar_notas(lista_notas, nova_nota):    
    try:
        if 0 <= float(nova_nota) <= 10:
            lista_notas.append(float(nova_nota))
    except:
        ...

media = lambda lista: sum(lista)/len(lista)

if __name__ == "__main__":
    while True:
        nota: str = input("Digite uma nova nota! ou digite 'q' para sair: ")
        if nota == "q" and len(lista_notas_alunos) == 0:
            exit()
            break
        elif nota == "q" and len(lista_notas_alunos) > 0:
            print("Notas: ", lista_notas_alunos)
            print("A média da turma é: ", media(lista_notas_alunos))
            break
        else:
            registrar_notas(lista_notas_alunos, nota)
        