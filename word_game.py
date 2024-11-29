import random
import tkinter as tk

# Colors
dark_blue = "#283044" #backgroung color
light_blue = "#78a1bb" #button background
white = "#ebf5ee"
dark_bronw = "#8b786d"
light_brown = "#bfa89e"

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


#Hint lists
hints_list_me = ["Exploring worlds and battling foes from the helm of a stealthy spaceship.","A story where choices ripple across a galaxy, shaping destinies and alliances.","A saga where diplomacy, loyalty, and sacrifice determine the fate of the universe."]
hints_list_dw = ["An ancient ship that’s bigger on the inside.","Adventures spanning time, space, and everything in between.","Enemies that shout 'Exterminate!' and never stop."]
hints_list_cr = ["A game where imagination is your greatest weapon.","A party of misfits seeking treasure, glory, and sometimes survival.","Spells, swords, and subterfuge define the adventurers’ path."]



#Set up number of guesses     
guesses = 0

#Set up global secret variable
secret = None

# Create the main window
main_window = tk.Tk()



# Functions

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
    feedback_label.config(text=f"Green letters: {green_string}. Yellow letters: {yellow_string}.")
    
    return green

# Quit the game
def quit_window():
    main_window.quit()

# Show the rules page 
def show_rules():
    main_frame.pack_forget()  # Hide the main frame
    rules_frame.pack(padx=20, pady=20)  # Show the rules frame

# Go back to the main frame from the Rules frame
def go_back():
    rules_frame.pack_forget()  # Hide the rules frame
    main_frame.pack(padx=20, pady=20)  # Show the main frame

#Show Congratulations Frame
def show_congratulations():
    # Dynamically update the congratulation label text
    congratulation_label_text.config(
        text=f"Congratulations! You guessed the word {secret} in {guesses} guesses!"
    )
    main_frame.pack_forget()  # Hide the main frame
    game_frame.pack_forget() #Hide the game frame
    congratulation_frame.pack(padx=20, pady=20)  # Show the rules frame   

# Go to the Game Frame
def start_game():
    global secret, guesses, feedback_text, length_of_secret, game_label_word_length

    # Reset game state
    secret = random.choice(word_list)
    length_of_secret = len(secret)
    guesses = 0
    feedback_text = ""
    feedback_label.config(text="")  # Clear feedback
    game_frame.pack(padx=20, pady=20)
    main_frame.pack_forget()
    

    
    # Show how many letters the word has
    game_label_word_length = tk.Label(
        game_frame,
        text=f"The word has {length_of_secret} letters.",
        font=("Cooper Black", 18),
        fg=white,
        bg=dark_blue,
        wraplength=450,
    )
    game_label_word_length.pack(pady=20)

    #This ensures that the enter key can be used to submit the guess
    guess_entry.focus_set()
    
# Submit guess and check it
def submit_guess():
    
        
        global guesses, feedback_text, length_of_secret
        guess = guess_entry.get().upper()  # Get the guess from the entry
        guess_entry.delete(0, tk.END)  # Clear the entry field
        
        # Validate the guess

                    
        if len(guess) != length_of_secret or not guess.isalpha():
            feedback_text = "Please enter a valid word, {} letters long.".format(len(secret))
            
        else:
            guesses += 1
        
            # Get the green count
            green = get_yellow_and_green(secret, guess,length_of_secret)
        
        
        
        # Check if the guess is correct
        if green == length_of_secret:
            show_congratulations()
      
# Play again
def play_again():
    congratulation_frame.pack_forget() #hide congratulation frame
    game_label_word_length.pack_forget()

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
    start_game()

#Return to the main frame from the game frame
def go_to_main_from_game(): 
    game_label_word_length.pack_forget() 
    game_frame.pack_forget() #Hide game frame
    main_frame.pack(padx=20, pady=20) #Show the main frame

#Set up hints
def hints(secret):
    
    if secret in mass_effect:

        if not hints_list_me:
            feedback_label.config(text=f"You've seen all available hints.")

        else:        
            hint_me = random.choice(hints_list_me)
            feedback_label.config(text=f"Here's a hint about the universe the word is from: {hint_me}")
            hints_list_me.remove(hint_me)

    elif secret in doctor_who:
        
        if not hints_list_dw:
            feedback_label.config(text=f"You've seen all available hints.")

        else:
            hint_dw = random.choice(hints_list_dw)
            feedback_label.config(text=f"Here's a hint about the universe the word is from: {hint_dw}")
            hints_list_dw.remove(hint_dw)
                
    elif secret in critical_role:
                
        if not hints_list_cr:
            feedback_label.config(text=f"You've seen all available hints.")

        else:
            hint_cr = random.choice(hints_list_cr)
            feedback_label.config(text=f"Here's a hint about the universe the word is from: {hint_cr}")
            hints_list_cr.remove(hint_cr)

# GUI

#Main Window settings
    # Set the title of the window
