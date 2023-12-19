#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

class CardsAgainstHumanity {
private:
    std::vector<std::string> blackCards;
    std::vector<std::string> whiteCards;

public:
    CardsAgainstHumanity() {
        blackCards = {
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
         
            // ... (remaining black cards)
        };

        whiteCards = {
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

            // ... (remaining white cards)
        };
    }

    std::string drawBlackCard() {
        srand(time(nullptr));
        int randomIndex = rand() % blackCards.size();
        return blackCards[randomIndex];
    }

    std::vector<std::string> drawWhiteCards(int numCards) {
        srand(time(nullptr));
        std::vector<std::string> drawnCards;
        for (int i = 0; i < numCards; i++) {
            int randomIndex = rand() % whiteCards.size();
            drawnCards.push_back(whiteCards[randomIndex]);
        }
        return drawnCards;
    }

    void playRound() {
        std::string blackCard = drawBlackCard();
        std::cout << "\nBlack Card: " << blackCard << std::endl;

        int numPlayers;
        std::cout << "Enter the number of players: ";
        std::cin >> numPlayers;

        if (numPlayers < 3) {
            std::cout << "You need at least 3 players to play. Try again." << std::endl;
            return;
        }

        std::vector<std::string> playerResponses(numPlayers);

        for (int player = 0; player < numPlayers; player++) {
            std::vector<std::string> whiteCards = drawWhiteCards(7);
            std::cout << "\nPlayer " << player + 1 << "'s White Cards: ";
            for (const auto& card : whiteCards) {
                std::cout << card << " ";
            }
            std::cout << std::endl;

            std::cout << "Select a card for Player " << player + 1 << ": ";
            std::cin >> playerResponses[player];
        }

        std::cout << "\nResponses:\n";
        for (int player = 0; player < numPlayers; player++) {
            std::cout << "Player " << player + 1 << ": " << playerResponses[player] << std::endl;
        }

        // Simple scoring mechanism: random player wins
        int winner = rand() % numPlayers + 1;

        std::cout << "\nPlayer " << winner << " wins this round!" << std::endl;
    }
};

int main() {
    CardsAgainstHumanity game;

    while (true) {
        game.playRound();

        std::string playAgain;
        std::cout << "Do you want to play another round? (yes/no): ";
        std::cin >> playAgain;

        if (playAgain != "yes") {
            std::cout << "Thanks for playing!" << std::endl;
            break;
        }
    }

    return 0;
}
