import itertools

__suspects = ['White', 'Green', 'Peacock', 'Plumb', 'Scarlet', 'Mustard']
__rooms = ['Dining Room', 'Lounge', 'Kitchen', 'Study', 'Hall', 'Billiard Room', 'Conservatory', 'Ballroom', 'Library', 'Cellar']
__weapons = ['Dagger', 'Lead Pipe', 'Spanner', 'Candlestick', 'Revolver', 'Rope']

my_suspect = input("Enter Your Suspect: ")
my_room = input("Enter Your Room: ")
my_weapon = input("Enter Your Weapon: ")

print("___________________________")
print("Generating Combinations")
print("___________________________")

__suspects.remove(my_suspect)
__rooms.remove(my_room)
__weapons.remove(my_weapon)

combo_list = [__suspects, __rooms, __weapons]
combo_list = list(itertools.product(*combo_list))

Round = 0

def select_pop(this_rounds_guess):
    global Round
    global combo_list
    global __suspects
    global __weapons
    global __rooms
    selection_0 = int(input("(1) = Iterate Round, (2) = Enter Details: "))
    if selection_0 == 1:
        Round += 1
        return
    elif selection_0 == 2:
        Round +=1
        selection_1 = int(input("(1) Enter Character, (2) Enter Room, (3) Enter Weapon: "))
        if selection_1 == 1:
            __suspects.remove(this_rounds_guess[0])
        elif selection_1 == 2:
            __rooms.remove(this_rounds_guess[1])
        elif selection_1 == 3:
            __weapons.remove(this_rounds_guess[2])
        else:
            print("Invalid selection")
            select_pop()
        combo_list = [__suspects, __rooms, __weapons]
        combo_list = list(itertools.product(*combo_list))
        return
    else:
        select_pop()

while len(combo_list) > 1:
    print("Round", Round)
    print("Guesses Remaining", len(combo_list))
    print("Remaining Suspects", len(__suspects))
    print("Remaining Rooms", len(__rooms))
    print("Remaining Weapons", len(__weapons))
    this_rounds_guess = combo_list[0]
    print("This Round's Guess: ", this_rounds_guess)
    select_pop(this_rounds_guess)

print("Final guess: ", combo_list)
    
