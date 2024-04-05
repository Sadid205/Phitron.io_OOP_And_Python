S = input().split()
str_reverse = list(map(lambda item:item[::-1],S))
for i in range(len(str_reverse)-1):
    print(str_reverse[i],end=' ')
print(str_reverse[-1])