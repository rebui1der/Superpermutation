import itertools as it

def arr_range(n: int) -> list:
    arr = []
    div = n
    end = 0
    for k in range(1, size):
        div //= size - k + 1
        for j in range(size - k):
            end += div
        arr += [end]
    arr += [n]
    return arr

def num_in_range(arr: list, number: int) -> int:
    for i, val in enumerate(arr):
        if number < val:
            return i + 1

size = 9

letters = tuple(chr(i) for i in range(65, 65 + size))
print(f'letters = {letters}')
perm_dict = {''.join(val) : i for i, val in enumerate(it.permutations(letters))}
perm_tuple = tuple(perm_dict.keys())
n = len(perm_tuple)

result_str = perm_tuple[0]
arr = arr_range(n)
i = 0
temp_str = ''
for _ in range(n // 2 - 1):
    k = num_in_range(arr, i)
    val = perm_tuple[i]
    i = perm_dict[val[k:] + val[k-1::-1]]
    temp_str += val[k-1::-1]
    if len(temp_str) > 4000:
        result_str += temp_str
        temp_str = ''
result_str += temp_str
del perm_dict
del perm_tuple

result_str += result_str[-2::-1]
print(f'len = {len(result_str)}')
print(result_str)
