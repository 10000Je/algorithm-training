// no.3190: 뱀

import java.util.*;
import java.io.*;

enum STATE {
    EMPTY, SNAKE, APPLE
}

enum DIR {
    UP, DOWN, LEFT, RIGHT
}

class Pair {
    int r;
    int c;

    Pair(int r, int c) {
        this.r = r;
        this.c = c;
    }
}

class Snake {
    DIR dir;
    Pair head;
    Pair tail;

    Snake(DIR dir, Pair head, Pair tail) {
        this.dir = dir;
        this.head = head;
        this.tail = tail;
    }
}

public class Main {

    static STATE[][] board;
    static Pair[][] link;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int K = Integer.parseInt(br.readLine());

        board = new STATE[N][N];
        link = new Pair[N][N];

        for(int i=0; i<K; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int R = Integer.parseInt(st.nextToken()) - 1;
            int C = Integer.parseInt(st.nextToken()) - 1;
            board[R][C] = STATE.APPLE;
        }

        int L = Integer.parseInt(br.readLine());
        String[] rotate = new String[10_100];
        for(int i=0; i<L; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int X = Integer.parseInt(st.nextToken());
            char C = st.nextToken().charAt(0);
            rotate[X] = String.valueOf(C);
        }

        board[0][0] = STATE.SNAKE;
        Snake snake = new Snake(DIR.RIGHT, new Pair(0, 0), new Pair(0, 0));
        
        int count = 0;
        while(tryMove(snake)) {
            count++;
            if(rotate[count] == null) {
                continue;
            }
            if(rotate[count].equals("L")) {
                rotateLeft(snake);
            }
            if(rotate[count].equals("D")) {
                rotateRight(snake);
            }
        }
        count++;
        System.out.println(count);
    }

    // 이동에 실패하면 false, 성공하면 true
    static boolean tryMove(Snake snake) {
        int N = board.length;
        Pair head = snake.head;
        Pair tail = snake.tail;
        switch(snake.dir) {
            case UP:
                if(head.r == 0 || board[head.r-1][head.c] == STATE.SNAKE) {
                    return false;
                }
                link[head.r][head.c] = new Pair(head.r - 1, head.c);
                head.r--;
                break;
            case DOWN:
                if(head.r == N - 1 || board[head.r+1][head.c] == STATE.SNAKE) {
                    return false;
                }
                link[head.r][head.c] = new Pair(head.r + 1, head.c);
                head.r++; 
                break;
            case LEFT:
                if(head.c == 0 || board[head.r][head.c-1] == STATE.SNAKE) {
                    return false;
                }
                link[head.r][head.c] = new Pair(head.r, head.c - 1);
                head.c--;
                break;
            case RIGHT:
                if(head.c == N - 1 || board[head.r][head.c+1] == STATE.SNAKE) {
                    return false;
                }
                link[head.r][head.c] = new Pair(head.r, head.c + 1);
                head.c++;
                break;
        }
        if(board[head.r][head.c] != STATE.APPLE) {
            board[tail.r][tail.c] = STATE.EMPTY;
            snake.tail = link[tail.r][tail.c];
        }
        board[head.r][head.c] = STATE.SNAKE;
        return true;
    }

    static void rotateLeft(Snake snake) {
        switch(snake.dir) {
            case UP:
                snake.dir = DIR.LEFT;
                break;
            case LEFT:
                snake.dir = DIR.DOWN;
                break;
            case DOWN:
                snake.dir = DIR.RIGHT;
                break;
            case RIGHT:
                snake.dir = DIR.UP;
                break;
        }
    }

    static void rotateRight(Snake snake) {
        switch(snake.dir) {
            case UP:
                snake.dir = DIR.RIGHT;
                break;
            case RIGHT:
                snake.dir = DIR.DOWN;
                break;
            case DOWN:
                snake.dir = DIR.LEFT;
                break;
            case LEFT:
                snake.dir = DIR.UP;
                break;
        }
    }

}
