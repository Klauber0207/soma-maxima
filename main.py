#arr = [1,2,3,4,5]

def AlturaII(arr):
    soma_maxima = arr[0]
    soma_atual = 0

    for i in range(len(arr)):
        soma_atual = 0
        for j in range(i,len(arr)):
            soma_atual += arr[j]
            soma_maxima = max(soma_maxima,soma_atual)

    return soma_maxima

arr = [20, -30, 15, -10, 30, -20, -30, 30]

print(AlturaII(arr))