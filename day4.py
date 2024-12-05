def read_input(file_name: str):
    with open(file_name, 'r') as file:
        return file.read().split('\n')


def check_horizontal(word_search: list) -> int:
    count = 0
    for line_pos, line in enumerate(word_search):
        for letter_pos, letter in enumerate(line):
            # Check for "XMAS" (rightward)
            if letter == "X" and letter_pos <= len(line) - 4:
                if (line[letter_pos+1] == "M" and
                    line[letter_pos+2] == "A" and
                    line[letter_pos+3] == "S"):
                    count += 1
            # Check for "SAMX" (leftward reverse)
            if letter == "S" and letter_pos <= len(line) - 4:
                if (line[letter_pos+1] == "A" and
                    line[letter_pos+2] == "M" and
                    line[letter_pos+3] == "X"):
                    count += 1
    return count


def check_vertical(word_search: list) -> int:
    count = 0
    for line_pos, line in enumerate(word_search):
        for letter_pos, letter in enumerate(line):
            # Check for "XMAS" (downward)
            if letter == "X" and line_pos <= len(word_search) - 4:
                if (word_search[line_pos+1][letter_pos] == "M" and
                    word_search[line_pos+2][letter_pos] == "A" and
                    word_search[line_pos+3][letter_pos] == "S"):
                    count += 1
            # Check for "SAMX" (downward reverse)
            if letter == "S" and line_pos <= len(word_search) - 4:
                if (word_search[line_pos+1][letter_pos] == "A" and
                    word_search[line_pos+2][letter_pos] == "M" and
                    word_search[line_pos+3][letter_pos] == "X"):
                    count += 1
    return count


def check_diagonal_up_right(word_search: list) -> int:
    count = 0
    for line_pos, line in enumerate(word_search):
        for letter_pos, letter in enumerate(line):
            # Check for "XMAS" (up-right diagonal)
            if letter == "X" and line_pos >= 3 and letter_pos <= len(line) - 4:
                if (word_search[line_pos-1][letter_pos+1] == "M" and
                    word_search[line_pos-2][letter_pos+2] == "A" and
                    word_search[line_pos-3][letter_pos+3] == "S"):
                    count += 1
            # Check for "SAMX" (up-right diagonal reverse)
            if letter == "S" and line_pos >= 3 and letter_pos <= len(line) - 4:
                if (word_search[line_pos-1][letter_pos+1] == "A" and
                    word_search[line_pos-2][letter_pos+2] == "M" and
                    word_search[line_pos-3][letter_pos+3] == "X"):
                    count += 1
    return count


def check_diagonal_down_right(word_search: list) -> int:
    count = 0
    for line_pos, line in enumerate(word_search):
        for letter_pos, letter in enumerate(line):
            # Check for "XMAS" (down-right diagonal)
            if letter == "X" and line_pos <= len(word_search) - 4 and letter_pos <= len(line) - 4:
                if (word_search[line_pos+1][letter_pos+1] == "M" and
                    word_search[line_pos+2][letter_pos+2] == "A" and
                    word_search[line_pos+3][letter_pos+3] == "S"):
                    count += 1
            # Check for "SAMX" (down-right diagonal reverse)
            if letter == "S" and line_pos <= len(word_search) - 4 and letter_pos <= len(line) - 4:
                if (word_search[line_pos+1][letter_pos+1] == "A" and
                    word_search[line_pos+2][letter_pos+2] == "M" and
                    word_search[line_pos+3][letter_pos+3] == "X"):
                    count += 1
    return count



word_search = read_input("day4input.txt")

horizontal_matches = check_horizontal(word_search)
vertical_matches = check_vertical(word_search)
up_right_diagonal_matches = check_diagonal_up_right(word_search)
down_right_diagonal_matches = check_diagonal_down_right(word_search)

total_matches = (horizontal_matches + vertical_matches +
                    up_right_diagonal_matches + down_right_diagonal_matches)
print(f"Part 1 Answer: {total_matches}")