main_window.title("Word Game")

    # Set the size of the window
main_window.geometry("500x600")  # Width x Height

    # Disable the window's resizing capability
main_window.resizable(False, False)

    # Change the background color using configure
main_window.configure(bg= dark_blue)

# Main Frame
main_frame = tk.Frame(main_window, bg=dark_blue)

#Main Window Content
    # Title
label = tk.Label(main_frame, text="Welcome to the Word Game", font=("Cooper Black", 24), fg = white, bg = dark_blue)
label.pack(pady=20)  # pady adds some space around the label

    # Buttons

start_game_button = tk.Button(main_frame, text="Start Game", font=("Cooper Black", 14), bg = light_blue, command= start_game)
start_game_button.pack(pady=10)

rules_button = tk.Button(main_frame, text="Rules", font=("Cooper Black", 14), bg = light_blue, command= show_rules)
rules_button.pack(pady=10)

quit_button = tk.Button(main_frame, text="Quit", font=("Cooper Black", 14), bg = light_blue, command = quit_window)
quit_button.pack(pady=10)



# Show the main frame initially
main_frame.pack(padx=20, pady=20)

# Rules Frame
rules_frame = tk.Frame(main_window, bg=dark_blue)

# Rules Frame content
    #Title
rules_label_title = tk.Label(
    rules_frame,
    text="Rules",
    font=("Cooper Black", 24),
    fg=white,
    bg=dark_blue,
    wraplength=450,
)
rules_label_title.pack(pady=20)

    #Rule's Text
rules_label_universe = tk.Label(
    rules_frame,
    text="I'll generate a word for you to guess. This word is from either the Mass Effect, Doctor Who or Critical Role/D&D universes.",
    font=("Arial", 14),
    fg=white,
    bg=dark_blue,
    wraplength=450,
)
rules_label_universe.pack(pady=20)

rules_label_colors = tk.Label(
    rules_frame,
    text="Green means you have a correct letter in the correct place. Yellow means you have a correct letter, but in the wrong place.",
    font=("Arial", 14),
    fg=white,
    bg=dark_blue,
    wraplength=450,
)
rules_label_colors.pack(pady=20)

    # Back button in the rules frame
back_button = tk.Button(rules_frame, text="Back", font=("Cooper Black", 14), bg=light_blue, command=go_back)
back_button.pack(pady=10)


# Game frame settings
game_frame = tk.Frame(main_window, bg=dark_blue)

    #Title
game_label_title = tk.Label(
    game_frame,
    text="Guess the word!",
    font=("Cooper Black", 24),
    fg=white,
    bg=dark_blue,
    wraplength=450,
)
game_label_title.pack(pady=20)


    #Guess Input
guess_entry = tk.Entry(game_frame, font=("Arial", 16), width=20)
guess_entry.pack(pady=10)

    #Submit guess button
guess_entry.bind("<Return>", lambda event: submit_guess()) #Submit with "enter"
submit_button = tk.Button(game_frame, text="Submit", font=("Cooper Black", 14), bg=light_blue, command=submit_guess)
submit_button.pack(pady=10)

    #Space where the feedback and hints will show
feedback_label = tk.Label(game_frame, text="", font=("Arial", 14), fg=white, bg=dark_blue, wraplength=450, justify="left")
feedback_label.pack(pady=20)

    #Hint button
hint_button = tk.Button(game_frame, text="Hint", font=("Cooper Black", 14), bg=light_blue, command=lambda: hints(secret))
hint_button.pack(pady=10)

    #Back to main menu button
back_to_main_button = tk.Button(game_frame, text="Main Menu", font=("Cooper Black", 14), bg=light_blue, command=go_to_main_from_game)
back_to_main_button.pack(pady=10)


#Congratulation Frame Settings
congratulation_frame = tk.Frame(main_window, bg=dark_blue)

    #Title
congratulation_label_title = tk.Label(
    congratulation_frame,
    text="Congratulations!",
    font=("Cooper Black", 24),
    fg=white,
    bg=dark_blue,
    wraplength=450,
)
congratulation_label_title.pack(pady=20)

    #Congratulation text
congratulation_label_text = tk.Label(
    congratulation_frame,
    text=f"Congratulations! You guessed the word {secret} in {guesses} guesses!",
    font=("Arial", 18),
    fg=white,
    bg=dark_blue,
    wraplength=450,
)
congratulation_label_text.pack(pady=20)

    #Play again button
play_again_button = tk.Button(congratulation_frame, text="Play Again", font=("Cooper Black", 14), bg=light_blue, command=play_again)
play_again_button.pack(pady=10)
    #Quit game button
quit_button = tk.Button(congratulation_frame, text="Quit", font=("Cooper Black", 14), bg = light_blue, command = quit_window)
quit_button.pack(pady=10)




# Start the Tkinter event loop ( keeps the window open)
main_window.mainloop()
        



    


    

    
