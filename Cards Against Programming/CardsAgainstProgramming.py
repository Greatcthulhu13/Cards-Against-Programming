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
    def __init__(self):
        self.max_hand_size = 10
        self.min_players = 3
        self.max_rounds = 5

        self.black_cards = [
            ("I never truly understood ___ until I encountered ___.", 2),
            "What's that smell?",
            "In an attempt to reach a wider audience, the Smithsonian Museum of Natural History has opened an interactive exhibit on ___.",
            "In its new tourism campaign, Detroit proudly proclaims that it has finally eliminated _____.",
            ("_____ is a slippery slope that leads to _____.", 2),
            ("In M. Night Shyamalan's new movie, Bruce Willis discovers that _____ had really been _____ all along.", 2),
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
            ("ITV 3 presents _____, the story of _____.", 2),
            "And I would have gotten away with it, too, if it hadn't been for _____.",
            "What's a girl's best friend?",
            "Major League Baseball has banned _____ for giving players an unfair advantage.",
            ("And the Academy Award for _____ goes to _____.", 2),
            "BILLY MAYS HERE FOR _____!",
            ("Rumor has it that Vladimir Putin's favorite dish is _____ stuffed with _____.", 2),
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
            ("In a world ravaged by _____, our only solace is _____.", 2),
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
            ("Next on Britain's got talent, ________ performing, ________", 2),
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
            "This week on Doctor Who, the Doctor will battle ________",
            ("_______ at Christmas?! ________ has it all up next on BBC One!", 2),
            "The main cause of slavery was _________",
            "What did I find in my second-hand closet?",
            "The main cause of death in the 18th Century was ________",
            "___________. The new fragrance for men",
            "___________. The new fragrance for women",
            "What did they find in Prince Andrews basement?",
            "_________. A new Netflix Original",
            "And the Grammy goes to ________",
            "And the Oscar goes to _________",
            ("Next up on WWE: ________ vs. _______", 2),
            "A new sport called _______, will be featured in the 2024 Olympics",
            "If I was a muscian my stage name would be ________",
            "If I was a singer my debut album would be called _________",
            "Who is the next James Bond?",
            "Who is the next Doctor, in Doctor Who?",
            ("A _______ a day keeps the _______ away", 2),
            "_________ is the best gift someone can give",
            "_________ is the worst gift someone can give",

            # Add more as you see fit
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
            "People",
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
            "The War on Drugs",
            "Plagerism",
            "A nice holiday at Tiananmnen Square in 1989",
            "Alcholism",
            "A scarily accurate Lois Griffin impression",
            "William Shatner's music career",
            "Radiohead's performance at the MTV Beach House",
            "Walter White",
            "A minor spelling error",
            "Everybody by Backstreet Boys",
            "A Yoko Ono concert",
            "North Korea",
            "Laughing at the name Zedong",
            "Mark David Chapman",
            "Doing "here comes the aeroplane" on September 12th 2001",
            "Stealing the glass from the pub",
            "A jaunty tune",
            "Dinner with Jay-Z",
            "Stalking people",
            "An Adam Sandler movie",
            # Add more as you see fit
        ]

    def draw_black_card(self):
        chosen_card = random.choice(self.black_cards)
        if isinstance(chosen_card, tuple):
            return chosen_card[0]
        else:
            self.black_cards.remove(chosen_card)
            return chosen_card

    def draw_white_cards(self, num_cards):
        return random.sample(self.white_cards, num_cards)

    def play_round(self):
        black_card = self.draw_black_card()
        num_answers_required = black_card[1] if isinstance(black_card, tuple) else 1
        print(f"\nBlack Card: {black_card}")

        num_players = self.get_valid_player_count()

        player_responses = {}

        for player in range(1, num_players + 1):
            white_cards = self.draw_white_cards(self.max_hand_size)

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
