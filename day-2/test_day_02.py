from day_2 import parse_game, Subset


def test_parse_game():
    game = parse_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert game.id == 1

    assert game.subsets[0] == Subset(red=4, green=0, blue=3)
    assert game.subsets[1] == Subset(red=1, green=2, blue=6)
    assert game.subsets[2] == Subset(red=0, green=2, blue=0)

    assert game.max_subset() == Subset(red=4, green=2, blue=6)
