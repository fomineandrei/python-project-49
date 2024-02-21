#!/usr/bin/env python3


from brain_games.games.engine_bg import game_bg
from brain_games.games.brain_gcd_logic import GCD, question_check_gcd


def main():
    game_bg(question_check_gcd(), GCD)


if __name__ == '__main__':
    main()
