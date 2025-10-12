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
        elif opt == "player":
            print("Opening player menu...")
            player_login = True
        elif opt == "log out":
            print("Logging out now. Goodbye!")
            logout = True
        else:
            print("Invalid input!")
main_menu()