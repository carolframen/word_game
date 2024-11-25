import random

def get_yellow_and_green (secret, guess):
    yellow = 0
    green = 0

    #Check for yellow: correct digit, wrong place
    for i in range(6):
        if guess[i] != secret[i] and guess[i] in secret:
            yellow += 1

    #Check for green: correct digit, correct place
    for i in range(6):
        if guess[i] == secret[i]:
            green += 1
    return green, yellow

def play_the_game():
    #Choose a random word
    word_list = ["GARRUS", "KAIDAN", "ASHLEY", "MORDIN", "LEGION", "TURIAN", "KROGAN", "ILLIUM", "PRAGIA", "REAPER", "RELAYS", "GALAXY", "TARDIS", "DOCTOR", "DALEKS", "MARTHA", "VORTEX", "JUDOON", "ZYGONS", "MASTER", "MERCER", "JESTER", "IMOGEN", "LAUDNA", "COMBAT", "SPELLS", "TAVERN", "RANGER", "CLERIC", "WIZARD"]
    secret = random.choice(word_list)

    print("Welcome to the word guessing game!")
    print("I have generated a 6 letter word for you to guess it. This word is from either the Mass Effect, Doctor Who or Critical Role/D&D universes.")

    guesses = 0
    while True:
        guess = input("Enter your guess (6-digit word): ").upper()
        
        # Validate the guess
        if len(guess) != 6 or not guess.isalpha():
            print("Please enter a valid 6-digit word.")
            continue
        
        guesses += 1
        
        # Get the cows and bulls count
        green, yellow = get_yellow_and_green(secret, guess)
        
        print(f"Green: {green}, Yellow: {yellow}")
        
        # Check if the guess is correct
        if green == 6:
            print(f"Congratulations! You've guessed the number {secret} in {guesses} guesses.")
            break

# Start the game
play_the_game()

    


    

    
