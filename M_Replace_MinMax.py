my_list = []
n = int(input())
arr_string = input()

numbers = list(map(int,arr_string.split()))
for i in numbers:
    my_list.append(i)

i = 0
j = len(my_list)-1

min_val = -2147483648
max_val = 2147483647
while(i<j):
   
    if my_list[i]>min_val:
       min_val = my_list[i]
    if my_list[i]<max_val:
        max_val = my_list[i]

    if my_list[j] > min_val:
        min_val = my_list[j]
    if my_list[j] < max_val:
        max_val = my_list[j]
    i=i+1
    j=j-1

rep_min =  my_list.index(min_val)
rep_max = my_list.index(max_val)
my_list[rep_min] = max_val
my_list[rep_max] = min_val

for value in my_list:
    print(value,end=' ')

