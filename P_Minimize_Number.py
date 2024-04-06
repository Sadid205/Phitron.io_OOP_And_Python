N = int(input())
S = list(map(int,input().split()))

cnt = 0

l = len(S)

list_len = 0

i = 0
while True:
    if S[i]%2==0:
        S[i] = S[i]//2
        list_len = list_len+1
        i=i+1
        if list_len == N:
            cnt = cnt+1
            i = 0
            list_len = 0
    else:
        break
print(cnt)
