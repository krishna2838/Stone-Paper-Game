import random

def get_computer_choice():
    return random.choice(["stone", "paper", "scissors"])

def get_user_choice():
    while True:
        choice = input("Enter stone, paper, or scissors: ").lower()
        if choice in ["stone", "paper", "scissors"]:
            return choice
        else:
            print("Invalid input. Please try again.")

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Stone-Paper-Scissors Game!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)
        print(result)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Run the game
if __name__ == "__main__":
    play_game()