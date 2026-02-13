import random

NUM_PLAYERS = 5
NUMBERS_PER_PLAYER = 3
NUMBER_RANGE = (1, 99)

# Generate players' numbers
players = {}
for i in range(1, NUM_PLAYERS + 1):
    numbers = random.sample(range(NUMBER_RANGE[0], NUMBER_RANGE[1] + 1),
                            NUMBERS_PER_PLAYER)
    players[f"Player {i}"] = numbers

# Lottery numbers
lottery_numbers = random.sample(range(1, 100), NUMBERS_PER_PLAYER)

print("\nLottery Numbers:", lottery_numbers)
print("\nPlayer Numbers:")

for player, nums in players.items():
    print(player, nums)

# Check winners
print("\nResults:")
winner_found = False

for player, nums in players.items():
    matches = set(nums) & set(lottery_numbers)

    if len(matches) == NUMBERS_PER_PLAYER:
        print(player, "WINS! Perfect match:", matches)
        winner_found = True
    elif matches:
        print(player, "partial match:", matches)

if not winner_found:
    print("No full winner this round.") 
