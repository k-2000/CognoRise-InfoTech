import random

# Function to get the user's choice
def get_user_choice():
    while True:
        user_choice = input("Please select rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "win"
    else:
        return "lose"

# Function to display the result of each round
def display_result(user_choice, computer_choice, result):
    print(f"User choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")
    print(f"Result: {result}")

# Function to ask the user if they want to play again
def play_again():
    return input("Do you want to play again? (yes/no): ").lower() == 'yes'

# Main function to control the flow of the game
def main():
    print("Welcome to Rock, Paper, Scissors Game!")
    rounds = int(input("How many rounds do you want to play?: "))
    user_score = 0
    computer_score = 0
    round_number = 1
    
    while round_number <= rounds:
        print(f"\n--- Round {round_number} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)
        
        # Update scores
        if result == 'win':
            user_score += 1
        elif result == 'lose':
            computer_score += 1
        
        round_number += 1
    
    # Display game summary
    print("\n--- Game Summary ---")
    print(f"Total Rounds: {rounds}")
    print(f"User Score: {user_score}")
    print(f"Computer Score: {computer_score}")
    
    # Determine the winner of the game
    if user_score > computer_score:
        print("Congratulations! You win!")
    elif user_score < computer_score:
        print("Better luck next time! Computer wins!")
    else:
        print("It's a tie!")
    
    print("Thanks for playing!")

# Entry point of the program
if __name__ == "__main__":
    main()
