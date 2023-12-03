from dataclasses import dataclass

@dataclass
class Symbol:
    symbol: str
    x: int
    y: int

@dataclass
class Number:
    number: int
    x: int
    y: int

    def is_adjacent(self, symbol: Symbol) -> bool:
        n = len(str(self.number))
        x1, y1 = self.x, self.y
        x2, y2 = symbol.x, symbol.y

        dx = x1 - x2
        dy = y1 - y2

        return (-n <= dx <= 1) and (-1 <= dy <= 1)

def parse_input(file_name: str) -> tuple[list[Number] | list[Symbol]]:
    numbers, symbols = [], []
    with open(file_name, "r") as file:
        lines = [line.strip() for line in file]

        for row, line in enumerate(lines):
            number = ""

            for column, char in enumerate(line):
                if char != ".":
                    if char.isnumeric():
                        number += char
                    else:
                        if number != "":
                            numbers.append(Number(int(number), column - len(number), row))
                            number = ""
                        symbols.append(Symbol(char, column, row))
                else:
                    if number != "":
                            numbers.append(Number(int(number), column - len(number), row))
                            number = ""
            if number != "":
                numbers.append(Number(int(number), column - len(number), row))
    return numbers, symbols

def get_adjacent_numbers(numbers: list[Number], symbols: list[Symbol]) -> list[int]:
    res = []
    for number in numbers:
        is_adjacent = False
        for symbol in symbols:
            is_adjacent = number.is_adjacent(symbol)
            if is_adjacent:
                break
        if is_adjacent:
            res.append(number.number)
    return res

def get_gears(numbers: list[Number], symbols: Symbol) -> list[Symbol]:
    res = []
    for symbol in symbols:
        if symbol.symbol != "*":
            continue
        count = 0
        for number in numbers:
            count += number.is_adjacent(symbol)
        if count == 2:
            res.append(symbol)
    return res

def gear_ratio(numbers: list[Number], gear: Symbol) -> int:
    res = 1
    for number in numbers:
        if number.is_adjacent(gear):
            res *= number.number
    return res

def sum_gear_ratios(numbers: list[Number], gears: list[Symbol]) -> int:
    
    return sum(gear_ratio(numbers, gear) for gear in gears)
    


if __name__ == "__main__":
    #FILE_NAME = "inputs/day3.test.txt"
    FILE_NAME = "inputs/day3.txt"
    numbers, symbols = parse_input(FILE_NAME)
    #print(numbers)
    #print()
    #print(symbols)
    adjacent = get_adjacent_numbers(numbers, symbols)
    #print()
    #print(adjacent)
    print(sum(adjacent))
    gears = get_gears(numbers, symbols)
    s = sum_gear_ratios(numbers, gears)
    print(s)

