numbers = input()

convert_list = []

for num in numbers:
    convert_list.append(int(num))

i = 0
j = len(convert_list)-1

is_true = True

while i<j:
    if convert_list[i] == convert_list[j]:
        i = i+1
        j = j-1
    else:
        is_true = False
        break




if is_true==True:
   print(numbers)
   print("YES")
else:
    reverse_str = numbers[::-1]
    integer_str = int(reverse_str)
    print(integer_str)
    print("NO")

    
        