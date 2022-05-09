n = int(input())

strings = []
for _ in range(n):
    strings.append(input())

num_dict = dict()

# 길이가 같을때?
# 각 알파벳의 자리수에 따라 정렬 후 9~0까지 값 할당하는 방식

for string in strings:
    for i in range(len(string)):
        l = len(string) - i
        if string[i] not in num_dict:
            num_dict[string[i]] = 10**(l-1)
        else:
            num_dict[string[i]] += 10**(l-1)

num_dict = sorted(num_dict.items(), key=lambda x: -x[1])

max_ = 9
answer = 0
for v in num_dict:
    answer += max_*(v[1])
    max_ -=1
print(answer)

