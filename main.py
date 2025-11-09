def admin_menu():
    admin_choices = ["AP", "NW", "EP", "EW", "BACK"]
    admin_opt = ""
    while admin_opt not in admin_choices:
        print("Admin Menu")
        print("Type AP to add new players")
        print("Type NW to add new words")
        print("Type EP to edit player data")
        print("Type EW to edit word list")
        print("Type BACK to return to the main menu.")
        admin_opt = input("Enter choice here: ").upper()
        if admin_opt == "AP":
            print("Opening database to add new players")
        elif admin_opt == "NW":
            print("Opening database to add new words")
        elif admin_opt == "EP":
            print("Opening database to edit player data")
        elif admin_opt == "EW":
            print("Opening database to edit word list")
        elif admin_opt == "BACK":
            print("Returning to main menu...")
            main_menu()
        else:
            print("Invalid Input!")


def player_menu():
    game_modes = ["Slang",
                  "Rhyme Time",
                  "Translate",
                  "Contextual",
                  "Chain",
                  "Opposites",
                  "Alpha-Thon",
                  "Back"]
    selection = ""
    while selection not in game_modes:
        print("Player menu")
        print("Available game modes:")
        print("Slang")
        print("Rhyme Time")
        print("Translate")
        print("Contextual")
        print("Chain")
        print("Opposites")
        print("Alpha-Thon")
        print("Back")
        selection = input("Enter choice here: ").title()
        if selection == "Slang":
            print("Entering Slang game mode")
        elif selection == "Rhyme Time":
            print("Entering Rhyme Time game mode")
        elif selection == "Translate":
            print("Entering Translate game mode")
        elif selection == "Contextual":
            print("Entering Contextual game mode")
        elif selection == "Chain":
            print("Entering Chain game mode")
        elif selection == "Opposites":
            print("Entering Opposites game mode")
        elif selection == "Alpha-Thon":
            print("Entering Alpha-Thon game mode")
        elif selection == "Back":
            print("Returning to main menu...")
            main_menu()
        else:
            print("Invalid Input!")


def main_menu():
    admin_login = False
    player_login = False
    while admin_login is False and player_login is False:
        print("Word puzzle game")
        print("Made by Jacob Rosner")
        print("Made in 2025")
        opt = input("Are you an admin or a player? ").lower()
        if opt == "admin":
            admin_login = True
            admin_menu()
        elif opt == "player":
            player_login = True
            player_menu()
        else:
            print("Invalid input!")


main_menu()
