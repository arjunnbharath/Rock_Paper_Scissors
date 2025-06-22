def game_intro():
    print("--"*27)
    print(" "*16+"Welcome to the game!")
    print("This is a simple text-based rock paper scissors game.")
    print(" " * 9 + "You will play against the computer.")
    print("--"*27)
    
    
game_intro()

def play_game():
    import random
    options =["rock","paper","scissors"]  
    while True:
        user = input("select rock, paper or scissor (type ""exit"" to quit) : ").lower()
        if user == 'exit':
            print ("Thank q for playing")
            break
        if user not in options :
            print("")
            print("Invalid")
            continue
        computer =random.choice(options)
        print("Machine choose -- ", computer)
        if user == computer :
            print("it's a tie !!!!")
        elif (user == "rock" and computer =="scissors") or (user == "scissors" and computer =="paper") or (user == "paper" and computer =="rock") :
            print("!!! YOU WON !!!")
        else :
            print("you loose")

play_game()
#git status       # 1. Check what has changed (new, modified, deleted files)
#git add .        # 2. Stage all changes (you can also use 'git add <filename>')
#git commit -m "Your commit message"   # 3. Commit staged changes with a message
#git push         # 4. Push the committed changes to the remote repository
