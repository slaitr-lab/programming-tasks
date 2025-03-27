# Инициализация переменных
n, m = int(input()), int(input())
path = []
start_indx = 0
arg = list(range(1, n + 1))

while True:  
    path.append(arg[start_indx])
    start_indx = (start_indx + m - 1) % n
    if arg[start_indx] == 1:
        break

print(''.join(map(str, path)))


