N, K = list(map(int,input().split()))
winner_list = []

for i in range(N):
    winner_list.append(input())

top_winner_list = winner_list[:K]

sorted_top_winner_list = sorted(top_winner_list)

print( *sorted_top_winner_list ,sep='\n')
