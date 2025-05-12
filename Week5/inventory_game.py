import time

# Intro sequence
intro_lines = [
    "Welcome to the Survive the Apocalypse Game!",
    "The year is 2088.",
    "As a consequence of WW3, the world as we knew it is gone.",
    "A massive atomic bomb has been dropped.",
    "The sky turned black and everything vanished.",
    "The oceans boiled.",
    "As a result of the radioactive global pollution, people... mutated.",
    "",
    "Now they aren't normal humans.",
    "They hunt for people like you.",
    "Survivors.",
    "Because they feed themselves with it.",
    "",
    "You are one of the last survivors.",
    "",
    "In order to survive you need to scavenge, fight and make reasonable decisions.",
    "",
    "Type 'help' to begin."
]

for line in intro_lines:
    print(line)
    time.sleep(0.5)

# Game variables
inventory = []
items_in_room = [
    {"name": "bread", "type": "food", "uses": 1},
    {"name": "bandage", "type": "healing", "uses": 1},
    {"name": "knife", "type": "weapon", "uses": 3},
    {"name": "matches", "type": "tool", "uses": 2},
    {"name": "bottle", "type": "water", "uses": 1},
    {"name": "key", "type": "key", "uses": 1},
    {"name": "stick", "type": "tool", "uses": 1}
]

max_inventory_size = 5
fire_created = False
game_over = False
door_locked = True
escaped = False

# Game functions
def show_room_items():
    print("\nItems in this area:")
    for item in items_in_room:
        print(f"- {item['name']} ({item['type']})")


def show_inventory():
    print("\nYour Inventory:")
    if not inventory:
        print(" - (empty)")
    else:
        for item in inventory:
            print(f"- {item['name']} ({item['type']}) uses: {item.get('uses', 1)}")


def pick_up(item_name):
    if len(inventory) >= max_inventory_size:
        print("Your inventory is full! Drop something first.")
        return
    for item in items_in_room:
        if item['name'].lower() == item_name.lower():
            inventory.append(item)
            items_in_room.remove(item)
            print(f"You picked up {item_name}.")
            if item_name.lower() == "matches":
                print("Matches! Nice. Now find something to burn... maybe a stick?")
            return
    print(f"There is no {item_name} here.")


def drop(item_name):
    for item in inventory:
        if item['name'].lower() == item_name.lower():
            items_in_room.append(item)
            inventory.remove(item)
            print(f"You dropped {item_name}.")
            return
    print(f"You don't have {item_name} in your inventory.")


def use(item_name):
    global fire_created, game_over, door_locked, escaped

    for item in inventory:
        if item['name'].lower() == item_name.lower():
            # Fire making
            if item_name.lower() == "matches":
                if has_item("stick"):
                    print("You use the matches and the stick... You’ve made a fire.")
                    fire_created = True
                    remove_item("stick")
                    item['uses'] -= 1
                else:
                    print("You strike the matches... but there's nothing to burn.")
                    item['uses'] -= 1

            # Key logic with moral decision
            elif item_name.lower() == "key":
                if door_locked:
                    if has_item_type("food"):
                        print("You use the key and unlock the heavy bunker door...")
                        print("But as you push it open, you hear a faint voice behind you.")
                        print("Another survivor is trapped in a nearby room. They're begging for help.")
                        print("Do you:")
                        print("1) Help the survivor (risky but humane)")
                        print("2) Escape alone (safe but cold-hearted)")
                        choice = input("> ").strip()

                        if choice == "1":
                            if has_item("knife"):
                                print("You rush to the locked room and use your knife to break it open.")
                                print("You free the survivor, and together you escape to the surface.")
                                print("It’s not just survival anymore — it’s humanity.")
                                escaped = True
                                game_over = True
                            else:
                                print("You try to help, but without a weapon or tool, you can’t break the door.")
                                print("You fail. Maybe next time.")
                        elif choice == "2":
                            print("You slam the door behind you and run toward the daylight.")
                            print("The screams fade behind you. You're safe... but at what cost?")
                            escaped = True
                            game_over = True
                        else:
                            print("You hesitate. The door closes. You’ll need to try again.")
                        door_locked = False
                    else:
                        print("You need at least some food before escaping. You won't survive outside.")
                else:
                    print("The door is already unlocked.")

            # Generic item use
            else:
                print(f"You used the {item_name}.")
                item['uses'] -= 1

            if item['uses'] <= 0:
                inventory.remove(item)
                print(f"The {item_name} is now used up and gone.")
            return
    print(f"You don't have {item_name} in your inventory.")


def examine(item_name):
    for item in inventory + items_in_room:
        if item['name'].lower() == item_name.lower():
            print(f"Examining {item['name']}... It is a {item['type']}.")
            return
    print(f"There's no item named {item_name} here or in your inventory.")


def show_help():
    print("""
Available commands:
- inventory         → Show your current items
- pickup [item]     → Pick up an item from the area
- drop [item]       → Drop an item from your inventory
- use [item]        → Use an item (e.g., eat food or use a tool)
- examine [item]    → Get details about an item
- look              → Show what items are in the area
- help              → Show this help message
- quit              → Exit the game
""")


def has_item(item_name):
    return any(item['name'].lower() == item_name.lower() for item in inventory)


def has_item_type(item_type):
    return any(item['type'].lower() == item_type.lower() for item in inventory)


def remove_item(item_name):
    for item in inventory:
        if item['name'].lower() == item_name.lower():
            inventory.remove(item)
            return


# Start game
show_room_items()
print("\nGame is ready. Waiting for your command...")

while not game_over:
    command = input("\n> ").strip().lower()

    if command == "quit":
        print("Exiting game. Stay safe out there, survivor.")
        break
    elif command == "help":
        show_help()
    elif command == "inventory":
        show_inventory()
    elif command == "look":
        show_room_items()
    elif command.startswith("pickup "):
        item_name = command[len("pickup "):]
        pick_up(item_name)
    elif command.startswith("drop "):
        item_name = command[len("drop "):]
        drop(item_name)
    elif command.startswith("use "):
        item_name = command[len("use "):]
        use(item_name)
    elif command.startswith("examine "):
        item_name = command[len("examine "):]
        examine(item_name)
    else:
        print("Unknown command. Type 'help' for a list of valid commands.")
