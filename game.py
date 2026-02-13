import random


def generate_lottery_numbers(count, min_num, max_num):
    """Generate random lottery numbers."""
    return random.sample(range(min_num, max_num + 1), count)


def generate_players_numbers(num_players, numbers_per_player, min_num, max_num):
    """Generate numbers for all players using a loop."""
    players = {}
    for i in range(1, num_players + 1):
        numbers = random.sample(range(min_num, max_num + 1), numbers_per_player)
        players[f"Player {i}"] = numbers
    return players


def check_matches(player_numbers, lottery_numbers):
    """Check how many numbers match between player and lottery."""
    return set(player_numbers) & set(lottery_numbers)


def display_results(players, lottery_numbers):
    """Display all players' numbers and check for winners using loops and conditionals."""
    print("\n" + "="*50)
    print("LOTTERY NUMBERS:", sorted(lottery_numbers))
    print("="*50)
    
    print("\nPLAYER NUMBERS:")
    for player, nums in players.items():
        print(f"{player}: {sorted(nums)}")
    
    # Check for winners using conditional logic
    print("\n" + "="*50)
    print("RESULTS:")
    print("="*50)
    
    winner_found = False
    partial_winners = []
    
    for player, nums in players.items():
        matches = check_matches(nums, lottery_numbers)
        match_count = len(matches)
        
        # Conditional: check different match scenarios
        if match_count == len(lottery_numbers):
            print(f"🎉 {player} WINS! Perfect match: {sorted(matches)}")
            winner_found = True
        elif match_count >= 2:
            partial_winners.append((player, matches))
            print(f"✨ {player} - {match_count} matches: {sorted(matches)}")
        elif match_count == 1:
            print(f"   {player} - 1 match: {sorted(matches)}")
        else:
            print(f"   {player} - No matches")
    
    # Final conditional summary
    print("\n" + "="*50)
    if winner_found:
        print("🏆 We have a GRAND WINNER!")
    elif partial_winners:
        print(f"📊 {len(partial_winners)} player(s) with partial matches!")
    else:
        print("❌ No winners this round. Better luck next time!")
    print("="*50)


def get_valid_input(prompt, min_val, max_val):
    """Get valid integer input from user using loop and conditionals."""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"⚠️  Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("⚠️  Invalid input! Please enter a valid number.")


def play_game():
    """Main game function with configurable settings."""
    print("\n" + "="*50)
    print("   WELCOME TO THE LOTTERY GAME!")
    print("="*50)
    
    # Get game configuration with input validation
    num_players = get_valid_input("\nEnter number of players (1-10): ", 1, 10)
    numbers_per_player = get_valid_input("Enter numbers per player (3-6): ", 3, 6)
    max_number = get_valid_input("Enter maximum number range (10-100): ", 10, 100)
    
    # Generate lottery and player numbers
    lottery_numbers = generate_lottery_numbers(numbers_per_player, 1, max_number)
    players = generate_players_numbers(num_players, numbers_per_player, 1, max_number)
    
    # Display results
    display_results(players, lottery_numbers)


def main():
    """Main entry point with play-again loop."""
    while True:
        play_game()
        
        # Conditional: ask to play again
        play_again = input("\n🎮 Play again? (yes/no): ").strip().lower()
        
        if play_again in ['yes', 'y']:
            continue
        elif play_again in ['no', 'n']:
            print("\n👋 Thanks for playing! Goodbye!")
            break
        else:
            # Loop continues if invalid input
            print("Invalid choice. Please enter 'yes' or 'no'.")
            continue


if __name__ == "__main__":
    main() 
