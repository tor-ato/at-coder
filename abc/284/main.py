T = int(input())

N = []
A = []

for i in range(T):
    N.append(int(input()))
    A.append(list(map(int,input().split())))

ans_list = []

for i in A:
    counter = 0
    for j in i:
        if j % 2 == 1:
            # print(j)
            counter += 1
            # print(f"counter : {counter}")
    ans_list.append(counter)

print(*ans_list , sep='\n')

