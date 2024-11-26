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
    #Lists of words
    mass_effect = ["GARRUS", "KAIDAN", "ASHLEY", "MORDIN","LEGION", "TURIAN", "KROGAN", "ILLIUM", "PRAGIA", "REAPER", "RELAYS", "GALAXY"]
    doctor_who = ["TARDIS", "DOCTOR", "DALEKS", "MARTHA", "JUDOON", "ZYGONS", "MASTER","VORTEX"]
    critical_role = [ "MERCER", "COMBAT", "SPELLS", "TAVERN", "RANGER", "CLERIC", "WIZARD", "IMOGEN", "LAUDNA","JESTER"]
    
    #Put all lists together
    word_list = mass_effect+doctor_who+critical_role
    
    #Choose a random word
    secret = random.choice(word_list)

    #Initial message
    print("Welcome to the word guessing game!")
    print("I have generated a 6 letter word for you to guess it. This word is from either the Mass Effect, Doctor Who or Critical Role/D&D universes.")
    print("At anytime type 'hint' to get a hint about the word or 'exit' to quit the game.")

    guesses = 0
   
    while True:
        guess = input("Enter your guess (6-digit word): ").upper()

        #Exit the game
        if guess == "EXIT":
            print("You quit the game.")
            break

        #Set up the hints
        if guess == "HINT":
            if secret in mass_effect:
                print("The word is from Mass Effect.")
            elif secret in doctor_who:
                print("The word is from Doctor Who.")
            elif secret in critical_role:
                print("The word is from Critical Role or D&D.")
                continue
        
        # Validate the guess
        if len(guess) != 6 or not guess.isalpha():
            print("Please enter a valid 6-digit word.")
            continue
        
        guesses += 1
        
        # Get the yellow and green count
        green, yellow = get_yellow_and_green(secret, guess)
        
        print(f"Green: {green}, Yellow: {yellow}")
        
        # Check if the guess is correct
        if green == 6:
            print(f"Congratulations! You've guessed the number {secret} in {guesses} guesses.")
            break
    
    play_again = input("Type yes to play again:").upper()

    if play_again == "YES":
        play_the_game()
    else:
        print("Invalid reply. Closing the game.")
        
        

# Start the game
play_the_game()

    


    

    
