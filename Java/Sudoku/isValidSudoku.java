import java.util.*;
class Solution {
    public boolean isValidRowAndCol(char[][] board, int i, int j) {
        for (int k = 1; k < board.length; k++) {
            if ((board[i][j] == board[(i + k) % board.length][j]) || (board[i][j] == board[i][(j + k) % board.length])) {
                return false;
            }
        }
        return true;
    }

    public boolean isValidSubBox(char[][] board, int r, int c) {
        ArrayList<Character> nums = new ArrayList(board.length);
        for (int i = r; i < (r + 3); i++) {
            for (int j = c; j < (c + 3); j++) {
                if (board[i][j] != '.') {
                    if (!nums.contains(board[i][j])) {
                        nums.add(board[i][j]);
                    }
                    else {
                        return false;
                    }
                }
            }
        }
        nums.clear();
        return true;
    }

    public boolean isValidSudoku(char[][] board) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                if (board[i][j] != '.') {
                    if (!isValidRowAndCol(board, i, j)) {
                        return false;
                    }
                }
            }
        }

        for (int i = 0; i < board.length; i += 3) {
            for (int j = 0; j < board.length; j += 3) {
                if (!isValidSubBox(board, i, j)) {
                    return false;
                }
            }
        }
        return true;
    }
}
