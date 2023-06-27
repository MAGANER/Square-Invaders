import terminal_main
import graphical_main
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "classic":
        terminal_main.run_game()
    else:
        graphical_main.run_game()
