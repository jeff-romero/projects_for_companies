package CardGames;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Random;

public class Deck {
    protected static final int DEFAULT_DECK_LENGTH = 52;
    private ArrayList<Card> deck;
    private Random random;

    public Deck() {
        this.random = new Random();
        this.deck = new ArrayList<Card>(DEFAULT_DECK_LENGTH);

        this.fillDeck();
    }

    public Deck(int initialCapacity) {
        this.random = new Random();
        int n;
        if (initialCapacity > 0 && (initialCapacity % DEFAULT_DECK_LENGTH == 0)) {
            this.deck = new ArrayList<Card>(initialCapacity);
            n = initialCapacity;
        }
        else {
            this.deck = new ArrayList<Card>(DEFAULT_DECK_LENGTH);
            n = DEFAULT_DECK_LENGTH;
        }

        while (n > 0) {
            this.fillDeck();
            n -= DEFAULT_DECK_LENGTH;
        }
    }

    private void fillDeck() {
        for (int suit = 0; suit < Constants.SUITS.length; suit++) {
            for (int rank = 0; rank < Constants.RANKS.length; rank++) {
                this.deck.add(new Card(Constants.SUITS[suit], Constants.RANKS_STRINGS[rank], Constants.RANKS[rank]));
            }
        }
    }

    public ArrayList<Card> getDeck() {
        return this.deck;
    }

    public boolean empty() {
        return (this.deck.size() == 0) ? true : false;
    }

    public int getDeckLength() {
        return this.deck.size();
    }

    public void printDeck() {
        Iterator<Card> iterator = this.deck.iterator();
        while (iterator.hasNext()) {
            Card currentCard = iterator.next();
            System.out.println(currentCard.toString());
        }
    }

    public ArrayList<Card> swapDeck(ArrayList<Card> otherDeck) {
        if (otherDeck != null && !otherDeck.isEmpty()) {
            ArrayList<Card> temp = this.deck;
            this.deck = otherDeck;
            otherDeck = temp;
            return this.deck;
        }
        return null;
    }

    public boolean mergeDeck(ArrayList<Card> otherDeck) {
        if (otherDeck != null && !otherDeck.isEmpty()) {
            for (Card c : otherDeck) {
                this.deck.add(c);
            }
            return true;
        }
        return false;
    }

    public void shuffle() {
        for (int i = this.deck.size() - 1; i >= 1; i--) {
            int j = random.nextInt(i + 1); // 0 <= j <= i
            this.deck.add(this.deck.remove(j));
        }
    }

    public Card drawCard() {
        Card removed = null;
        if (this.deck != null && !this.deck.isEmpty()) {
            removed = this.deck.remove(random.nextInt(this.deck.size()));
        }
        return removed;
    }

    public static void main(String[] args) {
        Deck d = new Deck(416);
        d.printDeck();
        System.out.println("\n\nShuffling...");
        d.shuffle();
        System.out.println("Printing shuffled deck:");
        d.printDeck();
    }
}
