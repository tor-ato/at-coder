

def main():
    HW  = list(map(int,input().split()))

    H = HW[0]
    W = HW[1]

    HW_list = []

    for i in range(H):
        HW_list.append(list(map(int,input().split())))


    WH_list = []

    for i in range(W):
        if 0 < i:
            print()
        for j in range(H):
            if j != H-1:
                print(HW_list[j][i],end=" ")
            else:
                print(HW_list[j][i],sep="",end="")
            






if __name__ == "__main__":
    main()