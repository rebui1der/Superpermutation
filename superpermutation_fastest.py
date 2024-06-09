import itertools as it

size = 9
letters = [chr(i) for i in range(65, 65 + size)]
print(f'letters = {letters}')

permutations_dict = {''.join(val) : i for i, val in enumerate(it.permutations(letters))}
permutations_list = list(permutations_dict)
n = len(permutations_list)

result_list = []
div = n
end = 0
for k in range(1, size):
    div //= size - k + 1
    for j in range(size - k):
        begin = end
        end += div
        for i in range(begin, end):
            temp_str = permutations_list[i][k:] + permutations_list[i][k-1::-1]
            result_list += [(permutations_dict[temp_str], permutations_list[i][k-1::-1])]

i = 0
result_str = permutations_list[0]
for _ in range(n - 1):    
    result_str += result_list[i][1]
    i = result_list[i][0]

print(f'len = {len(result_str)}')
print(result_str)