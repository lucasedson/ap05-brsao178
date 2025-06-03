# 3. Crie um programa que verifique se uma senha é forte. 
# Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. 
# O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.​
def tem_numero(string):
    return any(char.isdigit() for char in string)

def valida_senha(senha):
    if len(senha) < 8:
        return False, "Digite uma senha com pelo menos 8 caracteres!"
    elif tem_numero(senha) is False:
        return False,"Digite uma senha que tenha pelo menos um número!"
    else:
        return True, "Parábens, você cadastrou uma nova senha!"

if __name__ == "__main__":
    while True:
        senha = input("Cadastre a senha: ")

        if senha == "sair":
            exit()
            
        status, msg = valida_senha(senha)

        if  status == False:
            print(msg)
        else:
            print(msg)
            break