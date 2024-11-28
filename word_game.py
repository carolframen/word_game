import random

#List of words

    # Mass Effect
three_me = ["EDI"]
four_me = ["EDEN","GETH","WREX"]
five_me = ["LIARA","THANE","JAVIK","ASARI","DRELL","HANAR","VOLUS","ELCOR","EARTH","OMEGA","FEROS","AEGIS","CODEX"]
six_me = ["GARRUS", "KAIDAN", "ASHLEY", "MORDIN","LEGION", "TURIAN", "KROGAN", "ILLIUM", "PRAGIA", "REAPER", "RELAYS", "GALAXY"]
seven_me = ["SHEPARD","MIRANDA","REAPERS","QUARIAN","THESSIA","PALAVEN","RANNOCH","CITADEL","HORIZON","VIRMIRE","NOVERIA","BIOTICS","SPECTRE","COUNCIL","ECLIPSE","PARAGON","REFUGEE","MEDIGEL"]
eight_me = ["ILLUSIVE","CERBERUS","SALARIAN","PROTHEAN","TUCHANKA","HAESTROM","NORMANDY","ALLIANCE","TERMINUS","RENEGADE","CRUCIBLE","CATALYST","SCANNING","OMNITOOL"]
nine_me = ["BATARIANS","GENOPHAGE","SOVEREIGN","HARBINGER","LEVIATHAN","SYNTHESIS","TALIZORAH","ANDROMEDA"]

mass_effect = three_me + four_me + five_me + six_me + seven_me + eight_me + nine_me #Joining them all so the hint system can work

    #Doctor Who
three_dw = ["AMY"]
four_dw = ["ROSE","RORY","JACK","UNIT"]
five_dw = ["SONIC","SKARO","DONNA","RIVER","CLARA"]
six_dw = ["TARDIS", "DOCTOR", "DALEKS", "MARTHA", "JUDOON", "ZYGONS", "MASTER","VORTEX"]
seven_dw = doctor_who = ["PARADOX","BADWOLF","TIMEWAR","WEEPING"]
eight_dw = ["CYBERMEN","TIMELINE","TIMEWARP"]
nine_dw = ["GALLIFREY","COMPANION","PANDORICA","CHAMELEON","TORCHWOOD"]

doctor_who = three_dw + four_dw + five_dw + six_dw + seven_dw + eight_dw + nine_dw #Joining them all so the hint system can work

    #Critical Role
three_cr = ["VAX","VEX","MAP","NPC"]
four_cr = ["MATT","GROG","BEAU","PIKE","ROLE","DICE","BARD","MONK"]
five_cr = ["CALEB","FJORD","YASHA","QUEST","ARMOR","ROGUE"]
six_cr = ["MERCER", "COMBAT", "SPELLS", "TAVERN", "RANGER", "CLERIC", "WIZARD", "IMOGEN", "LAUDNA","JESTER"]
seven_cr = ["MACHINA","ARCADIA","SCANLAN","KEYLETH","DRAGONS","MONSTER","VILLAIN","WEAPONS","WARLOCK","FIGHTER","PALADIN","HEALING"]
eight_cr = ["EXANDRIA","TALDOREI","TIBERIUS","CADUCEUS","CAMPAIGN","CRITICAL","DUNGEONS","ROLEPLAY","SORCERER"]
nine_cr = ["ENCOUNTER"]

critical_role = three_cr + four_cr + five_cr + six_cr + seven_cr + eight_cr + nine_cr #Joining them all so the hint system can work

#Put all lists together so the secret variable can pick one of them
word_list = mass_effect+doctor_who+critical_role




#Set up yellow and green
def get_yellow_and_green (secret, guess, word_length):
    green = 0

    green_letters = []
    yellow_letters = []

    #Check for yellow: correct digit, wrong place
    for i in range(word_length):
        if guess[i] != secret[i] and guess[i] in secret:
            yellow_letters.append(guess[i])
            
        else:
            yellow_letters.append("_")

    #Check for green: correct digit, correct place
    for i in range(word_length):
        if guess[i] == secret[i]:
            green_letters.append(guess[i])
            green += 1
        else:
            green_letters.append("_")
    green_string = " ".join(green_letters)
    yellow_string = " ".join(yellow_letters)
    print(f"Green letters: {green_string}. Yellow letters: {yellow_string}.")
    return green

#Set up hints

    #Hint lists
