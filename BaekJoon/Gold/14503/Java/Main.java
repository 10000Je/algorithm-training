// no.14503: 로봇 청소기 (G5)

import java.util.*;
import java.io.*;

enum DIR {
    UP, DOWN, LEFT, RIGHT
}

enum STATE {
    CLEAN, UNCLEAN, WALL
}

class Person {
    static final int UP = 0;
    static final int RIGHT = 1;
    static final int DOWN = 2;
    static final int LEFT = 3;
    
    int r;
    int c;
    DIR dir;

    void setDir(int dir) {
        switch(dir) {
            case UP:
                this.dir = DIR.UP;
                break;
            case DOWN:
                this.dir = DIR.DOWN;
                break;
            case LEFT:
                this.dir = DIR.LEFT;
                break;
            case RIGHT:
                this.dir = DIR.RIGHT;
                break;
            default:
                break;
        }
    }
}

public class Main {
    
    static STATE[][] board; // 청소가 되어있으면 true, 아니면 false

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        Person cleaner = new Person();
        cleaner.r = Integer.parseInt(st.nextToken());
        cleaner.c = Integer.parseInt(st.nextToken());
        cleaner.setDir(Integer.parseInt(st.nextToken()));
        
        board = new STATE[N][M];
        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++) {
                int state = Integer.parseInt(st.nextToken());
                board[i][j] = (state == 0) ? STATE.UNCLEAN : STATE.WALL;
            }
        }

        int count = 0;
        while(true) {
            if(board[cleaner.r][cleaner.c] == STATE.UNCLEAN) {
                count++;
                board[cleaner.r][cleaner.c] = STATE.CLEAN;
            }
            if(check(cleaner)) {
                rotateAndMove(cleaner);
            }
            else {
                if(!tryBack(cleaner)) {
                    break;
                }
            }
        }
        System.out.println(count);
    }

    // 청소되지 않은 빈 칸이 있으면 true, 없으면 false
    static boolean check(Person cleaner) {
        if(board[cleaner.r - 1][cleaner.c] == STATE.UNCLEAN) {
            return true;
        }
        if(board[cleaner.r + 1][cleaner.c] == STATE.UNCLEAN) {
            return true;
        }
        if(board[cleaner.r][cleaner.c - 1] == STATE.UNCLEAN) {
            return true;
        }
        if(board[cleaner.r][cleaner.c + 1] == STATE.UNCLEAN) {
            return true;
        }
        return false;
    }

    // 후진에 실패하면 false, 성공하면 true
    static boolean tryBack(Person cleaner) {
        switch(cleaner.dir) {
            case UP:
                if(board[cleaner.r + 1][cleaner.c] == STATE.WALL) {
                    return false;
                }
                cleaner.r++;
                break;
            case DOWN:
                if(board[cleaner.r - 1][cleaner.c] == STATE.WALL) {
                    return false;
                }
                cleaner.r--;
                break;
            case LEFT:
                if(board[cleaner.r][cleaner.c + 1] == STATE.WALL) {
                    return false;
                }
                cleaner.c++;
                break;
            case RIGHT:
                if(board[cleaner.r][cleaner.c - 1] == STATE.WALL) {
                    return false;
                }
                cleaner.c--;
                break;
        }
        return true;
    }

    // 반시계 방향으로 90도 회전 후 청소되어 있지 않으면 앞으로 이동
    static void rotateAndMove(Person cleaner) {
        switch(cleaner.dir) {
            case UP:
                cleaner.dir = DIR.LEFT;
                if(board[cleaner.r][cleaner.c - 1] == STATE.UNCLEAN) {
                    cleaner.c--;
                }
                break;
            case LEFT:
                cleaner.dir = DIR.DOWN;
                if(board[cleaner.r + 1][cleaner.c] == STATE.UNCLEAN) {
                    cleaner.r++;
                }
                break;
            case DOWN:
                cleaner.dir = DIR.RIGHT;
                if(board[cleaner.r][cleaner.c + 1] == STATE.UNCLEAN) {
                    cleaner.c++;
                }
                break;
            case RIGHT:
                cleaner.dir = DIR.UP;
                if(board[cleaner.r - 1][cleaner.c] == STATE.UNCLEAN) {
                    cleaner.r--;
                }
                break;
        }
    }

}
