import sys

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "classic":
        import terminal_main
        terminal_main.run_game()
    else:
        import graphical_main
        while True:
            if not graphical_main.run_game():
                break
