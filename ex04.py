def verifica_paridade(numero):
    try:
        if int(numero) % 2 == 0:
            return "PAR", "O numero é par"
        else:
            return "IMPAR", "O numero é impar"
    
    except ValueError:
        return False, "Digite um numero inteiro"

if __name__ == "__main__":
    
    lista_par = []
    lista_impar = []
    while True:

        numero = input("Digite um numero ou digite 'sair': ")

        if numero == "sair":
            print("Par: ", lista_par)
            print("Impar: ", lista_impar)
            print("Quantidade de numeros pares: ", len(lista_par))
            print("Quantidade de numeros impares: ", len(lista_impar))
            break

        status, msg_paridade = verifica_paridade(numero)

        if status == "PAR":
            print(msg_paridade)
            lista_par.append(int(numero))
            
        elif status == "IMPAR":
            print(msg_paridade)
            lista_impar.append(int(numero))
            
        elif status == False:
            print(msg_paridade)
    