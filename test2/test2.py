try:
    with open('D:\my_tests\\test2\circle.txt', 'r', encoding='utf-8') as f:
        centr_x = float(f.readline().strip())
        centr_y = float(f.readline().strip())
        radius = float(f.readline().strip())

    with open('D:\my_tests\\test2\points.txt', 'r', encoding='utf-8') as p:
        points = [tuple(map(float, l.strip().split())) for l in p]

    answer = []
    for x, y in points:
        '''по т. Пифагора
        расстояние между (x, y)'''
        dis = ((x - centr_x) ** 2 + (y - centr_y) ** 2) ** 0.5
        if dis < radius:
            answer.append(1) # внутри окружности 
        elif dis == radius:
            answer.append(0) # на окружности
        else:
            answer.append(2) # снаружи окружности
        
    print('\n'.join(map(str, answer)))

except FileNotFoundError as e:
    print(f'Файл не найден. {e}')
except ValueError as e:
    print(f'Не верное содержимое файла. {e}')
