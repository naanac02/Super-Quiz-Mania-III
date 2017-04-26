print("Welcome to Super Quiz Mania III!")
def pselect():
    players = input("""How many players are there? (2-4)
    """)
    if players == "2":
        p1 = input("""What's your name p1?
        """)
        p2 = input("""What about you p2?
        """)
    elif players == "3":
        p1 = input("""What's your name p1?
        """)
        p2 = input("""What about you p2?
        """)
        p3 = input("""How about p3?
        """)
    elif players == "4":
        p1 = input("""What's your name p1?
        """)
        p2 = input("""What about you p2?
        """)
        p3 = input("""How about p3?
        """)
        p4 = input("""What's your name p4?
        """)
    else:
        print("Sorry, "+str(players)+" is not a valid number")
        pselect()
    print("Welcome all players!")
    input("Press any key to continue...")
pselect()
