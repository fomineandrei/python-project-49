#!/usr/bin/env python3


from brain_games.games.brain_progression_logic import PROG, question_check_prog
from brain_games.games.engine_bg import game_bg


def main():
    game_bg(question_check_prog(), PROG)


if __name__ == '__main__':
    main()
