package CardGames;

import java.util.ArrayList;

public class Player {
    // 1, 5, 10, 20, 25, 50, 100, 500, 1000
    private int balance;
    private ArrayList<Card> hand;
    private ArrayList<Card> split;

    public Player() {
        this.balance = 100;
        this.hand = new ArrayList<Card>();
        this.split = null;
    }

    public int getBalance() {
        return this.balance;
    }

    public ArrayList<Card> getHand() {
        return this.hand;
    }

    public void clearHand() {
        this.hand = new ArrayList<Card>();
        this.split = null;
    }

    public void addBalance(int value) {
        this.balance += value;
    }

    public void subtractBalance(int value) {
        this.balance -= value;
    }

    public void addCardToHand(Card c) {
        this.hand.add(c);
    }

    public void split() {
        if (this.split == null) {
            this.split = new ArrayList<Card>();
            this.split.add(this.hand.remove(this.hand.size() - 1));
        }
    }

    public boolean hasSplit() {
        return (this.split != null) ? true : false;
    }

    public void printHand() {
        for (Card c : this.hand) {
            System.out.format("%s%n", c.toString());
        }
    }
}
