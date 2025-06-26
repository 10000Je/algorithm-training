// no.28707: 배열 정렬 (G1)

import java.util.*;
import java.io.*;

class Node implements Comparable<Node> {
    int[] v;
    int w;

    Node(int[] v, int w) {
        this.v = v;
        this.w = w;
    }

    @Override
    public int compareTo(Node other) {
        return w - other.w;
    }
}

class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] A = new int[n];
        for(int i=0; i<n; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        int m = Integer.parseInt(br.readLine());
        int[][] M = new int[m][];
        for(int i=0; i<m; i++) {
            st = new StringTokenizer(br.readLine());
            int l = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            M[i] = new int[] { l-1, r-1, c };
        }
        System.out.println(dijkstra(A, M));
    }

    static int dijkstra(int[] start, int[][] M) {
        int n = start.length;
        List<Integer> end = copy(start);
        end.sort(null);
        
        PriorityQueue<Node> heap = new PriorityQueue<>();
        Map<List<Integer>, Integer> dist = new HashMap<>();
        Set<List<Integer>> visit = new HashSet<>();
        dist.put(copy(start), 0);
        heap.add(new Node(start, dist.get(copy(start))));

        while(!heap.isEmpty()) {
            Node x = heap.remove();
            if(visit.contains(copy(x.v))) {
                continue;
            }
            visit.add(copy(x.v));
            for(int[] arr : M) {
                int[] next = new int[n];
                for(int i=0; i<n; i++) {
                    next[i] = x.v[i];
                }
                int l = arr[0], r = arr[1], c = arr[2];
                int temp = next[l];
                next[l] = next[r];
                next[r] = temp;

                if(visit.contains(copy(next))) {
                    continue;
                }
                if(!dist.containsKey(copy(next)) || 
                dist.get(copy(x.v)) + c < dist.get(copy(next))) {
                    dist.put(copy(next), dist.get(copy(x.v)) + c);
                    heap.add(new Node(next, dist.get(copy(next))));
                }
            }
        }

        return dist.containsKey(end) ? dist.get(end) : -1;
    }

    static List<Integer> copy(int[] arr) {
        List<Integer> result = new ArrayList<>(arr.length);
        for(int num : arr) {
            result.add(num);
        }
        return result;
    }

}