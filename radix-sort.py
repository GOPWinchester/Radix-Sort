def counting_sort(list, exp):
    bukets = [[] for _ in range(10)]
    for e in list:
        bukets[((e // exp) % 10)].append(e)
    count = 0
    new_list = []
    while count < 10:
        if len(bukets[count]):
            new_list.append(bukets[count].pop(0))
        else: count+=1
    for i in range(len(new_list)): list[i] = new_list[i]

def radix_sort(list):
    max_num = max(list)
    exp = 1
    while max_num // exp > 0:
        counting_sort(list, exp)
        exp *= 10

nums = [170, 45, 75, 90, 802, 24, 2, 66]
print(nums)
radix_sort(nums)
print(nums)
