#!/usr/bin/env python3


from brain_games.engine_bg import game_launch
from brain_games.games import brain_gcd_logic


def main():
    game_launch(brain_gcd_logic)


if __name__ == '__main__':
    main()
