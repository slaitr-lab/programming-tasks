with open('D:\my_tests\\test4\\random_numbers.txt', 'r', encoding='utf-8') as r:
    nums = [int(i.strip()) for i in r]

def median(nums: list) -> float:
    mid_index = len(nums) // 2
    if len(nums) % 2 == 0:
        # Если количество элементов четное, возвращаем среднее значение двух центральных чисел
        return (nums[mid_index - 1] + nums[mid_index]) / 2
    # Если количество элементов нечетное, возвращаем центральный элемент
    return nums[mid_index]

def ans(nums: list) -> int:
    if not nums:
        return 0
    sor_nums = sorted(nums)
    med = median(sor_nums)
    # Сумма разностей до медианы 
    return sum(abs(med - n) for n in nums)

print(ans(nums))