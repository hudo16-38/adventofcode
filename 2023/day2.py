from dataclasses import dataclass

@dataclass
class Game:
    id: int
    games: list[dict[str, int]]


def parse_input(file_name: str) -> list[Game]:
    result = []

    with open(file_name, "r") as file:
        for record in file:
            game, games = record.strip().split(":")
            _, id = game.split()
            id = int(id)
            games = games.strip(" ").split("; ")
            game_list = []
            for game in games:
                g = {}
                colors = game.split(", ")
                for color in colors:
                    count, color_name = color.split()
                    g[color_name] = int(count)
                game_list.append(g)
            result.append(Game(id, game_list))
    return result

def filter_possible_games(games: list[Game], filter: dict) -> list[Game]:
    res = []
    for game in games:
        maxs = {}

        for record in game.games:
            for color in record:
                maxs[color] = max(maxs.get(color, 0), record.get(color))
        possible = True
        for color in maxs:
            if maxs.get(color) > filter.get(color):
                possible = False
        if possible:
            res.append(game)
    return res
           

def sum_ids(possible_games: list[Game]) -> int:
    return sum(game.id for game in possible_games)

def get_minimum_filter(game: Game) -> dict[str, int]:
    mins = {}
    for record in game.games:
        for color in record:
            mins[color] =  max(mins.get(color, 0), record.get(color))
    return mins

def filter_power(filter: dict[str, int]) -> int:
    res = 1
    for color, count in filter.items():
        res *= count
    return res

def sum_powers(games: list[Game]) -> int:
    s = 0
    for game in games:
        min_filter = get_minimum_filter(game)
        power =  filter_power(min_filter)
        s += power
    return s


if __name__ == "__main__":
    FILE_NAME = "inputs/day2.txt"
    games = parse_input(FILE_NAME)

    filter = dict(red=12, green=13, blue=14)
    possible_games = filter_possible_games(games, filter)

    s = sum_ids(possible_games)
    print(f"{s = }")
    p = sum_powers(games)
    print(f"{p = }")

