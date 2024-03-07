#!/usr/bin/env python3


from brain_games.engine_bg import game_check
from brain_games.games.brain_progression_logic import RULES, question_check
from brain_games.games.brain_progression_logic import MODULE


def main():
    game_check(MODULE, [RULES, question_check])


if __name__ == '__main__':
    main()
