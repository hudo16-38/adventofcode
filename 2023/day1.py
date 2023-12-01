number_map = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
    }
    

def find_numbers(line: str, replace_words: bool=False) -> str:
    replacements = [("one", "o1e"),
                    ("two", "t2o"),
                    ("three", "t3e"),
                    ("four", "f4r"),
                    ("five", "f5e"),
                    ("six", "s6x"),
                    ("seven", "s7n"),
                    ("eight", "e8"),
                    ("nine", "n9e")
                    ]
    
                    
    if replace_words:
        for word, replacement in replacements:
            line = line.replace(word, replacement)
        
    res = ""
    for char in line:
        if char.isnumeric():
            res += char
    return res

def compute_sum(file_name: str, replace_words: bool=False) -> int:
    res = 0
    with open(file_name, "r") as file:
        for line in file:
            numbers = find_numbers(line, replace_words)
            number = numbers[0]+numbers[-1]
            res += int(number)
    return res

if __name__ == "__main__":
    FIRST_FILE = "first_part.txt"
    SECOND_FILE = "second_part.txt"
    
    print(compute_sum(FIRST_FILE))
    print(compute_sum("test.txt", True))
    print(compute_sum(SECOND_FILE, True))
