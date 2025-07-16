// no.14891: 톱니바퀴

import java.util.*;
import java.io.*;

enum State {
    N, S
}

// 톱니바퀴
class Wheel {
    State[] state = new State[8];

    Wheel(String str) {
        for(int i=0; i<8; i++) {
            state[i] = (str.charAt(i) == '0') ? State.N : State.S;
        }
    }
}

public class Main {
    
    static final int N = 0;
    static final int NE = 1;
    static final int E = 2;
    static final int SE = 3;
    static final int S = 4;
    static final int SW = 5;
    static final int W = 6;
    static final int NW = 7;

    static Wheel[] arr = new Wheel[4];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        arr[0] = new Wheel(br.readLine());
        arr[1] = new Wheel(br.readLine());
        arr[2] = new Wheel(br.readLine());
        arr[3] = new Wheel(br.readLine());

        int K = Integer.parseInt(br.readLine());
        for(int i=0; i<K; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            
            int no = Integer.parseInt(st.nextToken()) - 1;
            int dir = Integer.parseInt(st.nextToken());
            if(dir == 1) {
                clock(no, new boolean[4]);
            }
            else {
                counterClock(no, new boolean[4]);
            }
        }

        int score = 0;
        if(arr[0].state[N] == State.S) {
            score += 1;
        }
        if(arr[1].state[N] == State.S) {
            score += 2;
        }
        if(arr[2].state[N] == State.S) {
            score += 4;
        }
        if(arr[3].state[N] == State.S) {
            score += 8;
        }
        System.out.println(score);
    }

    // 시계방향 회전, 이미 회전한 톱니바퀴는 회전하지 않음
    static void clock(int no, boolean[] check) {
        check[no] = true;
        switch(no) {
            case 0:
                if(connected(arr[0], arr[1]) && !check[1]) {
                    counterClock(1, check);
                }
                break;
            case 1:
                if(connected(arr[0], arr[1]) && !check[0]) {
                    counterClock(0, check);
                }
                if(connected(arr[1], arr[2]) && !check[2]) {
                    counterClock(2, check);
                }
                break;
            case 2:
                if(connected(arr[1], arr[2]) && !check[1]) {
                    counterClock(1, check);
                }
                if(connected(arr[2], arr[3]) && !check[3]) {
                    counterClock(3, check);
                }
                break;
            case 3:
                if(connected(arr[2], arr[3]) && !check[2]) {
                    counterClock(2, check);
                }
                break;
        }

        State temp = arr[no].state[N];
        arr[no].state[N] = arr[no].state[NW];
        arr[no].state[NW] = arr[no].state[W];
        arr[no].state[W] = arr[no].state[SW];
        arr[no].state[SW] = arr[no].state[S];
        arr[no].state[S] = arr[no].state[SE];
        arr[no].state[SE] = arr[no].state[E];
        arr[no].state[E] = arr[no].state[NE];
        arr[no].state[NE] = temp;
    }

    static void counterClock(int no, boolean[] check) {
        check[no] = true;
        switch(no) {
            case 0:
                if(connected(arr[0], arr[1]) && !check[1]) {
                    clock(1, check);
                }
                break;
            case 1:
                if(connected(arr[0], arr[1]) && !check[0]) {
                    clock(0, check);
                }
                if(connected(arr[1], arr[2]) && !check[2]) {
                    clock(2, check);
                }
                break;
            case 2:
                if(connected(arr[1], arr[2]) && !check[1]) {
                    clock(1, check);
                }
                if(connected(arr[2], arr[3]) && !check[3]) {
                    clock(3, check);
                }
                break;
            case 3:
                if(connected(arr[2], arr[3]) && !check[2]) {
                    clock(2, check);
                }
                break;
        }

        State temp = arr[no].state[N];
        arr[no].state[N] = arr[no].state[NE];
        arr[no].state[NE] = arr[no].state[E];
        arr[no].state[E] = arr[no].state[SE];
        arr[no].state[SE] = arr[no].state[S];
        arr[no].state[S] = arr[no].state[SW];
        arr[no].state[SW] = arr[no].state[W];
        arr[no].state[W] = arr[no].state[NW];
        arr[no].state[NW] = temp;
    }

    // 두 톱니바퀴가 접합부의 극이 다르면 true, a가 항상 왼쪽에 있다고 가정한다.
    static boolean connected(Wheel a, Wheel b) {
        return a.state[E] != b.state[W];
    }

}
