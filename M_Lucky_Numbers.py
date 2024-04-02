A,B = input().split()
A = int(A)
B = int(B)

def is_lucky(num):
    while num>0:
        digit = num%10
        if digit !=4 and digit !=7:
            return False
        num//=10
    return True
Lucky_numbers = []
for num in range(A,B+1):
    if is_lucky(num):
        Lucky_numbers.append(num)

if len(Lucky_numbers)==0:
    print(-1)
else:
    for num in Lucky_numbers:
        print(num,end=" ")
