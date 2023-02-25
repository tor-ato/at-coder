def main():
    N = int(input())
    A = list(map(int,input().split()))


    W_flag = 0

    counter = 0


    while W_flag == 0:
        counter += 1
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[i] = A[i] / 2
            else:
                W_flag = 1
        
    print(counter -1)


    

if __name__ == '__main__':
    main()