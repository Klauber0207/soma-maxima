import time
start = time.process_time()
#arr = [20, -30, 15, -10, 30, -20, -30, 30]

def SomaSubArray(arr, n):
    maximo_atual = arr[0]
    maximo_final = 0

    for i in range(0, n):
        maximo_final = maximo_final + arr[i]
        if maximo_final < 0:
            maximo_final = 0

        elif (maximo_atual < maximo_final):
            maximo_atual = maximo_final

    return maximo_atual

arr = [20, -30, 15, -10, 30, -20, -30, 30]
print(SomaSubArray(arr, len(arr)))

end = time.process_time()
print(end - start)
