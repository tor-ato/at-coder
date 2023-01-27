def main():
    N = int(input())
    a = list(map(int,input().split()))

    # print(N)
    # print(a)

    Alice = 0
    Alice_list =[]
    Bob = 0
    Bob_list = []

    a.sort(reverse=True)
    


    for i in range(N):
        if i % 2 == 0:
            Alice_list.append(a[i])
        else:
            Bob_list.append(a[i])
    

    Alice_Bob_diff = abs(sum(Alice_list)-sum(Bob_list))

    print(Alice_Bob_diff)
    


if __name__ == '__main__':
    main()