

def main():
    input_list = list(map(int,input().split()))
    N = input_list[0]
    A = input_list[1]
    B = input_list[2]
    
    sum_tmp = 0

    for i in range(1,N+1):
        sum_N_int_list =  sum(list(map(int,list(str(i)))))
        if  A<= sum_N_int_list <=B:
            sum_tmp += i
    
    print(sum_tmp)

if __name__=='__main__':
    main()