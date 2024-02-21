#!/usr/bin/env python3


from brain_games.games.brain_prime_logic import PRIM, question_check_prim
from brain_games.games.engine_bg import game_bg


def main():
    game_bg(question_check_prim(), PRIM)


if __name__ == '__main__':
    main()
