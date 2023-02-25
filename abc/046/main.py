

def main():
    A, B, C = list(map(int,input().split()))
    judge = False

    for i in range(1,B+1):
        if A * i % B == C:
            judge =True

    if (judge):
        print("yes")


if __name__ == "__main__":
    main()

