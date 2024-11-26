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
                hints_list_me = ["Exploring worlds and battling foes from the helm of a stealthy spaceship.","A story where choices ripple across a galaxy, shaping destinies and alliances.","A saga where diplomacy, loyalty, and sacrifice determine the fate of the universe."]
                hint_me = random.choice(hints_list_me)
                print(f"Here's a tip about the universe the word is from: {hint_me}")

            elif secret in doctor_who:
                hints_list_dw = ["An ancient ship that’s bigger on the inside.","Adventures spanning time, space, and everything in between.","Enemies that shout 'Exterminate!' and never stop."]
                hint_dw = random.choice(hints_list_dw)
                print(f"Here's a tip about the universe the word is from: {hint_dw}")
                
            elif secret in critical_role:
                hints_list_cr = ["A game where imagination is your greatest weapon.","A party of misfits seeking treasure, glory, and sometimes survival.","Spells, swords, and subterfuge define the adventurers’ path."]
                hint_cr = random.choice(hints_list_cr)
                print(f"Here's a tip about the universe the word is from: {hint_cr}")

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

    


    

    
