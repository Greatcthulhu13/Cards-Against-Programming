import random

class CardsAgainstHumanity:
    def __init__(self):
        self.max_hand_size = 7  # Number of white cards each player draws
        self.min_players = 3   # Minimum number of players required
        self.max_rounds = 5    # Maximum number of rounds for the game

        self.black_cards = [
            "I never truly understood ___ until I encountered ___.",
            "What's that smell?",
            "In an attempt to reach a wider audience, the Smithsonian Museum of Natural History has opened an interactive exhibit on ___.",
            "In its new tourism campaign, Detroit proudly proclaims that it has finally eliminated _____.",
            "_____ is a slippery slope that leads to _____.",
            "In M. Night Shyamalan's new movie, Bruce Willis discovers that _____ had really been _____ all along.",
            "What ended my last relationship?", 
            "What gets better with age?",
            "What gives me uncontrollable gas?",
            "_____. High five, bro.",
            "_____. It's a trap!",
            "What helps Obama unwind?",
            "____ was in my car boot",
            "I had to go to the hospital because of ____",
            "My visit to Japan was great because of _____",
            "What would grandma find disturbing, yet oddly charming?",
            "What never fails to liven up the party?",
            "What is the meaning of life?",
            "______. Is why your dad left",
            "Lifetime presents _____, the story of _____.",
            "And I would have gotten away with it, too, if it hadn't been for _____.",
            "What's a girl's best friend?",
            "Major League Baseball has banned _____ for giving players an unfair advantage.",
            "And the Academy Award for _____ goes to _____.",
            "BILLY MAYS HERE FOR _____!",
            "Rumor has it that Vladimir Putin's favorite dish is _____ stuffed with _____.",
            "Coming to Broadway this season, _____: The Musical",
            "Science will never explain the origin of _____.!",
            "Dear Abby, I'm having some trouble with _____ and would like your advice.",
            "What's the gift that keeps on giving?",
            "Sorry everyone, I just _____.",
            "Due to a PR fiasco, Walmart no longer offers _____.",
            "Who is the most emo?",
            "Studies show that lab rats navigate mazes 50% faster after being exposed to _____.",
            "During Picasso's often-overlooked Brown Period, he produced hundreds of paintings of _____.",
            "What's the new fad diet?",
            "Maybe she's born with it. Maybe it's _____.",
            "What's there a ton of in heaven?",
            "In 1,000 years, when paper money is but a distant memory, _____ will be our currency.",
            "Why am I sticky?",
            "What do old people smell like?",
            "What will that one friend be arrested for?",
            "In 1,000 years, when paper money is but a distant memory, _____ will be our currency.",
            "What did I bring back from Mexico?",
            "In a world ravaged by _____, our only solace is _____.",
            "Who stole the cookies from the cookie jar?",
            "What is George Bush thinking about?",
            "Thank god for _____",
            "If I had a time machine, I would change _____",
            "If I had a penny everytime someone said ______. I'd have one penny.",
            "In 2024 the Pope will announce the Bible 2, featuring ______",
            "What was the cause of my divorce?",
            "The new Star Wars film will feature a cameo from ______",
            "What did I get in my Christmas stocking?",
            "What did I get for Christmas?",
            "What did I get for my Birthday?",
            "The train is now departing for ______",
            "What is the latest trend?",
            "What did I order from China?",
            "World War 2 started because of ______",
            "What am I doing when my door is looked?",
            "You are now listening to Kanye West's new album, _______",
            "What was JFK's last thoughts?",
            "You are now listening to ______",
            "In leaked government documents they found ________",
            "Who was the fifth Beatle?",
            "What was the cause of the traffic on the M4 this morning?",
            "What was the cause of the awkward silence?",
            "Next on Britain's got talent, ________ performing, ________",
            "I drink to forget _____.", 
            "When I am President of the United States, I will create the Department of _____.",
            "This season on Man vs. Wild, Bear Grylls must survive in the depths of the Amazon with only _____ and his wits.",
            "I got 99 problems but _____ ain't one.",
            "What was going to be the eleventh commandment?",
            "TSA guidelines now prohibit _____ on airplanes.",
            "I learned the hard way that you can't cheer up a grieving friend with _____.",
            "What was I arrested for?",
            "The cause of the end of the world will be _______",
            "The most common password has been reaveled to be _______",
            "Rockstar Games presents their latest triple A game ________",
            # ... (unchanged)
        ]
        self.white_cards = [
            "Your mother",
            "Friendly Fire",
            "Ronald Reagan",
            "Famine",
            "Nicolas Cage",
            "Not caring about the third world",
            "Bannananana",
            "Object permanence",
            "A moment of silence",
            "My Family",
            "Cucumber",
            "Robert J. Oppenheimer",
            "Atomic War",
            "Explosions",
            "An M. Night Shyamalan plot twist",
            "Grave robbing",
            "A time travel paradox",
            "A jar of dirt",
            "42",
            "Blue-eyes white dragon",
            "Pot of Greed",
            "The Bill of Independence",
            "Vicki",
            "Blade",
            "Poor people",
            "Consultants",
            "Her Royal Highness, Queen Elizabeth II",
            "Forgetting the Alamo",
            "Crippling debt",
            "The Trail of Tears",
            "Derek Baum",
            "Existential Dread",
            "An Existential Crisis",
            "Smaug",
            "Red Bull",
            "A perfect Borat impression",
            "Poor people",
            "AIDS",
            "The Fall of the Roman Empire",
            "Watergate",
            "Waterboarding at Guantánamo Bay",
            "Pretending to care",
            "Hot people",
            "American Gladiators",
            "Public ridicule",
            "George Bush",
            "Aubergine",
            "Gerbil",
            "Rabbits foot",
            "Grandma",
            "Mommy",
            "Daddy",
            "Peter Griffin",
            "AXE Body Spray",
            "Judge Judy",
            "Stranger danger",
            "The Blood of Christ",
            "A Bop It",
            "Horrifying laser hair removal accident",
            "Charlie's Terraria addiction",
            "Lip biting",
            "Making car noises while pushing the shopping trolley around",
            "New Age music",
            "Commiting a hit and run",
            "Drinking printer ink",
            "Paint thinner",
            "Retinas",
            "Duran Duran",
            "Josh Hutcherson",
            "Slovakia",
            "Women",
            "Weezer",
            "Firefox",
            "Battling goblins",
            "William Henry Gates III",
            "A quick getaway",
            "GTA 7",
            "A poorly made cup of tea",
            "The fabric of reality",
            "Wheese Cheels",

            # ... (unchanged)
        ]

    def draw_black_card(self):
        return random.choice(self.black_cards)

    def draw_white_cards(self, num_cards):
        return random.sample(self.white_cards, num_cards)

    def play_round(self):
        black_card = self.draw_black_card()
        print(f"\nBlack Card: {black_card}")

        num_players = self.get_valid_player_count()

        player_responses = {}

        for player in range(1, num_players + 1):
            white_cards = self.draw_white_cards(self.max_hand_size)
            print(f"\nPlayer {player}'s White Cards: {white_cards}")

            chosen_card = self.get_player_choice(player, white_cards)
            player_responses[player] = chosen_card

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

    def get_player_choice(self, player, white_cards):
        while True:
            try:
                print(f"\nChoose a card for Player {player}:")
                for i, card in enumerate(white_cards, start=1):
                    print(f"{i}. {card}")
                choice_index = int(input("Enter the number of your choice: "))
                if 1 <= choice_index <= len(white_cards):
                    return white_cards[choice_index - 1]
                else:
                    print("Invalid choice. Please enter a number within the given range.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    game = CardsAgainstHumanity()

    for round_num in range(1, game.max_rounds + 1):
        print(f"\n--- Round {round_num} ---")
        game.play_round()

        play_again = input("Do you want to play another round? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break
