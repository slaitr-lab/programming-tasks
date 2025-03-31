import json
import os

values_file_path = os.path.join('D:\\', 'my_tests', 'test3', 'values.json')
tests_file_path = os.path.join('D:\\', 'my_tests', 'test3', 'tests.json')
report_file_path = os.path.join('D:\\', 'my_tests', 'test3', 'report.json')

with open(values_file_path, 'r', encoding='utf-8') as v:
    val = json.load(v)

# Создаем словарь значений, где ключ - это 'id', а значение - это 'value'
values = {i['id']: i['value'] for i in val['values']} 

with open(tests_file_path, 'r', encoding='utf-8') as t:
    tests = json.load(t)

def answer(sample):
    if isinstance(sample, dict):     
        if 'id' in sample and sample['id'] in values:
            # Устанавливаем новое значение по новому словарю values
            sample['value'] = values[sample['id']]
        for key in sample:
            answer(sample[key])

    elif isinstance(sample, list):
        for i in sample:
            # Рекурсивно для каждого элемента списка
            answer(i)

answer(tests)


with open(report_file_path, 'w', encoding='utf-8') as dr:
    json.dump(tests, dr, indent=4)