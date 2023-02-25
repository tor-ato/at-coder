def main():
    a, b = map(int, input().split(' '))
    parity_unchecked = a * b % 2

    # print(parity_unchecked)

    if parity_unchecked == 1:
        print("Odd")
    else:
        print("Even")

if __name__ == '__main__':
    main()


