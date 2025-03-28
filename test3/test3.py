import json
# Десериализуем json файл 
with open('D:\my_tests\\test3\\values.json', 'r', encoding='utf-8') as v:
    val = json.load(v)

# Создаем словарь значений, где ключ - это 'id', а значение - это 'value'
values = {i['id']: i['value'] for i in val['values']} 

with open('D:\my_tests\\test3\\tests.json', 'r', encoding='utf-8') as t:
    tests = json.load(t)

def answer(sample):
    if isinstance(sample, dict):
        for key in sample:
            if key == 'id' and sample[key] in values:
                # Устанавливаем новое значение по новому словарю values
                sample['value'] = values[sample[key]]
            else:
                # Рекурсивно для вложенного словаря
                answer(sample[key])
    elif isinstance(sample, list):
        for i in sample:
            # Рекурсивно для каждого элемента списка
            answer(i)

answer(tests)

# Сериализуем обновленные данные в новый json файл
with open('D:\my_tests\\test3\\report.json', 'w', encoding='utf-8') as dr:
    json.dump(tests, dr, indent=4)