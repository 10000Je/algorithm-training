// no.2162: 선분 그룹 (P5)

import java.util.*;
import java.io.*;

class Main {

    static int[][] lines; // 0, 1, 2, 3: x1, y1, x2, y2
    static int[] parent;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        lines = new int[n][];
        parent = new int[n];
        for(int i=0; i<n; i++) {
            parent[i] = i;
        }

        for(int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            lines[i] = new int[] {
                Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()),
                Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())
            };
        }

        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                if(meet(lines[i], lines[j])) {
                    union(i, j);
                }
            }
        }

        int[] size = new int[n];
        for(int i=0; i<n; i++) {
            size[find(i)]++;
        }
        
        int count = 0;
        int max = 0;
        for(int i=0; i<n; i++) {
            if(size[i] > 0) {
                count++;
                max = Math.max(max, size[i]);
            }
        }

        System.out.println(count);
        System.out.println(max);
    }

    // a, b : line
    static boolean meet(int[] a, int[] b) {
        int c1 = cross(a, new int[] { a[0], a[1], b[2], b[3] });
        int c2 = cross(a, new int[] { a[0], a[1], b[0], b[1] });
        int c3 = cross(b, new int[] { b[0], b[1], a[2], a[3] });
        int c4 = cross(b, new int[] { b[0], b[1], a[0], a[1] });
        
        if(compare(c1, c2) > 0 || compare(c3, c4) > 0) {
            return false;
        }
        else if(compare(c1, c2) < 0 || compare(c3, c4) < 0) {
            return true;
        }
        else {
            if(Math.abs(max(a[0], a[2], b[0], b[2]) - min(a[0], a[2], b[0], b[2])) >
            (Math.abs(a[2] - a[0]) + Math.abs(b[2] - b[0]))) {
                return false;
            }
            else if(Math.abs(max(a[1], a[3], b[1], b[3]) - min(a[1], a[3], b[1], b[3])) >
            (Math.abs(a[3] - a[1]) + Math.abs(b[3] - b[1]))) {
                return false;
            }
            else {
                return true;
            }
        }        
    }

    static int cross(int[] a, int[] b) {
        int x1 = a[2] - a[0], y1 = a[3] - a[1];
        int x2 = b[2] - b[0], y2 = b[3] - b[1];
        return (x1 * y2) - (y1 * x2);
    }

    static int compare(int a, int b) {
        if(a == 0 || b == 0) {
            return 0;
        }
        else if((a > 0 && b > 0) || (a < 0 && b < 0)) {
            return 1;
        }
        else {
            return -1;
        }
    }

    static int max(int... nums) {
        int max = nums[0];
        for(int num : nums) {
            max = Math.max(max, num);
        }
        return max;
    }

    static int min(int... nums) {
        int min = nums[0];
        for(int num : nums) {
            min = Math.min(min, num);
        }
        return min;
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

}