hints_list_me = ["Exploring worlds and battling foes from the helm of a stealthy spaceship.","A story where choices ripple across a galaxy, shaping destinies and alliances.","A saga where diplomacy, loyalty, and sacrifice determine the fate of the universe."]
hints_list_dw = ["An ancient ship that’s bigger on the inside.","Adventures spanning time, space, and everything in between.","Enemies that shout 'Exterminate!' and never stop."]
hints_list_cr = ["A game where imagination is your greatest weapon.","A party of misfits seeking treasure, glory, and sometimes survival.","Spells, swords, and subterfuge define the adventurers’ path."]

def hints(secret):
    if secret in mass_effect:

        if not hints_list_me:
            print("You've seen all available hints.")

        else:        
            hint_me = random.choice(hints_list_me)
            print(f"Here's a hint about the universe the word is from: {hint_me}")
            hints_list_me.remove(hint_me)

    elif secret in doctor_who:
        
        if not hints_list_dw:
            print("You've seen all available hints.")

        else:
            hint_dw = random.choice(hints_list_dw)
            print(f"Here's a hint about the universe the word is from: {hint_dw}")
            hints_list_dw.remove(hint_dw)
                
    elif secret in critical_role:
                
        if not hints_list_cr:
            print("You've seen all available hints.")

        else:
            hint_cr = random.choice(hints_list_cr)
            print(f"Here's a hint about the universe the word is from: {hint_cr}")
            hints_list_cr.remove(hint_cr)

#Set up number of guesses     
guesses = 0

#Set up funtions for the different word length

def game_three_letters():
    while True:
        guess = input("Enter your guess (3-letter word): ").upper()

        #Exit the game
        if guess == "EXIT":
            print("You quit the game.")
            break

        #Set up the hints
        elif guess == "HINT":
            hints(secret)
            continue
        
        # Validate the guess
        else:
            #Make sure guesses variable is accessible
            global guesses
            
            if len(guess) != 3 or not guess.isalpha():
                print("Please enter a valid 3-digit word.")
                continue
        
            guesses += 1
        
        # Get the green count
        green = get_yellow_and_green(secret, guess,3)
        
        
        
        # Check if the guess is correct
        if green == 3:
            print(f"Congratulations! You've guessed the word {secret} in {guesses} guesses.")
            break
def game_four_letters():   
    while True:
        
        guess = input("Enter your guess (4-letter word): ").upper()

        #Exit the game
        if guess == "EXIT":
            print("You quit the game.")
            break

        #Set up the hints
        elif guess == "HINT":
            hints(secret)
            continue
        
        # Validate the guess
        else:
            #Make sure guesses variable is accessible
            global guesses
            if len(guess) != 4 or not guess.isalpha():
                print("Please enter a valid 4-digit word.")
                continue
        
            guesses += 1
        
        # Get the green count
        green = get_yellow_and_green(secret, guess,4)
        
        
        
        # Check if the guess is correct
        if green == 4:
            print(f"Congratulations! You've guessed the word {secret} in {guesses} guesses.")
            break
def game_five_letters():
    while True:
    
        guess = input("Enter your guess (5-letter word): ").upper()

        #Exit the game
        if guess == "EXIT":
            print("You quit the game.")
            break

        #Set up the hints
        elif guess == "HINT":
            hints(secret)
            continue
        
        # Validate the guess
        else:
            #Make sure guesses variable is accessible
            global guesses
            if len(guess) != 5 or not guess.isalpha() and guess != "HINT":
                print("Please enter a valid 5-digit word.")
                continue
            
            guesses += 1
        
        # Get the green count
        green = get_yellow_and_green(secret, guess,5)
        
        
        
        # Check if the guess is correct
        if green == 5:
            print(f"Congratulations! You've guessed the word {secret} in {guesses} guesses.")
            break
def game_six_letters():
    while True:
        
        guess = input("Enter your guess (6-letter word): ").upper()

        #Exit the game
        if guess == "EXIT":
            print("You quit the game.")
            break

        #Set up the hints
        elif guess == "HINT":
            hints(secret)
            continue
        
        # Validate the guess
        else:
            #Make sure guesses variable is accessible
            global guesses
            if len(guess) != 6 or not guess.isalpha():
                print("Please enter a valid 6-digit word.")
                continue
            
            guesses += 1
        
        # Get the green count
        green = get_yellow_and_green(secret, guess,6)
        
        
        
        # Check if the guess is correct
        if green == 6:
            print(f"Congratulations! You've guessed the word {secret} in {guesses} guesses.")
            break
