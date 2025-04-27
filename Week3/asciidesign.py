#My zombie apocalypse game based on the ASCII design
import time
import random
text = ("The zombie apocalypse is coming!!! Brace yourself!!!")
words = text.split()
for word in words:
    print(word, end=" ", flush=True)
    time.sleep(0.5)
print()
def generate_grid(width, height, hero_symbol):
    grid = []
    for i in range(height):
        row = []
        for j in range(width):
            if i == height // 2 and j == width // 2:
                row.append(hero_symbol)
            else:
                if random.random() < 0.1:
                    row.append("Z")
                else:
                    row.append(".")
        grid.append(row)
    return grid

def display_grid(grid):
    print("\nZombie Apocalypse Map:")
    for row in grid:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" ")
        print("|")
    print("~" * (len(grid[0]) + 2))


width = int(input("Select your wanted width, e.g. 10 - has to be an integer:"))
height = int(input("Select your wanted height, e.g. 5 - has to be an integer:"))
hero_symbol = (input("Select your wanted hero symbol, e.g. @, !, #, $ - has to be a special symbol:"))

grid = generate_grid(width, height, hero_symbol)
print("\nHere is your zombie apocalypse grid:")
time.sleep(1)
display_grid(grid)


choice = input("\nWhat will you do? fight/run: ")
if choice == "fight":
    print("Grab a weapon and get ready to fight!")
    time.sleep(3)

    weapons = ["Cooking pan", "Lightsaber from Star Wars", "Voldemort's Wand", "Revolver from the West"]
    weapon = random.choice(weapons)
    print(f"\nYou found a {weapon}!")
    time.sleep(3)
elif choice == "run":
    print("Start running as fast as you can!")
    time.sleep(3)
else:
    print("You do not react... The zombies are getting closer!")
    time.sleep(3)




