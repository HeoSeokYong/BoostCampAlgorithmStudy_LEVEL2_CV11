a = input().split('-')
data = []
for i in a:
    data.append('+'.join([str(int(k)) for k in i.split('+')]))

answer = eval(data[0])
for i in data[1:]:
    answer -= eval(i)
    
print(answer)