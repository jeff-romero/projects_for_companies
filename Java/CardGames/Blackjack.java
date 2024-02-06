package CardGames;

import java.util.Scanner;
import java.util.Hashtable;
import java.util.InputMismatchException;
import java.util.NoSuchElementException;
import java.util.ArrayList;

public class Blackjack {
    public static Hashtable<String, Integer> getCardFrequency(ArrayList<Card> deck) {
        if (deck != null && !deck.isEmpty()) {
            Hashtable<String, Integer> frequency = new Hashtable<String, Integer>(deck.size());
            for (Card c : deck) {
                String cardKey = c.toString();
                if (!frequency.containsKey(cardKey)) {
                    frequency.put(cardKey, 1);
                }
                else {
                    frequency.replace(cardKey, frequency.get(cardKey) + 1);
                }
            }
            return frequency;
        }
        return null;
    }

    public static void printPlayerBalance() {

    }

    public static void printDeckStats(Deck dealer) {
        System.out.println("\n\nPrinting deck statistics:");
        Hashtable<String, Integer> frequencies = Blackjack.getCardFrequency(dealer.getDeck());
        // System.out.println(frequencies.keySet());
        System.out.println(frequencies.values());
    }

    public static int getTotalHandValue(ArrayList<Card> hand) {
        int val = 0;
        for (Card c : hand) {
            val += c.getRank();
        }
        return val;
    }

    public static void printHand(ArrayList<Card> hand) {
        for (Card c : hand) {
            System.out.format("%s%n", c.toString());
        }
    }

    public static void cleanup(Scanner stringScanner, Scanner intScanner) {
        System.out.println("\n\nExiting game...");
        stringScanner.close();
        intScanner.close();
    }

