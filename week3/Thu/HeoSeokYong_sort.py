sik = input()
sik_mp = [list(map(int, i.split('+'))) for i in sik.split('-')]

answer = sum(sik_mp.pop(0))

for s in sik_mp:
  answer -= sum(s)

print(answer)

# 1 line code
# print(eval('-'.join([str(eval("+".join([str(int(j)) for j in i.split('+')]))) for i in input().split('-')])))
