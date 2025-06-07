import random


def dice_roll(choice):
    if choice == "y":
        print(random.randint(1, 6))
    elif choice == "n":
        print('Bye')
    else:
        print('Invalid choice')


def take_choice():
    choice = input('Do you want to roll the dice? (y/n) ')
    return choice.lower()


def game():
    consent = take_choice()
    dice_roll(consent)


if __name__ == "__main__":
    game()