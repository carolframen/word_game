import random

#Set up yellow and green
def get_yellow_and_green (secret, guess, word_length):
    yellow = 0
    green = 0

    #Check for yellow: correct digit, wrong place
    for i in range(word_length):
        if guess[i] != secret[i] and guess[i] in secret:
            yellow += 1

    #Check for green: correct digit, correct place
    for i in range(word_length):
        if guess[i] == secret[i]:
            green += 1
    return green, yellow

#Set up funtions for the different word lenght

def game_three_letters():
    #Lists of words
    mass_effect = ["EDI"]
    doctor_who = ["AMY"]
    critical_role = ["VAX","VEX","MAP","NPC"]

    #Put all lists together
    word_list = mass_effect+doctor_who+critical_role

    #Choose a random word
    secret = random.choice(word_list)

    guesses = 0
   
    while True:
        guess = input("Enter your guess (3-digit word): ").upper()

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
        if len(guess) != 3 or not guess.isalpha():
            print("Please enter a valid 3-digit word.")
            continue
        
        guesses += 1
        
        # Get the yellow and green count
        green, yellow = get_yellow_and_green(secret, guess,3)
        
        print(f"Green: {green}, Yellow: {yellow}")
        
        # Check if the guess is correct
        if green == 3:
            print(f"Congratulations! You've guessed the number {secret} in {guesses} guesses.")
            break
def game_four_letters():
    #Lists of words
    mass_effect = ["EEEZO","EDEN","GETH","WREX"]
    doctor_who = ["ROSE","RORY","JACK","UNIT"]
    critical_role = ["MATT","GROG","BEAU","PIKE","ROLE","DICE","BARD","MONK"]

    #Put all lists together
    word_list = mass_effect+doctor_who+critical_role

    #Choose a random word
    secret = random.choice(word_list)

    guesses = 0
   
    while True:
        guess = input("Enter your guess (4-digit word): ").upper()

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
        if len(guess) != 4 or not guess.isalpha():
            print("Please enter a valid 4-digit word.")
            continue
        
        guesses += 1
        
        # Get the yellow and green count
        green, yellow = get_yellow_and_green(secret, guess,3)
        
        print(f"Green: {green}, Yellow: {yellow}")
        
        # Check if the guess is correct
        if green == 4:
            print(f"Congratulations! You've guessed the number {secret} in {guesses} guesses.")
            break
def game_five_letters():
    #Lists of words
    mass_effect = ["LIARA","THANE","JAVIK","ASARI","DRELL","HANAR","VOLUS","ELCOR","EARTH","OMEGA","FEROS","AEGIS","CODEX"]
    doctor_who = ["SONIC","SKARO","DONNA","RIVER","CLARA"]
    critical_role = ["CALEB","FJORD","YASHA","QUEST","ARMOR","ROGUE"]

    #Put all lists together
    word_list = mass_effect+doctor_who+critical_role

    #Choose a random word
    secret = random.choice(word_list)

    guesses = 0
   
    while True:
        guess = input("Enter your guess (5-digit word): ").upper()

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
        if len(guess) != 5 or not guess.isalpha():
            print("Please enter a valid 5-digit word.")
            continue
        
        guesses += 1
        
        # Get the yellow and green count
        green, yellow = get_yellow_and_green(secret, guess,3)
        
        print(f"Green: {green}, Yellow: {yellow}")
        
        # Check if the guess is correct
        if green == 5:
            print(f"Congratulations! You've guessed the number {secret} in {guesses} guesses.")
            break
def game_six_letters():
    #Lists of words
    mass_effect = ["GARRUS", "KAIDAN", "ASHLEY", "MORDIN","LEGION", "TURIAN", "KROGAN", "ILLIUM", "PRAGIA", "REAPER", "RELAYS", "GALAXY"]
    doctor_who = ["TARDIS", "DOCTOR", "DALEKS", "MARTHA", "JUDOON", "ZYGONS", "MASTER","VORTEX"]
    critical_role = [ "MERCER", "COMBAT", "SPELLS", "TAVERN", "RANGER", "CLERIC", "WIZARD", "IMOGEN", "LAUDNA","JESTER"]

    #Put all lists together
    word_list = mass_effect+doctor_who+critical_role

    #Choose a random word
    secret = random.choice(word_list)

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
        green, yellow = get_yellow_and_green(secret, guess,6)
        
        print(f"Green: {green}, Yellow: {yellow}")
        
        # Check if the guess is correct
        if green == 6:
            print(f"Congratulations! You've guessed the number {secret} in {guesses} guesses.")
            break
