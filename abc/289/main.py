def main():
    N, M = map(int, input().split())
    a = list(map(int, input().split()))

    

    ans = []

    flag = 0

    for i in range(1,N+1):
        print(ans)
        if i in int_list_a and flag == 0:
            print(F"don't swap{i}")
            ans.append(i+1)
            ans.append(i)
            flag = 1

        else:
            print(F"swap{i}")
            ans.append([i])
            flag = 0

    print(ans)





if __name__ == '__main__':
    main()