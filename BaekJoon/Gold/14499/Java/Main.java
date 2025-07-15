// no.14499: 주사위 굴리기

import java.util.*;
import java.io.*;

class Dice {
    // 현재 주사위에 칸이 어떤 위치로 배치되어 있는지 기록
    // UP, DOWN, EAST, WEST, SOUTH, NORTH
    int[] info = new int[6];
    int r, c;

    Dice(int r, int c) {
        this.r = r;
        this.c = c;
    }
}

public class Main {
    
    static final int UP = 0;
    static final int DOWN = 1;
    static final int EAST = 2;
    static final int WEST = 3;
    static final int SOUTH = 4;
    static final int NORTH = 5;

    static int[][] map;
    static int N, M;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        Dice dice = new Dice(x, y);
        map = new int[N][M];
        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<K; i++) {
            int cmd = Integer.parseInt(st.nextToken());
            switch(cmd) {
                case 1:
                    right(dice);
                    break;
                case 2:
                    left(dice);
                    break;
                case 3:
                    up(dice);
                    break;
                case 4:
                    down(dice);
                    break;
            }
        }
    }

    // UP -> NORTH, NORTH -> DOWN, DOWN -> SOUTH, SOUTH -> UP
    static void up(Dice dice) {
        if(dice.r == 0) {
            return; // 이동이 불가능
        }
        int temp = dice.info[UP];
        dice.info[UP] = dice.info[SOUTH];
        dice.info[SOUTH] = dice.info[DOWN];
        dice.info[DOWN] = dice.info[NORTH];
        dice.info[NORTH] = temp;

        dice.r--;
        touch(dice);
    }

    // UP -> SOUTH, SOUTH -> DOWN, DOWN -> NORTH, NORTH -> UP
    static void down(Dice dice) {
        if(dice.r == N-1) {
            return;
        }
        int temp = dice.info[UP];
        dice.info[UP] = dice.info[NORTH];
        dice.info[NORTH] = dice.info[DOWN];
        dice.info[DOWN] = dice.info[SOUTH];
        dice.info[SOUTH] = temp;

        dice.r++;
        touch(dice);
    }

    // UP -> WEST, WEST -> DOWN, DOWN -> EAST, EAST -> UP
    static void left(Dice dice) {
        if(dice.c == 0) {
            return;
        }
        int temp = dice.info[UP];
        dice.info[UP] = dice.info[EAST];
        dice.info[EAST]= dice.info[DOWN];
        dice.info[DOWN] = dice.info[WEST];
        dice.info[WEST] = temp;

        dice.c--;
        touch(dice);
    }

    // UP -> EAST, EAST -> DOWN, DOWN -> WEST, WEST -> UP
    static void right(Dice dice) {
        if(dice.c == M-1) {
            return;
        }
        int temp = dice.info[UP];
        dice.info[UP] = dice.info[WEST];
        dice.info[WEST] = dice.info[DOWN];
        dice.info[DOWN] = dice.info[EAST];
        dice.info[EAST] = temp;

        dice.c++;
        touch(dice);
    }

    static void touch(Dice dice) {
        if(map[dice.r][dice.c] == 0) {
            map[dice.r][dice.c] = dice.info[DOWN];
        }
        else {
            dice.info[DOWN] = map[dice.r][dice.c];
            map[dice.r][dice.c] = 0;
        }
        System.out.println(dice.info[UP]);
    }

}
