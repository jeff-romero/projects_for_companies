package CardGames;

import java.util.Comparator;

public class Card {
    private String face;
    private String suit;
    private String rankString;
    private int rank;

    public Card() {
        this.face = Constants.FRONT;
        this.suit = Constants.SUITS[0];
        this.rankString = Constants.RANKS_STRINGS[0];
        this.rank = Constants.RANKS[0];
    }

    public Card(String suit, String rankString, int rank) {
        this.face = Constants.FRONT;
        this.suit = suit;
        this.rankString = rankString;
        this.rank = rank;
    }

    public String getFace() {
        return this.face;
    }

    public String getSuit() {
        return this.suit;
    }

    public String getRankString() {
        return this.rankString;
    }

    public int getRank() {
        return this.rank;
    }

    public String flip() {
        if (this.face.equals(Constants.FRONT)) {
            this.face = Constants.BACK;
        }
        else if (this.face.equals(Constants.BACK)) {
            this.face = Constants.FRONT;
        }
        return this.face;
    }

    private void setSuit(String suit) {
        this.suit = suit;
    }

    private void setRankString(String rankString) {
        this.rankString = rankString;
    }

    private void setRank(int rank) {
        this.rank = rank;
    }

    public String toString() {
        return this.getRankString() + " of " + this.getSuit() + "s";
    }

    // FOR TESTING
    public static void main(String[] args) {
        Card c = new Card();
        System.out.println(c.toString());
    }
}
