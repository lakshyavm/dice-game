import random
import sys

def get_standings(scores):
    # Returns a sorted list of (player, score) tuples
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)

def display_leaderboard(standings):
    places = ['🥇 Winner', '🥈 Runner Up', '🥉 Third Place']
    print("\n🏁 Final Standings 🏁")
    for i, (player, score) in enumerate(standings):
        label = places[i] if i < len(places) else f"{i+1}th Place"
        print(f"{label}: {player} with {score} points")
        if i == 2:
            break  # Only first, runner up, and third
    # Announce ties if they exist for places
    top_scores = [s for p,s in standings]
    if top_scores.count(top_scores[0]) > 1:
        print(f"✨ It's a Tie for First Place! ✨")
    elif len(standings) > 1 and top_scores.count(top_scores[1]) > 1:
        print(f"✨ It's a Tie for Runner Up! ✨")
    elif len(standings) > 2 and top_scores.count(top_scores[2]) > 1:
        print(f"✨ It's a Tie for Third Place! ✨")

def dice_game_tournament(players, rounds=10):
    scores = {player: 0 for player in players}
    prev_rolls = {player: None for player in players}

    print("\n🎲 Welcome to the Dice Game Tournament! 🎲")
    print(f"Players: {', '.join(players)}")
    print(f"Rounds: {rounds}")
    print("Let the game begin!\n")

    for round_num in range(1, rounds + 1):
        print(f"\n=== Round {round_num} ===")
        for player in players:
            input(f"{player}, press Enter to roll the dice... ")
            roll = random.randint(1, 6)
            print(f"{player} rolled a {roll}.")

            # Game rules
            if roll == 6:
                scores[player] += 10
                print("Great! +10 points.")
                if prev_rolls[player] == 6:
                    scores[player] += 5
                    print("Amazing! Back-to-back 6s! +5 bonus!")
            elif roll == 1:
                scores[player] -= 5
                print("Oh no! -5 points.")
            else:
                scores[player] += roll
                print(f"+{roll} points.")

            if scores[player] < 0:
                print("Score dropped below zero. Reset to 0.")
                scores[player] = 0

            prev_rolls[player] = roll
            print(f"{player}'s total score: {scores[player]}\n")

    standings = get_standings(scores)
    display_leaderboard(standings)
    print("\nAll players' scores:")
    for player, score in standings:
        print(f"{player}: {score} points")

def main():
    while True:
        print("\nEnter player names (comma-separated):")
        input_players = input().strip().split(",")
        players = [p.strip() for p in input_players if p.strip()]
        if len(players) < 2:
            print("At least two players are required. Please enter again.")
            continue

        while True:
            try:
                rounds = int(input("Enter number of rounds (default 10): ") or 10)
                if rounds < 1:
                    print("Number of rounds must be at least 1.")
                    continue
                break
            except ValueError:
                print("Please enter a valid integer for rounds.")

        dice_game_tournament(players, rounds)

        # Play again prompt
        while True:
            answer = input("\nDo you want to play again? (y/n): ").strip().lower()
            if answer in {'y', 'yes'}:
                break  # Outer while continues (new game)
            elif answer in {'n', 'no', 'exit', 'quit'}:
                print("Thank you for playing! Goodbye 🎉")
                sys.exit()
            else:
                print("Please enter 'y' to play again or 'n' to exit.")

if __name__ == "__main__":
    main()