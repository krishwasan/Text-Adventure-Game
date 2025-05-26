def start_game():
    print("Welcome to the Adventure!")
    print("You wake up in a dark room with two doors.")
    first_choice()

def first_choice():
    print("\nDo you:")
    print("1) Open the left door")
    print("2) Open the right door")
    choice = input("> ")

    if choice == '1':
        left_room()
    elif choice == '2':
        right_room()
    else:
        print("Invalid choice, try again.")
        first_choice()

def left_room():
    print("\nYou enter a library filled with dusty books.")
    print("There is a shiny key on the table.")
    print("Do you:")
    print("1) Take the key")
    print("2) Leave the key and move forward")
    choice = input("> ")

    if choice == '1':
        print("You took the key and move forward.")
        treasure_room(has_key=True)
    elif choice == '2':
        print("You leave the key and move forward.")
        treasure_room(has_key=False)
    else:
        print("Invalid choice, try again.")
        left_room()

def right_room():
    print("\nYou enter a room with a sleeping dragon!")
    print("Do you:")
    print("1) Try to sneak past the dragon")
    print("2) Go back to the first room")
    choice = input("> ")

    if choice == '1':
        print("The dragon wakes up and you run away!")
        start_game()
    elif choice == '2':
        start_game()
    else:
        print("Invalid choice, try again.")
        right_room()

def treasure_room(has_key):
    print("\nYou find a locked treasure chest.")
    if has_key:
        print("You use the key to open the chest and find gold! You win!")
    else:
        print("The chest is locked and you have no key. You lose!")
    play_again()

def play_again():
    print("\nDo you want to play again? (yes/no)")
    choice = input("> ").lower()
    if choice == 'yes':
        start_game()
    elif choice == 'no':
        print("Thanks for playing!")
    else:
        print("Please type 'yes' or 'no'.")
        play_again()

if __name__ == "__main__":
    start_game()
