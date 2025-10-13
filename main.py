def admin_menu():
    admin = ["AP", "NW", "EP", "EW", "BACK"]
    admin_opt = ""
    while admin_opt not in admin:
        print("Admin menu")
        print("Type AP to add a new player")
        print("Type NW to add new words")
        print("Type EP to edit player data")
        print("Type EW to edit the word list")
        print("Type BACK to return to the main menu")
        admin_opt = input("Enter choice here: ").upper()
        if admin_opt == "AP":
            print("Opening database to add new players")
        elif admin_opt == "NW":
            print("Opening database to add new words")
        elif admin_opt == "EP":
            print("Opening database to edit player data")
        elif admin_opt == "EW":
            print("Opening database to edit words")
        elif admin_opt == "BACK":
            print("Returning to main menu")
            main_menu()
        else:
            print("Invalid Input!")

def player_menu():
    player = ["Slang",
              "Rhyme Time",
              "Translate",
              "Contextual",
              "Chain",
              "Opposites",
              "Alpha-Thon",
              "Back"]
    player_opt = ""
    while player_opt not in player:
        print("Player Menu")
        print("Available game modes:")
        print("Slang")
        print("Rhyme Time")
        print("Translate")
        print("Contextual")
        print("Chain")
        print("Opposites")
        print("Alpha-Thon")
        print("Back (return to main menu)")
        player_opt = input("Enter choice here: ").title()
        if player_opt == "Slang":
            print("Entering Slang game mode")
        elif player_opt == "Rhyme Time":
            print("Entering Rhyme Time game mode")
        elif player_opt == "Translate":
            print("Entering Translate game mode")
        elif player_opt == "Contextual":
            print("Entering Contextual game mode")
        elif player_opt == "Chain":
            print("Entering Chain game mode")
        elif player_opt == "Opposites":
            print("Entering Opposites game mode")
        elif player_opt == "Alpha-Thon":
            print("Entering Alpha-Thon game mode")
        elif player_opt == "Back":
            print("Returning to main menu.")
            main_menu()
        else:
            print("Invalid input!")

def main_menu():
    admin_login = False
    player_login = False
    logout = False
    while admin_login == False and player_login == False and logout == False:
        print("Word Puzzle Game.")
        print("Made by Jacob Rosner.")
        print("Made in 2025.")
        opt = input("Are you a player or an admin? Or do you want to log out? ").lower()
        if opt == "admin":
            print("Opening admin menu...")
            admin_login = True
            admin_menu()
        elif opt == "player":
            print("Opening player menu...")
            player_login = True
            player_menu()
        elif opt == "log out":
            print("Logging out now. Goodbye!")
            logout = True
        else:
            print("Invalid input!")
main_menu()