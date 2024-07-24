import random

def play_game():
    choices = ["paper", "scissors"]
    
    # Let the computer randomly choose
    computer_choice = random.choice(choices)
    
    # Get user's choice
    user_choice = input("Enter your choice (paper/scissors): ").lower()
    
    # Validate user's choice
    while user_choice not in choices:
        print("Invalid choice! Please enter either 'paper' or 'scissors'.")
        user_choice = input("Enter your choice (paper/scissors): ").lower()
    
    # Print choices
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "paper" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        winner = "Scissors" if computer_choice == "scissors" else "Paper"
        print(f"{winner} cuts Paper! Computer wins!")
    else:
        winner = "Scissors" if user_choice == "scissors" else "Paper"
        print(f"{winner} cuts Paper! You win!")

# Play the game
play_game()
