A,B = input().split()
S = input()
A = int(A)
B = int(B)

flag = True
if A+B+1 != len(S):
    print('No')
else:
    for i in range(len(S)):
        if(i==A):
            if(S[i]!='-'):
                print('No')
                flag = False
                break
        else:
            if(S[i]=='-'):
                print('No')
                flag = False
                break
    if flag==True:
        print('Yes')
