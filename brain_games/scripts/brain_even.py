#!/usr/bin/env python3


from brain_games.games.brain_even_logic import EVEN, question_check_even
from brain_games.games.engine_bg import game_bg


def main():
    game_bg(question_check_even(), EVEN)


if __name__ == '__main__':
    main()
