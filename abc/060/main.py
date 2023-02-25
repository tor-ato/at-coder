

def main():
    A, B, C = list(map(int,input().split()))
    judge = False

    for i in range(1,B+1):
        if A * i % B == C:
            judge =True

    if (judge):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()

