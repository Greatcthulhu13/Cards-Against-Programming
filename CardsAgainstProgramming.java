import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class CardsAgainstHumanity {
    private List<String> blackCards;
    private List<String> whiteCards;

    public CardsAgainstHumanity() {
        this.blackCards = Arrays.asList(
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
        );
        this.whiteCards = Arrays.asList(
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
        );
    }

    public String drawBlackCard() {
        Random random = new Random();
        return blackCards.get(random.nextInt(blackCards.size()));
    }

    public List<String> drawWhiteCards(int numCards) {
        Random random = new Random();
        List<String> drawnCards = new ArrayList<>(whiteCards);
        for (int i = 0; i < whiteCards.size() - numCards; i++) {
            drawnCards.remove(random.nextInt(drawnCards.size()));
        }
        return drawnCards;
    }

    public void playRound() {
        String blackCard = drawBlackCard();
        System.out.println("\nBlack Card: " + blackCard);

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of players: ");
        int numPlayers = scanner.nextInt();

        if (numPlayers < 3) {
            System.out.println("You need at least 3 players to play. Try again.");
            return;
        }

        String[] playerResponses = new String[numPlayers];

        for (int player = 0; player < numPlayers; player++) {
            List<String> whiteCards = drawWhiteCards(7);
            System.out.println("\nPlayer " + (player + 1) + "'s White Cards: " + whiteCards);

            System.out.print("Select a card for Player " + (player + 1) + ": ");
            playerResponses[player] = scanner.next();
        }

        System.out.println("\nResponses:");
        for (int player = 0; player < numPlayers; player++) {
            System.out.println("Player " + (player + 1) + ": " + playerResponses[player]);
        }

        // Simple scoring mechanism: random player wins
        int winner = new Random().nextInt(numPlayers) + 1;

        System.out.println("\nPlayer " + winner + " wins this round!\n");
    }

    public static void main(String[] args) {
        CardsAgainstHumanity game = new CardsAgainstHumanity();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            game.playRound();

            System.out.print("Do you want to play another round? (yes/no): ");
            String playAgain = scanner.next().toLowerCase();
            if (!playAgain.equals("yes")) {
                System.out.println("Thanks for playing!");
                break;
            }
        }
    }
}
