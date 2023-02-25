S = input()
T = input()

list_S = list(S)
list_T = list(T)

len_S = len(S)
len_T = len(T)

ans = "No"
# print(len_S)
# print(len_T)

if len_S <= len_T:
    ans = "Yes"
    for i in range(len_S):
        # print(list_S[i])
        # print(list_T[i])
        if(list_S[i] != list_T[i]):
            ans = "No"

print(ans)



    
