from dataclasses import dataclass, field
from typing import List


@dataclass()
class Subset:
    red: int = 0
    green: int = 0
    blue: int = 0

    def power(self):
        return self.red * self.green * self.blue


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

    total_power = sum(game.max_subset().power() for game in games)

    print(total_power)


if __name__ == "__main__":
    main()
