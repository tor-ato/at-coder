def main():

    N ,K = list(map(int,input().split()))
    S = input()

    S_list = list(S)
    count_o = 0

    for i in range(N):

        if S[i] == "o":
            count_o += 1

        if(K < count_o):
            S_list[i] = S_list[i].replace('o','x')
            
    print("".join(S_list))
    

if __name__ == "__main__":
    main()