def game_seven_letters():
    while True:
        
        guess = input("Enter your guess (7-letter word): ").upper()

        #Exit the game
        if guess == "EXIT":
            print("You quit the game.")
            break

        #Set up the hints
        elif guess == "HINT":
            hints(secret)
            continue
        
        # Validate the guess
        else:
            #Make sure guesses variable is accessible
            global guesses
            if len(guess) != 7 or not guess.isalpha():
                print("Please enter a valid 7-digit word.")
                continue
            
            guesses += 1
        
        # Get the green count
        green = get_yellow_and_green(secret, guess,7)
        
        
        
        # Check if the guess is correct
        if green == 7:
            print(f"Congratulations! You've guessed the word {secret} in {guesses} guesses.")
            break
def game_eight_letters():
    while True:

        guess = input("Enter your guess (8-letter word): ").upper()

        #Exit the game
        if guess == "EXIT":
            print("You quit the game.")
            break

        #Set up the hints
        elif guess == "HINT":
            hints(secret)
            continue
        
        # Validate the guess
        else:
            #Make sure guesses variable is accessible
            global guesses
            if len(guess) != 8 or not guess.isalpha():
                print("Please enter a valid 8-digit word.")
                continue
            
            guesses += 1
        
        # Get the green count
        green = get_yellow_and_green(secret, guess,8)
        
        
        
        # Check if the guess is correct
        if green == 8:
            print(f"Congratulations! You've guessed the word {secret} in {guesses} guesses.")
            break
def game_nine_letters():
    while True:
        
        guess = input("Enter your guess (9-letter word): ").upper()

        #Exit the game
        if guess == "EXIT":
            print("You quit the game.")
            break

        #Set up the hints
        elif guess == "HINT":
            hints(secret)
            continue
        
        # Validate the guess
        else:
            #Make sure guesses variable is accessible
            global guesses
            if len(guess) != 9 or not guess.isalpha():
                print("Please enter a valid 9-digit word.")
                continue
            
            guesses += 1
        
        # Get the green count
        green = get_yellow_and_green(secret, guess,9)
        
        
        # Check if the guess is correct
        if green == 9:
            print(f"Congratulations! You've guessed the word {secret} in {guesses} guesses.")
            break


#Function to play the game
def play_the_game():
    #Choose a random word
    global secret
    secret = random.choice(word_list)

    #Set up the number of characters on the secret word
    length_of_secret = len(secret)
   
    #Initial message
    print("Welcome to the word guessing game!")
    print("I'll generate a word for you to guess. This word is from either the Mass Effect, Doctor Who or Critical Role/D&D universes.")
    print("At anytime type 'hint' to get a hint about the word or 'exit' to quit the game.")
    print("Green means you have a correct letter on the correct place. Yellow means you have a correct letter, but in the wrong place.")
    

    if length_of_secret == 3:
        print("The word has 3 letters.")
        game_three_letters()
    
    elif length_of_secret == 4:
        print("The word has 4 letters.")
        game_four_letters()

    elif length_of_secret == 5:
        print("The word has 5 letters.")
        game_five_letters()

    elif length_of_secret == 6:
        print("The word has 6 letters.")
        game_six_letters()

    elif length_of_secret == 7:
        print("The word has 7 letters.")
        game_seven_letters()
    
    elif length_of_secret == 8:
        print("The word has 8 letters.")
        game_eight_letters()

    elif length_of_secret == 9:
        print("The word has 9 letters.")
        game_nine_letters()

    else:
        print("Invalid option. Please try again.")
        play_the_game()
    
    want_to_play_again = input("Type yes to play again:").upper()

    if want_to_play_again == "YES":
        play_again()
    else:
        print("Have a nice day. Closing the game.")

#Function to reset everything if the player wants to play again
def play_again():
    #Guesses reset
    global guesses
    guesses = 0

    #Hint lists reset
    if secret in mass_effect:
        hints_list_me.append("Exploring worlds and battling foes from the helm of a stealthy spaceship.")
        hints_list_me.append("A story where choices ripple across a galaxy, shaping destinies and alliances.")
        hints_list_me.append("A saga where diplomacy, loyalty, and sacrifice determine the fate of the universe.")
    if secret in doctor_who:
        hints_list_dw.append("An ancient ship that’s bigger on the inside.")
        hints_list_dw.append("Adventures spanning time, space, and everything in between.")
        hints_list_dw.append("Enemies that shout 'Exterminate!' and never stop.")
    if secret in critical_role:
        hints_list_cr.append("A game where imagination is your greatest weapon.")
        hints_list_cr.append("A party of misfits seeking treasure, glory, and sometimes survival.")
        hints_list_cr.append("Spells, swords, and subterfuge define the adventurers’ path.")
    
    play_the_game()


        

# Start the game
play_the_game()

    


    

    
