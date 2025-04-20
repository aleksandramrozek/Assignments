"""
This is a simple text-based game that helps the user to choose a holiday destination based on their ideal weather preferences (temperature in Celsius).
The program asks the user for their ideal temperature and then suggests nice travel destinations.
Author: Aleksandra Mrozek <3
"""
import time
import emoji

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

slow_print(emoji.emojize("🌍 Welcome to the Travel Recommender Game!"))
slow_print(emoji.emojize("Let's find your perfect holiday destination based on your temperature preference! ☀️❄️"))

# 1. User's name
name = input("What's your name? ")
slow_print(f"Nice to meet you, {name}!")

# 2. Temperature
while True:
    temp_input = input("Enter your ideal holiday temperature (in °C): ")
    if temp_input.isdigit():
        temp = int(temp_input)
        if -50 <= temp <= 60:
            break
        else:
            print("Please enter a realistic temperature between -50 and 60°C.")
    else:
        print("That's not a valid number. Try again!")

# 3. Recommended destination based on temperature
if temp < 0:
    slow_print(emoji.emojize("Brrr... You must love the cold! 🏔️"))
    slow_print(emoji.emojize("We recommend skiing in the Alps or a trip to Iceland!"))
elif 0 <= temp <= 10:
    slow_print(emoji.emojize("You like it chilly, huh? ❄️"))
    slow_print(emoji.emojize("How about visiting Norway or Scotland?"))
elif 11 <= temp <= 19:
    slow_print(emoji.emojize("A mild temperature, very classy. 🍂"))
    slow_print(emoji.emojize("You might enjoy springtime in Paris or hiking in the Swiss mountains."))
elif 20 <= temp <= 30:
    slow_print(emoji.emojize("Ah, the perfect warm weather! 🌞"))
    slow_print(emoji.emojize("Spain, Greece, or the south of France would be amazing!"))
elif 31 <= temp <= 40:
    slow_print(emoji.emojize("You're going tropical! 🏝️"))
    slow_print(emoji.emojize("Bali, Thailand, or the Caribbean islands are calling you."))
else:
    slow_print(emoji.emojize("Whoa! You like it hot like a desert! 🔥"))
    slow_print(emoji.emojize("Maybe try the Sahara, Dubai, or Death Valley!"))

# 4. Bonus question: adventure or relaxation?
choice = input("Do you prefer (a) adventure or (b) relaxation? ").lower()

while choice not in ["a", "b"]:  # If the input is neither "a" nor "b", ask again
    slow_print(emoji.emojize("Invalid input. Please enter 'a' for adventure or 'b' for relaxation."))
    choice = input("Do you prefer (a) adventure or (b) relaxation? ").lower()
if choice == "a":
    slow_print(emoji.emojize("Great! We'll plan some mountain hikes, safaris, or jungle tours! 🧗‍♀️"))
    if temp < 10:
        slow_print(emoji.emojize("Cold adventures? Maybe dog sledding in Lapland! 🐾"))
elif choice == "b":
    slow_print(emoji.emojize("Relaxation it is. Expect beaches, spas, and sunsets. 🌅"))
    if temp > 30:
        slow_print(emoji.emojize("You’ll be sipping drinks under a palm tree in no time. 🍹"))
    else:
        slow_print(emoji.emojize("If you prefer something else than these two forms of travel, feel free to do destination research based on your individual preferences!"))

slow_print(emoji.emojize("Thanks for playing! ✈️ Safe travels, wanderer!"))