def main():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())

    input_coins = [A,B,C]

    three_coins  = [500,100,50]
    

    len_input_coins   = len(input_coins)
    # print(len_input_coins)

    range_input_coins = range(len_input_coins)
    range_list = list(range_input_coins)
    # print(range_input_coins)
    # print(range_list)

    counter = 0

    sum_coin  = 0

    

    for i in range(A+1):
        # print(f"i={i}")
        for j in range(B+1):
            # print(f" j={j}")
            for l in range(C+1):
                # print(f"  l={l}")
                # print(f"  A:{i} B:{j} C:{l}")
                # print(f"{500*i}, {100*j}, {50*l}")
                # print(500*i+100*j+50*l)
                
                sum_coin = 500*i+100*j+50*l

                # print(f"合計:{500*input_coins[i]+100*input_coins[j]+50*input_coins[l]}")
                
                # sum_coin = 500*input_coins[i]+100*input_coins[j]+50*input_coins[l]

                if sum_coin == X:
                    counter += 1

    print(counter)

    # print(A)
    # print(B)
    # print(C)
    # print(X)
    # print(input_coins)






if __name__ == '__main__':
    main()