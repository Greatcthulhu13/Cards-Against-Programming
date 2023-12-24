import random

# Function to read cards from a text file
def read_cards(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        cards = file.readlines()
        cards = [card.strip() for card in cards]
    return cards

white_cards = read_cards('white_cards.txt')
black_cards = read_cards('black_cards.txt')

class CardsAgainstHumanity:
    def __init__(self):
        self.max_hand_size = 10
        self.min_players = 3
        self.max_rounds = 5

    def draw_black_card(self):
        chosen_card = random.choice(black_cards)
        black_cards.remove(chosen_card)
        return chosen_card

    def draw_white_cards(self, num_cards):
        return random.sample(white_cards, num_cards)

    def play_round(self):
        black_card = self.draw_black_card()
        num_answers_required = black_card.count("___")  # Count underscores to determine the number of answers required
        if num_answers_required == 0:
            num_answers_required = 1
            showresponse = True 
        else:
            showresponse = False
        black_card = black_card.replace('"','') #Removes the speech marks in the black card bcs I'm too lazy to do it myself

        print(f"\nBlack Card: {black_card}")

        num_players = self.get_valid_player_count()

        player_responses = {}

        for player in range(1, num_players + 1):
            player_hand = self.draw_white_cards(self.max_hand_size)

            chosen_cards = self.get_player_choices(player, player_hand, num_answers_required)
            player_responses[player] = chosen_cards

        print("\nThe black card was:")
        print(black_card)
        print("Responses:")

        for player, responses in player_responses.items():
            filled_black_card = black_card
            for i, response in enumerate(responses, 1):
                # Replace the first set of underscores with the first response and the second set with the second response
                if i == 1:
                    filled_black_card = filled_black_card.replace("___", response, 1)
                else:
                    filled_black_card = filled_black_card.replace("____", response, 1)
            if showresponse == False:
                print(f"Player {player}'s response: {filled_black_card}")
                print("=" * 30)
            else:
                print(f"Player {player}'s response: {response}")
                print("=" * 30)

        # Simple scoring mechanism: random player wins
        winner = random.choice(list(player_responses.keys()))
        print(f"\nPlayer {winner} wins this round!\n")

    def get_valid_player_count(self):
        while True:
            try:
                num_players = int(input("Enter the number of players: "))
                if num_players < self.min_players:
                    print("You need at least 3 players to play. Try again.")
                else:
                    return num_players
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_player_choices(self, player, player_hand, num_answers_required):
        chosen_cards = []

        for i in range(num_answers_required):
            while True:
                try:
                    print(f"\nChoose a card for Player {player} (Pick {len(chosen_cards) + 1}):")
                    for i, card in enumerate(player_hand, start=1):
                        print(f"{i}. {card}")
                    choice_index = int(input("Enter the number of your choice: "))
                    if 1 <= choice_index <= len(player_hand):
                        chosen_cards.append(player_hand.pop(choice_index - 1))
                        break
                    else:
                        print("Invalid choice. Please enter a number within the given range.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        return chosen_cards

if __name__ == "__main__":
    game = CardsAgainstHumanity()

    for round_num in range(1, game.max_rounds + 1):
        print(f"\n--- Round {round_num} ---")
        game.play_round()

        play_again = input("Do you want to play another round? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break
