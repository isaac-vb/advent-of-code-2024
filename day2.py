def read_input(file_name: str):
    with open(file_name) as f:
        entries = f.readlines()
    entries = [[int(n) for n in e.split()] for e in entries]
    return entries

input = read_input("day2input.txt")

#Part 1
def check_increasing(report):
    if report[1] > report[0]:
        return True
    return False


def check_valid_report(report):
    for x in range(len(report) - 1):
        if check_increasing(report):
            if report[x] + 1 <= report[x + 1] <= report[x] + 3:
                continue
            return False
        else:
            if report[x] - 1 >= report[x + 1] >= report[x] - 3:
                continue
            return False
    return True

total =0
for i in input:
    if check_valid_report(i) == True:
        total += 1
print(f"Part 1 Answer: {total}")

#Part 2