    public static void main(String[] args) {
        Scanner stringScanner = new Scanner(System.in);
        Scanner intScanner = new Scanner(System.in);
        int totalDeckSize = 416;
        int timesToShuffle = totalDeckSize / Deck.DEFAULT_DECK_LENGTH;
        String in = "";
        Player player = new Player();

        while (!in.equals("surrender")) {
            do {
                System.out.println("Play? (y/n)");
                try {
                    in = stringScanner.nextLine();
                }
                catch (NoSuchElementException e) {
                    in = "";
                }
                if (in != null && !in.isEmpty()) {
                    if (in.equals("n")) {
                        Blackjack.cleanup(stringScanner, intScanner);
                        return;
                    }
                    else if (in.equals("y")) {
                        break;
                    }
                }
            } while (true);

            // Initialize dealer hand and deck
            ArrayList<Card> dealerHand = new ArrayList<Card>(8);
            Deck dealer = new Deck(totalDeckSize);
            for (int i = 0; i < timesToShuffle; i++) {
                dealer.shuffle();
            }

            int bet = 0;
            do {
                System.out.format("\n\nPlayer balance: %d%n", player.getBalance());
                System.out.format("Place bet (1-%d)%n", player.getBalance());
                try {
                    bet = intScanner.nextInt();
                }
                catch (InputMismatchException e) {
                    bet = Constants.MIN_BET;
                }
                catch (NoSuchElementException e) {
                    bet = Constants.MIN_BET;
                }

                if (bet > 0 && player.getBalance() - bet >= 0 && bet <= 9999999) {
                    break;
                }
            } while (true);

            // Place bet
            player.subtractBalance(bet);
            System.out.format("Player has bet %d%n", bet);

            /**
             * Dealer trn
             *      - Deal initial hand of 2 cards to each player
             *      - Dealer deals to themselves 1 card visible to the player
             *      - WAIT do deal second card to themselves until after player action completed
             */

            /**
             * Player turn (for each player)
             *      - Objective:
             *          Win money by creating card totals higher than the dealer's hand but not
             *          exceeding 21, or by stopping at 21 and waiting if the dealer busts.
             *      - Choose:
             *          1. Hit
             *              - Draw a card
             *          2. Stand
             *              - End their turn and stop without taking a card
             *          3. Double
             *              - Double their wager, take a single card, and finish their turn
             *          4. Split
             *              - If the two cards have the same value, separate them to make two hands
             *          5. Surrender
             *              - Give up half-bet and retire from the game
             */

            /**
             * 
             */

            // Dealer turn
            System.out.println("\n\nDealer turn\n");
            int cardsToDealPlayer = 2;
            for (int i = 0; i < cardsToDealPlayer; i++) {
                Card c = dealer.drawCard();
                player.addCardToHand(c);
            }
            System.out.format("Dealer deals %d cards to player.%n", cardsToDealPlayer);
            System.out.println("\nPlayer's hand:");
            player.printHand();

            // Dealer draws their initial card
            Card c = dealer.drawCard();
            dealerHand.add(c);
            System.out.format("%nDealer draws a card: %s%n", c.toString());

            // Player turn
            System.out.println("\n\nPlayer turn\n");
            int currentHandValue = 0;
            boolean waiting = true;
            // TODO: Split and double
            if (player.hasSplit()) {

            }
            while (waiting) {
                System.out.println("Enter action (hit, stand, double, split, surrender):");
                try {
                    in = stringScanner.nextLine();
                }
                catch (NoSuchElementException e) {
                    in = "";
                }

                switch (in) {
                    case "hit":
                        System.out.println("Player hits.");
                        c = dealer.drawCard();
                        player.addCardToHand(c);
                        player.printHand();
                        currentHandValue = Blackjack.getTotalHandValue(player.getHand());
                        if (currentHandValue > Constants.WINNING_NUM) {
                            System.out.println("%nPlayer hand value: %d.%nPlayer busts.%n");
                            waiting = false;
                        }
                        else if (currentHandValue == Constants.WINNING_NUM) {
                            waiting = false;
                        }
                        break;
                    case "stand":
                        System.out.println("Player stands.");
                        waiting = false;
                        break;
                    case "double":
                        System.out.println("Player doubles.");
                        if (player.getBalance() - bet >= 0) {
                            player.subtractBalance(bet);
                        }
                        c = dealer.drawCard();
                        player.addCardToHand(c);
                        waiting = false;
                        System.out.format("\n\nPlayer balance: %d%n", player.getBalance());
                        break;
                    case "split":
                        System.out.println("Player splits.");
                        if (player.getHand().get(0).getRank() == player.getHand().get(1).getRank()) {
                            player.split();
                            waiting = false;
                        }
                        break;
                    case "surrender":
                        System.out.println("Player surrenders.");
                        int halfBet;
                        if (bet >= 2) {
                            halfBet = (int)Math.ceil(bet / 2);
                            player.subtractBalance(halfBet);
                        }
                        waiting = false;
                        System.out.format("\n\nPlayer balance: %d%n", player.getBalance());
                        break;
                    default:
                        break;
                }
            }

            if (!in.equals("surrender")) {
                // Dealer tries for win condition. Will stand on total hand value of 17.
                int dealerHandValue = 0;
                while (dealerHandValue < 17 && dealerHandValue != Constants.WINNING_NUM) {
                    c = dealer.drawCard();
                    dealerHand.add(c);
                    dealerHandValue = Blackjack.getTotalHandValue(dealerHand);
                    System.out.format("%n%nDealer draws a card: %s%n", c.toString());
                    Blackjack.printHand(dealerHand);
                    System.out.format("%nDealer total hand value: %d%n", dealerHandValue);
                }
                
                // Check player total hand value
                currentHandValue = Blackjack.getTotalHandValue(player.getHand());
                if (currentHandValue == Constants.WINNING_NUM) {
                    System.out.format("%n%nPlayer hit %d! Winning bet: %d%n", Constants.WINNING_NUM, bet);
                    player.addBalance(bet);
                }
                else if (currentHandValue < Constants.WINNING_NUM) {
                    if (currentHandValue > dealerHandValue) {
                        System.out.format("%n%nPlayer hand value: %d%nDealer hand value: %d%n%nPlayer wins! Winning bet: %d%n", currentHandValue, dealerHandValue, bet);
                        player.addBalance(bet);
                    }
                    else if (currentHandValue < dealerHandValue) {
                        System.out.format("%n%nPlayer hand value: %d%nDealer hand value: %d%n%nDealer wins.%n", currentHandValue, dealerHandValue, bet);
                    }
                }
            }

            // Clear player hand
            player.clearHand();
            System.out.println("\n");
        }
        Blackjack.cleanup(stringScanner, intScanner);
    }
}
