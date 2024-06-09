""" from main_menu import MainMenu """
import time, sys
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
def print_slower(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.20)
""" def main():
    main_menu = MainMenu()
    main_menu.display_menu()

if __name__ == "__main__":
    main() """