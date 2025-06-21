def game_intro():
    print("--"*27)
    print(" "*16+"Welcome to the game!")
    print("This is a simple text-based rock paper scissors game.")
    print(" " * 9 + "You will play against the computer.")
    print("--"*27)
    
    
game_intro()
def game_rules():
    print("The rules are simple:")
    print("1. You will choose rock, paper, or scissors.")
    print("2. The computer will randomly choose one of the three options.")
    print("3. Rock beats scissors, scissors beats paper, and paper beats rock.")
    print("4. If both you and the computer choose the same option, it's a tie.")
    print("5. The game will continue until you decide to stop playing.")
game_rules()
def play_game():
    import random
    options =["rock", "paper", "scissors"] 
    while True:
        user_choice =input("Choose rock, paper, or scissors (or type 'exit' to quit): ").lower()
        if user_choice == 'exit':
            print("Thanks for playing! Goodbye!")
            break
        if user_choice not in options:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")     
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")      
        
play_game()