import java.util.*;
import java.io.*;

enum Direction {
    UP, DOWN, LEFT, RIGHT
}

class Main {

    private static final int INF = 11;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        char[][] board = new char[n][m];
        for(int i=0; i<n; i++) {
            String str = br.readLine();
            for(int j=0; j<m; j++) {
                board[i][j] = str.charAt(j);
            }
        }
        int result = dfs(0, null, board);
        System.out.println(result == INF ? -1 : result);
    }

    static int dfs(int depth, Direction dir, char[][] board) {
        if(depth > 10) {
            return INF;
        } 
        if(!check(board, 'B')) {
            return INF;
        }
        if(!check(board, 'R')) {
            return depth;
        }
        int result = INF;
        if(dir != Direction.UP)
            result = Math.min(result, dfs(depth+1, Direction.UP, up(board)));
        if(dir != Direction.DOWN)
            result = Math.min(result, dfs(depth+1, Direction.DOWN, down(board)));
        if(dir != Direction.LEFT)
            result = Math.min(result, dfs(depth+1, Direction.LEFT, left(board)));
        if(dir != Direction.RIGHT)
            result = Math.min(result, dfs(depth+1, Direction.RIGHT, right(board)));
        return result;
    }

    static boolean check(char[][] board, char color) {
        for(char[] arr : board) {
            for(char ch : arr) {
                if(ch == color) {
                    return true;
                }
            }
        }
        return false;
    }

    static char[][] up(char[][] board) {
        int n = board.length;
        int m = board[0].length;

        char[][] result = new char[n][m];
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                result[i][j] = board[i][j];
            }
        }

        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                if(!(result[i][j] == 'R' || result[i][j] == 'B')) {
                    continue;
                }
                char temp = result[i][j];
                result[i][j] = '.';
                int k = i-1;
                while(k >= 0) {
                    if(result[k][j] == '.') {
                        k--;
                    }
                    else if(result[k][j] == 'O') {
                        temp = '.';
                        break;
                    }
                    else {
                        break;
                    }
                }
                result[k+1][j] = temp;
            }
        }
        return result;
    }

    static char[][] down(char[][] board) {
        int n = board.length;
        int m = board[0].length;

        char[][] result = new char[n][m];
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                result[i][j] = board[i][j];
            }
        }

        for(int i=n-1; i>=0; i--) {
            for(int j=0; j<m; j++) {
                if(!(result[i][j] == 'R' || result[i][j] == 'B')) {
                    continue;
                }
                char temp = result[i][j];
                result[i][j] = '.';
                int k = i+1;
                while(k < n) {
                    if(result[k][j] == '.') {
                        k++;
                    }
                    else if(result[k][j] == 'O') {
                        temp = '.';
                        break;
                    }
                    else {
                        break;
                    }
                }
                result[k-1][j] = temp;
            }
        }
        return result;
    }

    static char[][] left(char[][] board) {
        int n = board.length;
        int m = board[0].length;

        char[][] result = new char[n][m];
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                result[i][j] = board[i][j];
            }
        }

        for(int j=0; j<m; j++) {
            for(int i=0; i<n; i++) {
                if(!(result[i][j] == 'R' || result[i][j] == 'B')) {
                    continue;
                }
                char temp = result[i][j];
                result[i][j] = '.';
                int k = j-1;
                while(k >= 0) {
                    if(result[i][k] == '.') {
                        k--;
                    }
                    else if(result[i][k] == 'O') {
                        temp = '.';
                        break;
                    }
                    else {
                        break;
                    }
                }
                result[i][k+1] = temp;
            }
        }
        return result;
    }

    static char[][] right(char[][] board) {
        int n = board.length;
        int m = board[0].length;

        char[][] result = new char[n][m];
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                result[i][j] = board[i][j];
            }
        }

        for(int j=m-1; j>=0; j--) {
            for(int i=0; i<n; i++) {
                if(!(result[i][j] == 'R' || result[i][j] == 'B')) {
                    continue;
                }
                char temp = result[i][j];
                result[i][j] = '.';
                int k = j+1;
                while(k < m) {
                    if(result[i][k] == '.') {
                        k++;
                    }
                    else if(result[i][k] == 'O') {
                        temp = '.';
                        break;
                    }
                    else {
                        break;
                    }
                }
                result[i][k-1] = temp;
            }
        }
        return result;
    }

}