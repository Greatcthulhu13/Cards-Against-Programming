import random

phand = ["Cards Against Programming"]
print(phand)

for xx in range(0, len(phand)):
  pcarddisplay = []
  pcarddisplay.append("┌─────────┐")
  pcarddisplay.append("│{}{}. . .│")
  pcarddisplay.append("│. . . . .│")
  pcarddisplay.append("│. . . . .│")
  pcarddisplay.append("│. . . . .│")
  pcarddisplay.append("│. . . . .│")
  pcarddisplay.append("│. . . . .│")
  pcarddisplay.append("│. . .{}{}│")
  pcarddisplay.append("└─────────┘")

  x = ("│.", phand[xx][:1], ". . . .│")
  pcarddisplay[1] = "".join(x)

  x = ("│. . . .", phand[xx][:1], ".│")
  pcarddisplay[7] = "".join(x)

  print("\n".join(pcarddisplay))

class CardsAgainstHumanity:
    def __init__(self, black_cards_file="black_cards.txt", white_cards_file="white_cards.txt"):
        self.max_hand_size = 10
        self.min_players = 3
        self.max_rounds = 5

        # Load black cards from file
        with open(black_cards_file, "r") as file:
            self.black_cards = [line.strip() for line in file.readlines()]

        # Load white cards from file
        with open(white_cards_file, "r") as file:
            self.white_cards = [line.strip() for line in file.readlines()]

    def draw_black_card(self):
        chosen_card = random.choice(self.black_cards)
        if "," in chosen_card:
            return tuple(chosen_card.split(","))
        else:
            self.black_cards.remove(chosen_card)
            return chosen_card

    def draw_white_cards(self, num_cards):
        return random.sample(self.white_cards, num_cards)

    def play_round(self):
        black_card = self.draw_black_card()
        num_answers_required = int(black_card[1]) if isinstance(black_card, tuple) else 1
        print(f"\nBlack Card: {black_card}")

        num_players = self.get_valid_player_count()

        player_responses = {}

        for player in range(1, num_players + 1):
            white_cards = self.draw_white_cards(self.max_hand_size)
            print(f"\nPlayer {player}'s White Cards:")
            for card in white_cards:
                print(card)

            chosen_cards = self.get_player_choices(player, white_cards, num_answers_required)
            player_responses[player] = chosen_cards

        print("\nResponses:")
        for player, response in player_responses.items():
            print(f"Player {player}: {response}")

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

    def get_player_choices(self, player, white_cards, num_answers_required):
        chosen_cards = []

        for i in range(num_answers_required):
            while True:
                try:
                    print(f"\nChoose a card for Player {player} (Pick {len(chosen_cards) + 1}):")
                    for i, card in enumerate(white_cards, start=1):
                        print(f"{i}. {card}")
                    choice_index = int(input("Enter the number of your choice: "))
                    if 1 <= choice_index <= len(white_cards):
                        chosen_cards.append(white_cards.pop(choice_index - 1))
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
