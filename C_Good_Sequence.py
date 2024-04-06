N = int(input())
A = list(map(int,input().split()))

freq = {}

for value in A:
    if value in freq:
        freq[value]+=1
    else:
        freq[value] = 1

remove_element = 0

for key,value in freq.items():
    if key>value:
        remove_element = remove_element+value
    if key<value:
        remove_element = remove_element+(value-key)
    
print(remove_element)