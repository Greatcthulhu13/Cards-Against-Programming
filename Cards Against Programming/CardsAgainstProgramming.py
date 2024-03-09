import random
import os

class CardsAgainstHumanity:
    names = []
    points = []
    def __init__(self):
        self.max_hand_size = 10
        self.min_players = 3
        self.max_rounds = 10
        self.white_cards = self.read_cards('white_cards.txt')
        self.black_cards = self.read_cards('black_cards.txt')
        self.num_players = self.get_valid_player_count()


    @staticmethod
    def read_cards(file_name):
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                return [card.strip() for card in file.readlines()]
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
            exit()
        except Exception as e:
            print(f"An unexpected error occurred while reading '{file_name}': {e}")
            exit()

    def draw_black_card(self):
        chosen_card = random.choice(self.black_cards)
        self.black_cards.remove(chosen_card)
        return chosen_card

    def draw_white_cards(self, num_cards):
        return random.sample(self.white_cards, num_cards)

    def play_round(self, round_num):
        black_card = self.draw_black_card()
        num_answers_required = black_card.count("___")  # Count underscores to determine the number of answers required
        if num_answers_required == 0:
            num_answers_required = 1
            show_response = True 
        else:
            show_response = False
        black_card = black_card.replace('"','')  # Removes the speech marks in the black card because I'm too lazy to do it myself
        ccz = round_num % self.num_players


        player_responses = {}

        for playernum in range(self.num_players):
            if(playernum != ccz):
                player = self.names[playernum]
                player_hand = self.draw_white_cards(self.max_hand_size)
                chosen_cards = self.get_player_choices(player, player_hand, num_answers_required, black_card)
                player_responses[player] = chosen_cards
        os.system("clear")
        print("\nThe black card was:")
        print(black_card)
        print("")
        print("Responses:")

        for player, responses in player_responses.items():
            filled_black_card = black_card
            for i, response in enumerate(responses, 1):
                # Replace the first set of underscores with the first response and the second set with the second response
                if i == 1:
                    filled_black_card = filled_black_card.replace("___", response, 1)
                else:
                    filled_black_card = filled_black_card.replace("____", response, 1)
            if show_response == False:
                print(f"Player {player}'s response: {filled_black_card}")
                print("=" * 30)
            else:
                print(f"Player {player}'s response: {response}")
                print("=" * 30)
        print("")
        print(f"The card czar is: {self.names[ccz]}\n")


        # Simple scoring mechanism: random player wins
        while True:
            winner_name = input("Decide the winner: ")
            try:
                playernum = self.names.index(winner_name)
                self.points[playernum] += 1
                print(f"\nPlayer {winner_name} wins this round!\n")
                break
            except:
                print("Invalid player name.")

    def get_valid_player_count(self):
        num_players = int(input("Number of players:"))
        for i in range(num_players):
            self.names.append(input("enter player's name: "))
            self.points.append(0)
        return num_players
    def get_player_choices(self, player, player_hand, num_answers_required, black_card):
        os.system("clear")
        print(f"\nBlack Card: {black_card}")
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
        game.play_round(round_num)

        play_again = input("Do you want to play another round? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            print("The winner is: ")
            winner_num = game.points.index(max(game.points))
            print(game.names[winner_num])
            break
