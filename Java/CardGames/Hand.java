package CardGames;

import java.util.ArrayList;

public class Hand {
    public static final int DEFAULT_HAND_LENGTH = 5;
    private ArrayList<Card> hand;

    public Hand() {
        this.hand = new ArrayList<Card>(DEFAULT_HAND_LENGTH);
    }

    public Hand(int length) {
        this.hand = new ArrayList<Card>(length);
    }

    public ArrayList<Card> getHand() {
        return this.hand;
    }

    public boolean isEmpty() {
        return this.hand.isEmpty();
    }

    public void add(Card c) {
        if (c != null) {
            this.hand.add(c);
        }
        else {
            throw new IllegalArgumentException("Cannot add null card.");
        }
    }

    public void printHand() {
        if (this.hand != null && !this.isEmpty()) {
            for (Card c : this.hand) {
                System.out.println(c.toString());
            }
        }
    }
}
