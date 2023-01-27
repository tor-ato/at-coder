def main():
    
    X = int(input())

    a  = []

    for i in range(X) :
        a.append(int(input()))


    a_set = set(a)



    print(len(a_set))



if __name__ == "__main__":
    main()
    