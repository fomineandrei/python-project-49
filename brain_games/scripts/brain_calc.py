#!/usr/bin/env python3


from brain_games.games.brain_calc_logic import CALC, question_check_calc
from brain_games.games.engine_bg import game_bg


def main():
    game_bg(question_check_calc(), CALC)


if __name__ == '__main__':
    main()
