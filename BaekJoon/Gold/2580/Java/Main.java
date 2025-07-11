// no.2580: 스도쿠
import java.util.*;
import java.io.*;

class Pair {
    int r;
    int c;

    Pair(int r, int c) {
        this.r = r;
        this.c = c;
    }
}

public class Main {
    
    static int[][] board = new int[9][9];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        List<Pair> blanks = new ArrayList<>();
        for(int i=0; i<9; i++) {
            for(int j=0; j<9; j++) {
                board[i][j] = sc.nextInt();
                if(board[i][j] == 0) {
                    blanks.add(new Pair(i, j));
                }
            }
        }
        
        // 문제의 케이스는 풀 수 있는 입력만 주어짐.
        boolean isAvailable = dfs(0, blanks);
        for(int i=0; i<9; i++) {
            for(int j=0; j<9; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }

    // 백트래킹, 하나만 발견해도 되므로 얼리 리턴을 진행해야함.
    static boolean dfs(int depth, List<Pair> blanks) {
        if(depth == blanks.size()) {
            return true;
        }
        Pair loc = blanks.get(depth);
        for(int i=1; i<=9; i++) {
            if(check(i, loc)) {
                board[loc.r][loc.c] = i;
                if(dfs(depth + 1, blanks)) {
                    return true;
                }
            }
        }
        board[loc.r][loc.c] = 0;
        return false;
    }

    // 가능하면 true, 불가능하면 false
    static boolean check(int num, Pair loc) {
        int r = loc.r, c = loc.c;

        for(int i=0; i<9; i++) {
            if(board[r][i] == num) {
                return false;
            }
            if(board[i][c] == num) {
                return false;
            }
        }

        for(int i=0; i<3; i++) {
            for(int j=0; j<3; j++) {
                if(board[(r/3)*3 + i][(c/3)*3 + j] == num) {
                    return false;
                }
            }
        }
        return true;
    }

}
