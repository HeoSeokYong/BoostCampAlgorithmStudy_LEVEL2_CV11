val = input().split()
val = [int(i) for i in val]

size = 2 ** val[0]
answer = 0
for i in range(val[0]):
    size /= 2
    area = 0
    if size <= val[1]:
        #row in 3, 4
        area += 2
        val[1] -= size
    if size <= val[2]:
        #col in 1, 4
        area += 1
        val[2] -= size
    answer += (size ** 2) * area

print(int(answer))