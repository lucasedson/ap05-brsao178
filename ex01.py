def calcular(a,b, op='+'):

    if op == '+':
        return float(a + b)
    elif op == '-':
        return float(a + b)
    elif op == '*':
        return float(a + b)
    elif op == '/':
        return float(a + b)
    else:
        return False, "Digite um operador válido. + (soma), -(subtração), *(multiplicação), /(divisão)"


if __name__ == "__main__":
    while True:
        try:
            primeiro_valor = input("Digite o primeiro valor: ")            
            segundo_valor = input("Digite o segundo valor: ")
            operador = input("Digite o operador: ")

            calculo = calcular(primeiro_valor, segundo_valor,operador)
            if calculo[0] == False:
                print(calculo[1])
                continue
            print(calculo)
            break

        except ValueError:
            print("Digite apenas números")
        except ZeroDivisionError:
            print("Não é possível dividir por zero." )
            
