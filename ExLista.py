#separa pares de impares dentro do V = []
V = [9, 8, 7, 12, 0, 13, 21]
P = []
I = []
for e in V:
    #print("esse é o valor de ", e)
    if e % 2 == 0:
        P.append(e)
    else:
        I.append(e)

print("Pares: ", P)
print("Impares: ", I)

#----------------------------------------

#outro exp: mostra o valor máximo
L = [1, 7, 2, 4]
maximo = L[0]
for e in L:
    #print(e) #cada rodada o valor de E
    if e > maximo:
        #print("pegou", e) #saber como guardou
        maximo = e
print("o valor máximo", maximo)