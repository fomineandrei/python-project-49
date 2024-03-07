#!/usr/bin/env python3


from brain_games.engine_bg import game_check
from brain_games.games.brain_calc_logic import MODULE, RULES, question_check


def main():
    game_check(MODULE, [RULES, question_check])


if __name__ == '__main__':
    main()
