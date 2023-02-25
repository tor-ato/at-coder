def main():
    N = int(input())

    divisor   = 10 ** 9 + 7

    power = 1

    
    for i in range(1,N+1):

        power = power * i % divisor

    ans = power % divisor

    print(ans)



    



if __name__ == "__main__":
    main()