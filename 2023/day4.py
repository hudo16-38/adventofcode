from dataclasses import dataclass
from collections import deque

@dataclass
class Card:
    id: int
    my_numbers: set[int]
    winning_numbers: set[int]

    def count_winning_cards(self) -> int:
        common =  self.my_numbers & self.winning_numbers
        return len(common)
    
    def worth(self) -> int:
        n = self.count_winning_cards()
        if n == 0:
            return 0
        return 2**(n-1)
    
    def get_copies(self):
        n = self.count_winning_cards()
        yield from range(self.id+1, self.id+1+n)
    
def parse_line(line: str) -> Card:
    info, nums = line.split(": ")
    _, id = info.split()
    id = int(id)

    my_nums, winning = nums.split(" | ")
    my_nums = set(map(int, my_nums.strip().split()))
    winning = set(map(int, winning.strip().split()))

    return Card(id, my_nums, winning)

def parse_input(file_name: str) -> dict[int, Card]:
    with open(file_name, "r") as file:
        res = {}
        for line in file:
            card = parse_line(line.strip())
            res[card.id] = card
    return res

def worth_sum(cards: dict[int, Card]) -> int:
    return sum(card.worth() for card in cards.values())

def count_cards(cards: dict[int, Card]) -> int:
    q = deque(cards.values())
    count = 0

    while q:
        card = q.popleft()
        count += 1

        for copy in card.get_copies():
            q.append(cards[copy])
    return count


if __name__ == "__main__":
    FILE_NAME = "inputs/day4.txt"
    cards = parse_input(FILE_NAME)

    print(worth_sum(cards))
    print(count_cards(cards))



    