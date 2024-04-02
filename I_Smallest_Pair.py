import sys
T = int(input())
for i in range(T):
    n = int(input())
    my_str = input()
    my_list = []
    numbers = list(map(int,my_str.split()))
    for val in numbers:
        my_list.append(val)
    
    my_min = sys.maxsize
    for i in range(n-1):
        for j in range(i+1,n):
            result = my_list[i]+my_list[j]+(j-i)
            if result<my_min:
                my_min = result
    print(my_min)

    

