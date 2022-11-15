#fim = int(input("Digite o Último número a imprimir:"))
#x = 0
#while x <+ fim:
#  if x % 2 == 0:
#      print(x)
#  x = x + 1

#while x <= fim:
#    print(x)
#    x = x + 3

#calculadora simples de soma:
#n = 1
#soma = 0
#while n <= 5:
#  x = int(input(f"Digite o {n} número"))
#  soma = soma + x
#  n = n + 1
#print(f"Soma: {soma}")


valor = int(input("Digite o valor a pagar:"))
cedulas = 0
atual = 50
apagar = valor
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f"{cedulas} cédulas(s) de R${atual}")
        if apagar == 0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0