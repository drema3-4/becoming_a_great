def A() -> int:
    '''Данная функция являяется
    решением задачи А первого дз по
    алгоритмам'''
    P, V = [int(num) for num in (input('>> ').split(' '))]
    Q, M = [int(num) for num in (input('>> ').split(' '))]
    return ((P + V) if (P + V > Q + M) else (Q + M)) -\
           ((P - abs(V)) if (P - abs(V) < Q - abs(M)) else (Q - abs(M))) +\
           1

print(A())