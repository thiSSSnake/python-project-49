#!/usr/bin/env python3
from brain_games.games import engine
from brain_games.games import game_calc


def game():
    engine.start_game(game_calc)


if __name__ == '__game__':

    game()