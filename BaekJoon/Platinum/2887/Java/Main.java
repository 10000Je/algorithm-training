// no.2887: 행성 터널 (P5)

import java.util.*;
import java.io.*;

class Main {

    static final int NO = 0;
    static final int X = 1;
    static final int Y = 2;
    static final int Z = 3;

    static final int COST = 2;

    static List<int[]> edges = new ArrayList<>(); // a, b, 가중치 (간선은 방향 상관 X)
    static int[] parent;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        List<int[]> nodes = new ArrayList<>();
        for(int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] node = new int[] {
                i, Integer.parseInt(st.nextToken()),
                Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())
            };
            nodes.add(node);
        }

        nodes.sort((a, b) -> a[X] - b[X]);
        for(int i=0; i<nodes.size()-1; i++) {
            edges.add(new int[] { nodes.get(i)[NO], nodes.get(i+1)[NO], 
                Math.abs(nodes.get(i)[X] - nodes.get(i+1)[X]) });
        }

        nodes.sort((a, b) -> a[Y] - b[Y]);
        for(int i=0; i<nodes.size()-1; i++) {
            edges.add(new int[] { nodes.get(i)[NO], nodes.get(i+1)[NO], 
                Math.abs(nodes.get(i)[Y] - nodes.get(i+1)[Y]) });
        }

        nodes.sort((a, b) -> a[Z] - b[Z]);
        for(int i=0; i<nodes.size()-1; i++) {
            edges.add(new int[] { nodes.get(i)[NO], nodes.get(i+1)[NO], 
                Math.abs(nodes.get(i)[Z] - nodes.get(i+1)[Z]) });
        }

        edges.sort(Main::compare);

        parent = new int[n];
        for(int i=0; i<n; i++) {
            parent[i] = i;
        }
    
        int total = 0;
        for(int[] edge : edges) {
            int a = edge[0];
            int b = edge[1];
            int cost = edge[2];
            if(find(a) != find(b)) {
                union(a, b);
                total += cost;
            }
        }
        System.out.println(total);
    }

    static int find(int x) {
        if(parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    static void union(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);
        parent[rootB] = rootA;
    }

    // Overflow를 막기 위해 따로 정의한 비교함수
    static int compare(int[] a, int[] b) {
        if(a[COST] > b[COST]) {
            return 1;
        }
        else if(a[COST] == b[COST]) {
            return 0;
        }
        else {
            return -1;
        }
    }

}