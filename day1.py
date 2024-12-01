def read_input(file_name:str):
    with open(file_name) as f:
        entries = f.readlines()
    entries = [[int(n) for n in e.split()] for e in entries]
    return entries
    
input= read_input("day1input.txt")

#Part 1
list_one = sorted([l[0] for l in input])
list_two = sorted([l[1] for l in input])
compared_lists = list(zip(list_one,list_two))
total = sum(abs(l[1]-l[0]) for l in compared_lists)

print(f"Part 1 Answer: {total}")


#Part 2
from collections import Counter
list_two_counts_dict =Counter(list_two)
total = sum(l*list_two_counts_dict.get(l,0) for l in list_one)

print(f"Part 2 Answer: {total}")


