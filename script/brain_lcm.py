#!/usr/bin/env python3

from game import lcm  # Убери "games." перед game
from engine import play_game  # Убери "games."

def main():
    play_game(lcm)

if __name__ == "__main__":
    main()

