S = input()
str_cnt = 0

all_str = []

split_str = ""

count_character = 0

for character in S:
    split_str = split_str + character
    if character == 'R':
        count_character = count_character-1
    else:
        count_character = count_character+1    
    if count_character == 0:
        all_str.append(split_str)
        str_cnt = str_cnt+1
        split_str = ""

print(str_cnt)
for str in all_str:
    print(str)        