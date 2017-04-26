print("Welcome to Super Quiz Mania III!")
def pselect():
    players = input("""How many players are there? (2-4)
    """)
    if players == "2":
        p1 = input("""What's your name p1?
        """)
        p2 = input("""What about you p2?
        """)
        print("Welcome "+str(p1)+" and "+str(p2))
    elif players == "3":
        p1 = input("""What's your name p1?
        """)
        p2 = input("""What about you p2?
        """)
        p3 = input("""How about p3?
        """)
        print("Welcome "+str(p1)+", "+str(p2)+", and "+str(p3))
    elif players == "4":
        p1 = input("""What's your name p1?
        """)
        p2 = input("""What about you p2?
        """)
        p3 = input("""How about p3?
        """)
        p4 = input("""What's your name p4?
        """)
        print("Welcome "+str(p1)+", "+str(p2)+", "+str(p3)+", and "+str(p4))
    else:
        print("Sorry, "+str(players)+" is not a valid character")
        pselect()
    input("Press any key to continue...")
pselect()

