# Andrew Jones, IT-140

def main_menu():
    # Print instructions and intro
    print('\nThe Fate of Fairville Adventure Game')
    print('Collect all 6 items to defeat the Orc Lord and save the town!')
    print('Move Commands: go South, go North, go East, go West')
    print('Add Item to Inventory: get "item name"\n')


def move_between_rooms(current_room, move, rooms):
    # move to corresponding room
    current_room = rooms[current_room][move]
    return current_room


def get_item(current_room, move, rooms, inventory):
    # add item to inventory and remove it from the room
    inventory.append(rooms[current_room]['item'])
    del rooms[current_room]['item']


def main():
    # dictionary of connecting rooms with items
    rooms = {
        'Main Gate': {'South': 'Stables', 'North': 'Altar of Truth', 'East': 'Hearth', 'West': 'Armory'},
        'Hearth': {'West': 'Main Gate', 'South': 'Library', 'item': 'Tome Of Fire'},
        'Library': {'North': 'Hearth', 'item': 'Tome Of Knowledge'},
        'Stables': {'North': 'Main Gate', 'item': 'Tome Of Swiftness'},
        'Armory': {'North': 'Keep', 'East': 'Main Gate', 'item': 'Tome Of Strength'},
        'Altar of Truth': {'South': 'Main Gate', 'East': 'Great Bridge', 'item': 'Tome Of Resurrection'},
        'Great Bridge': {'South': 'Dungeon', 'West': 'Altar of Truth'},
        'Dungeon': {'North': 'Great Bridge', 'item': 'Tome Of Darkness'},
        'Keep': ''
    }
    s = ' '
    # list for storing player inventory
    inventory = []
    # starting room
    current_room = 'Main Gate'
    # show the player the main menu
    main_menu()

    while True:
        # handle the case when player encounters the 'villain'
        if current_room == 'Keep':
            # winning case
            if len(inventory) == 6:
                print('"Oh no! You have collected all the Tomes!"')
                print('The Orc Lord falls to his knees and begs for mercy\n')
                print('Congratulations you have defeated the Orc Lord and saved the town!')
                print('Thank you for playing!')
                break
            # losing case
            else:
                print('\n"Ha! You puny human. You did not collect all the Tomes before challenging me!"')
                print('*SQUISH*\n')
                print('You were vanquished by the Orc Lord and the town was destroyed!')
                print('Thank you for playing!')
                break
        # Tell the user their current room, inventory and prompt for a move, ignores case
        print('You are in the ' + current_room)
        print(inventory)
        # tell the user if there is an item in the room
        if current_room != 'Keep' and 'item' in rooms[current_room].keys():
            print('You see the {}'.format(rooms[current_room]['item']))
        print('------------------------------')
        move = input('Enter your move: ').title().split()

        # handle if the user enters a command to move to a new room
        if len(move) >= 2 and move[1] in rooms[current_room].keys():
            current_room = move_between_rooms(current_room, move[1], rooms)
            continue
        # handle if the user enter a command to get an item
        elif len(move) == 4 and move[0] == 'Get' and s.join(move[1:3]) in rooms[current_room]['item']:
            print('You pick up the {}'.format(rooms[current_room]['item']))
            print('------------------------------')
            get_item(current_room, move, rooms, inventory)
            continue
        # handle if the user enters an invalid command
        else:
            print('Invalid move, please try again')
            continue


main()
