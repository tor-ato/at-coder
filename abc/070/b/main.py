def main():
    time_list = list(map(int,input().split()))


    dup_time = 0

    A = time_list[0]
    B = time_list[1]
    C = time_list[2]
    D = time_list[3]

    if A <= C <= B <= D:
        dup_time = B - C
    elif A <= C <= D <= B:
        dup_time = D - C
    elif C <= A <= B <= D:
        dup_time = B - A
    elif C <= A <= D <= B:
        dup_time = D - A

    
    else:
        dup_time        

    print(dup_time)



    

    

if __name__ == '__main__':
    main()