import os
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "classic":
        if os.name == "nt":
            print("Sorry! Terminal Square Invaders can not be run on Windows! But you can play graphical mode!")
            exit(0) 
        import terminal_main
        terminal_main.run_game()
    else:
        import graphical_main
        while True:
            if not graphical_main.run_game():
                break
