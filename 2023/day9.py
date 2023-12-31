def check(lst: list[int]) -> bool:
    return all(x == 0 for x in lst)

def make_differences(lst: list[int], reverse: bool=False) -> list[int]:
    res = []
    n = len(lst)

    if not reverse:
        for i in range(n-1):
            res.append(lst[i+1] - lst[i])
    else:
        for i in range(1, n):
            res.append(lst[i] - lst[i-1])
    return res

def compute_from_history(seq: tuple[int], reverse: bool=False) -> int:
    if check(seq):
        return 0
    diffs = make_differences(seq, reverse)
    
    if reverse:
        return seq[0] - compute_from_history(diffs, reverse)

    return seq[-1] + compute_from_history(diffs, reverse)


def load_histories(file_name: str) -> tuple[tuple[int]]:
    with open(file_name, "r") as file:
        lines = file.read().split("\n")
        return tuple(tuple(map(int, line.split())) for line in lines)
    
def sum_histories(histories: tuple[tuple[int]], reverse: bool=False) -> int:
    return sum(compute_from_history(h, reverse) for h in histories)


    
if __name__ == "__main__":
    histories = load_histories("inputs/day9.test.txt")
    #print(compute_from_history(histories[-1], True))
    print(sum_histories(histories))
    print(sum_histories(histories, True))

    histories = load_histories("inputs/day9.txt")
    print(sum_histories(histories))
    print(sum_histories(histories, True))

