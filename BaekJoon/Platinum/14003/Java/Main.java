// no.14003: 가장 긴 증가하는 부분 수열 5

import java.util.*;
import java.io.*;

class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] A = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        int[] dp = new int[n];
        List<Integer> lis = new ArrayList<>();
        lis.add(A[0]);
        dp[0] = 0;
        for(int i=1; i<n; i++) {
            int idx = binarySearch(A[i], 0, lis.size()-1, lis);
            dp[i] = idx;
            if(idx >= lis.size()) {
                lis.add(A[i]);
            }
            else {
                lis.set(idx, A[i]);
            }
        }

        int max = 1_000_000_001;
        int len = lis.size() - 1;
        List<Integer> result = new ArrayList<>();
        for(int i = n - 1; i >= 0; i--) {
            if(dp[i] == len && A[i] < max) {
                result.add(A[i]);
                max = A[i];
                len--;
            }
        }
        result.sort((a, b) -> a - b);

        int count = result.size();
        System.out.println(count);
        for(int num : result) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    // data 가 lis 배열 어디에 삽입되어야 하는지 index를 반환
    static int binarySearch(int data, int left, int right, List<Integer> lis) {
        if(left > right) {
            return left;
        }
        int mid = (left + right) / 2;
        if(data <= lis.get(mid)) {
            return binarySearch(data, left, mid - 1, lis);
        }
        else {
            return binarySearch(data, mid + 1, right, lis);
        }
    }

}