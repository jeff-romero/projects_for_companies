package CardGames;

import java.util.*;

public class Constants {
    public static final String FRONT = "front";
    public static final String BACK = "back";
    public static final String[] SUITS = {"Spade", "Diamond", "Heart", "Club"};
    public static enum Ranks {
        Two(2), Three(3), Four(4), Five(5), Six(6), Seven(7), Eight(8), Nine(9), Ten(10), Jack(10), Queen(10), King(10), Ace(11);
        private int value;

        Ranks(int value) {
            this.value = value;
        }

        public int getValue() {
            return this.value;
        }
    }
    public static final int[] RANKS = {2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11};
    public static ArrayList<Integer> RANKS_SERIALIZED = new ArrayList<Integer>(Arrays.asList(2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11));
    public static final String[] RANKS_STRINGS = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"};
    public static final int MIN_BET = 1;
    public static final int WINNING_NUM = 21;
}
