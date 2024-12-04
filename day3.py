import re

def read_input(file_name):
  with open(file_name, 'r') as file:
    file_content = file.read()
  return file_content

#Part 1
def part_one(instructions):
  total = 0
  clean_instructions = [[int(x) for x in re.findall(r"\d+", instruction)]
                        for instruction in re.findall(r"mul[(]\d+,\d+[)]", instructions)]

  for instruction in clean_instructions:
    total += instruction[0] * instruction[1]
  return total

instructions = read_input("day3input.txt")

print(f"Part 1 Answer: {part_one(instructions)}")

#Part 2
def part_two(instructions):
    total = 0
    re1 = r"mul[(]\d+,\d+[)]"
    re2 = r"do[(][)]"
    re3 = r"don't[(][)]"

    cleaned_instructions = re.compile("(%s|%s|%s)" % (re1, re2, re3)).findall(instructions)    
    result = []
    skip = False

    for instruction in cleaned_instructions:
        if instruction == "don't()":
            skip = True 
        elif instruction == "do()":
            skip = False  
            continue  
        if not skip:
            result.append(instruction)
    result = [re.findall(r"\d+", r) for r in result]
    for r in result:
        total += int(r[0]) * int(r[1])
    return total

print(f"Part 2 Answer: {part_two(instructions)}")



