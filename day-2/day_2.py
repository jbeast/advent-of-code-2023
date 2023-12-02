from dataclasses import dataclass, field
from typing import List


@dataclass()
class Subset:
    red: int = 0
    green: int = 0
    blue: int = 0


@dataclass()
class Game:
    id: int
    subsets: List[Subset] = field(default_factory=list)

    def max_subset(self):
        max_red = max(subset.red for subset in self.subsets)
        max_green = max(subset.green for subset in self.subsets)
        max_blue = max(subset.blue for subset in self.subsets)

        return Subset(red=max_red, green=max_green, blue=max_blue)


def parse_subset(subset: str) -> Subset:
    colours = {
        "red": 0,
        "blue": 0,
        "green": 0,
    }

    for number_colour in subset.split(","):
        number, colour = number_colour.strip().split(" ")
        if colour in colours:
            colours[colour] = int(number)

    return Subset(**colours)


def parse_game(input: str) -> Game:
    game, subsets = input.split(":")
    game_id = int(game.replace("Game ", ""))

    subsets = [parse_subset(subset) for subset in subsets.split(";")]

    return Game(id=game_id, subsets=subsets)


def main():
    with open("./day-2/input.txt", "r") as file:
        games = [parse_game(line) for line in file]

    base_subset = Subset(red=12, green=13, blue=14)
    game_ids = []

    for game in games:
        max_subset = game.max_subset()

        if max_subset.red <= 12 and max_subset.green <= 13 and max_subset.blue <= 14:
            game_ids.append(game.id)

    print(sum(game_ids))


if __name__ == "__main__":
    main()