def game_seven_letters():
    #Lists of words
    mass_effect = ["SHEPARD","MIRANDA","REAPERS","QUARIAN","THESSIA","PALAVEN","RANNOCH","CITADEL","HORIZON","VIRMIRE","NOVERIA","BIOTICS","SPECTRE","COUNCIL","ECLIPSE","PARAGON","REFUGEE","MEDIGEL"]
    doctor_who = ["PARADOX","BADWOLF","TIMEWAR","WEEPING"]
    critical_role = ["MACHINA","ARCADIA","SCANLAN","KEYLETH","DRAGONS","MONSTER","VILLAIN","WEAPONS","WARLOCK","FIGHTER","PALADIN","HEALING"]

    #Put all lists together
    word_list = mass_effect+doctor_who+critical_role

    #Choose a random word
    secret = random.choice(word_list)

    guesses = 0
   
    while True:
        guess = input("Enter your guess (7-digit word): ").upper()

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
        if len(guess) != 7 or not guess.isalpha():
            print("Please enter a valid 7-digit word.")
            continue
        
        guesses += 1
        
        # Get the yellow and green count
        green, yellow = get_yellow_and_green(secret, guess,3)
        
        print(f"Green: {green}, Yellow: {yellow}")
        
        # Check if the guess is correct
        if green == 7:
            print(f"Congratulations! You've guessed the number {secret} in {guesses} guesses.")
            break
def game_eight_letters():
    #Lists of words
    mass_effect = ["ILLUSIVE","CERBERUS","SALARIAN","PROTHEAN","TUCHANKA","HAESTROM","NORMANDY","ALLIANCE","TERMINUS","RENEGADE","CRUCIBLE","CATALYST","SCANNING","OMNITOOL"]
    doctor_who = ["CYBERMEN","TIMELINE","TIMEWARP"]
    critical_role = ["EXANDRIA","TALDOREI","TIBERIUS","CADUCEUS","CAMPAIGN","CRITICAL","DUNGEONS","ROLEPLAY","SORCERER"]

    #Put all lists together
    word_list = mass_effect+doctor_who+critical_role

    #Choose a random word
    secret = random.choice(word_list)

    guesses = 0
   
    while True:
        guess = input("Enter your guess (8-digit word): ").upper()

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
        if len(guess) != 8 or not guess.isalpha():
            print("Please enter a valid 8-digit word.")
            continue
        
        guesses += 1
        
        # Get the yellow and green count
        green, yellow = get_yellow_and_green(secret, guess,3)
        
        print(f"Green: {green}, Yellow: {yellow}")
        
        # Check if the guess is correct
        if green == 8:
            print(f"Congratulations! You've guessed the number {secret} in {guesses} guesses.")
            break
def game_nine_letters():
    #Lists of words
    mass_effect = ["BATARIANS","GENOPHAGE","SOVEREIGN","HARBINGER","LEVIATHAN","SYNTHESIS","TALIZORAH","ANDROMEDA"]
    doctor_who = ["GALLIFREY","COMPANION","PANDORICA","CHAMELEON","TORCHWOOD"]
    critical_role = ["ENCOUNTER"]

    #Put all lists together
    word_list = mass_effect+doctor_who+critical_role

    #Choose a random word
    secret = random.choice(word_list)

    guesses = 0
   
    while True:
        guess = input("Enter your guess (9-digit word): ").upper()

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
        if len(guess) != 9 or not guess.isalpha():
            print("Please enter a valid 9-digit word.")
            continue
        
        guesses += 1
        
        # Get the yellow and green count
        green, yellow = get_yellow_and_green(secret, guess,3)
        
        print(f"Green: {green}, Yellow: {yellow}")
        
        # Check if the guess is correct
        if green == 9:
            print(f"Congratulations! You've guessed the number {secret} in {guesses} guesses.")
            break


#Function to play the game
def play_the_game():
   
    #Initial message
    print("Welcome to the word guessing game!")
    print("I'll generate a word for you to guess. This word is from either the Mass Effect, Doctor Who or Critical Role/D&D universes.")
    print("At anytime type 'hint' to get a hint about the word or 'exit' to quit the game.")
    print("Green means you have a correct letter on the correct place. Yellow means you have a correct letter, but in the wrong place.")
    print("Now, first things first, how many letters do you want the word to have?")
    choose_the_word_lenght = int(input("You can choose any number between 3 and 9: "))

    if choose_the_word_lenght == 3:
        game_three_letters()
    
    elif choose_the_word_lenght == 4:
        game_four_letters()

    elif choose_the_word_lenght == 5:
        game_five_letters()

    elif choose_the_word_lenght == 6:
        game_six_letters()

    elif choose_the_word_lenght == 7:
        game_seven_letters()
    
    elif choose_the_word_lenght == 8:
        game_eight_letters()

    elif choose_the_word_lenght == 9:
        game_nine_letters()

    else:
        print("Invalid option. Please try again.")
        play_the_game()
    
    play_again = input("Type yes to play again:").upper()

    if play_again == "YES":
        play_the_game()
    else:
        print("Have a nice day. Closing the game.")
    
        
        

# Start the game
play_the_game()

    


    

    
