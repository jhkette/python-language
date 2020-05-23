
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, 
lisa=50.25, harrison=10.0)



# Use a loop to add together all the donations and store the resulting number in a variable called total_donations

total_donations = 0
for value in donations.values():
    total_donations += value
    
# This code picks a random food item:
from random import choice #DON'T CHANGE!


#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}
# use choice to get random food
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

if bakery_stock.get(food):
    print(str(bakery_stock[food]) + ' left')
else:
    print("We don't make that")



game_properties = ["current_score", "high_score", "number_of_lives", 
"items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", 
"enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 

# default value is second argument to fromkeys
initial_game_state = dict.fromkeys(game_properties, 0)

