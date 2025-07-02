// no.2568: 전깃줄 - 2

import java.io.*;
import java.util.*;

class Main {

    public static final int A = 0;
    public static final int B = 1;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        List<int[]> arr = new ArrayList<>();
        for(int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            arr.add(new int[] { Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())});
        }
        arr.sort((a, b) -> a[A] - b[A]);

        int[] dp = new int[n];
        List<Integer> lis = new ArrayList<>();
        lis.add(arr.get(0)[B]);
        dp[0] = 0;
        for(int i=1; i<n; i++) {
            int idx = binarySearch(lis, arr.get(i)[B], 0, lis.size()-1);
            dp[i] = idx;
            if(idx >= lis.size()) {
                lis.add(arr.get(i)[B]);
            }
            else {
                lis.set(idx, arr.get(i)[B]);
            }
        }

        int count = lis.size();

        boolean[] check = new boolean[n];
        int max = 500_001;
        int len = count - 1;
        for(int i = n - 1; i >= 0; i--) {
            if(dp[i] == len && arr.get(i)[B] < max) {
                max = arr.get(i)[B];
                len--;
                check[i] = true;
            }
        }

        List<Integer> result = new ArrayList<>();
        for(int i=0; i<n; i++) {
            if(!check[i]) {
                result.add(arr.get(i)[A]);
            }
        }
        result.sort(null);
        
        bw.write(String.valueOf(result.size()) + '\n');
        for(int no : result) {
            bw.write(String.valueOf(no) + '\n');
        }
        bw.flush();
    }

    static int binarySearch(List<Integer> lis, int value, int left, int right) {
        if(left > right) {
            return left;
        }
        int mid = (left + right) / 2;
        if(value <= lis.get(mid)) {
            return binarySearch(lis, value, left, mid-1);
        }
        else {
            return binarySearch(lis, value, mid+1, right);
        }
    }

}