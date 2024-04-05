n = int(input())
S = list(map(int,input().split()))

i = 0
j = len(S)-1
flag = True
while i<j :
    if S[i] != S[j]:
        flag = False
        break
    i = i+1
    j = j-1

if flag == True:
    print("YES")
else:
    print("NO")