import random

# List of possible moves
moves = ['rock', 'paper', 'scissors']

def get_computer_choice():
    """Randomly selects a move for the computer."""
    return random.choice(moves)

def get_human_choice():
    """Prompts the user to input their move."""
    choice = input("Enter your move (rock, paper, or scissors): ").lower()
    while choice not in moves:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        choice = input("Enter your move (rock, paper, or scissors): ").lower()
    return choice

def determine_winner(human, computer):
    """Determines the winner based on the choices of human and computer."""
    if human == computer:
        return "It's a tie!"
    elif (human == 'rock' and computer == 'scissors') or \
         (human == 'scissors' and computer == 'paper') or \
         (human == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Main function to play the game."""
    play_again = 'yes'
    while play_again.lower() == 'yes':
        human_choice = get_human_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {human_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(human_choice, computer_choice)
        print(result)
        
        play_again = input("\nDo you want to play again? (yes or no): ")

# Start the game
if __name__ == "__main__":
    play_game()