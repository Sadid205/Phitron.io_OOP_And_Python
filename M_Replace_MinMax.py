import sys
n  = int(input())
S  = list(map(int,input().split()))

int_min = sys.maxsize
int_max = -sys.maxsize-1

i = 0
j = len(S)-1

while i<j:
    if S[i]>S[j] and S[i]>int_max:
        int_max = S[i]
    if S[i]<S[j] and S[i]<int_min:
        int_min = S[i]
    if S[j]>S[i] and S[j]>int_max:
        int_max = S[j]
    if S[j]<S[i] and S[j]<int_min:
        int_min = S[j]
    i = i+1
    j = j-1

max_index = S.index(int_max)
min_index = S.index(int_min)
S[max_index] = int_min
S[min_index] = int_max
for i in  S:
    print(i,end=" ")


