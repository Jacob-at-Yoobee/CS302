import random

themes = ["Cities",
          "Animals",
          "Food",
          "Jobs",
          "Names",
          "Places"]

slang_meanings = {"Rizz": "Charisma",
                  "Nerd": "Know It All",
                  "LOL": "Laughing Out Loud",
                  "Cap": "Lies",
                  "Bruh moment": "Stupid Mistake",
                  "Deez Nuts": "Peanuts, Acorns, Almonds, Etc.",
                  "Cringe": "Annoying",
                  "Sus (adjective)": "Suspicious",
                  "Sus (verb)": "Suspect",
                  "Flip the Bird": "Give Someone The Middle Finger",
                  "OG": "Original",
                  "Drip": "High Fashion",
                  "Zesty": "Fruity",
                  "Chad": "Hunk",
                  "Karen": "Entitled Person (often a woman)"}

def slang_mode():
    lives = 3
    score = 0
    print("Welcome to the Slang mode!")
    print("In this mode, you must guess the meaning of a slang term.")
    print("Good luck!")
    while lives > 0:
        print("Preparing word...")
        slang_word = random.choice(list(slang_meanings.keys()))
        meaning = input("What is the definition of {}? ".format(slang_word)).title()
        if meaning == slang_meanings[slang_word]:
            print("Well done!")
            score += 1
        else:
            print("Incorrect!")
            print("{} actually means {}".format(slang_word, slang_meanings[slang_word]))
            lives -= 1

    print("Game Over!")
    print("You scored a total of {} points.".format(score))

def gameplay():
    modes = ["Slang",
             "Chain",
             "Opposites",
             "Alpha-Thon",
             "Rhyme Time",
             "Translate",
             "Contextual"]
    selected = ""
    while selected not in modes:
        print("Welcome to Jacob's Word Game!")
        print("There are seven game modes available.")
        print("They are Slang, Chain, Alpha-Thon, Rhyme Time, Opposites, Translate and Contextual.")
        selected = input("Which mode do you wish to play? ").title()
    if selected == "Slang":
        slang_mode()
    else:
        print("Invalid input!")

gameplay()