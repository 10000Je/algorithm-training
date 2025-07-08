// no.16566: 카드 게임

import java.util.*;
import java.io.*;

class Main {

    static int[] parent;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        parent = new int[M];
        for(int i=0; i<M; i++) {
            parent[i] = i;
        }

        int[] cards = new int[M];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<M; i++) {
            cards[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(cards);

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<K; i++) {
            int x = Integer.parseInt(st.nextToken());
            int idx = binarySearch(x, 0, M-1, cards);
            int root = find(idx);
            if(idx == M || root == -1) {
                // 더이상 카드를 낼 수 없는 상태,
                // 하지만 민수가 카드를 내지 못하는 테스트 케이스는 없음.
                return;
            }
            System.out.println(cards[root]);
            if(root == M-1) { // 가장 큰 숫자라면
                parent[root] = -1;
            }
            else {
                union(root, root + 1);
            }
        }
    }

    // cards 에서 x보다 큰 값들 중 가장 작은 값의 인덱스를 반환 (lower bound)
    static int binarySearch(int x, int left, int right, int[] cards) {
        if(left > right) {
            return left;
        }
        int mid = (left + right) / 2;
        if(x < cards[mid]) {
            return binarySearch(x, left, mid-1, cards);
        }
        else {
            return binarySearch(x, mid+1, right, cards);
        }
    }

    // 여기서 x 는 cards 의 인덱스 중 하나
    static int find(int x) {
        if(parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    // 일반적인 union-find 와는 달리, 방향이 명확해야한다.
    static void union(int source, int target) {
        int a = find(source);
        int b = find(target);
        parent[a] = b;
    }

}