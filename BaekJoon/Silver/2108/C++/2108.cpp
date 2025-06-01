// no.2108: 통계학 (S3)

#include <cstdio>
#include <algorithm>
#include <unordered_map>
#include <cmath>
#include <vector>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> arr;
    unordered_map<int, int> cnt;
    for(int i=0; i<n; i++) {
        int num;
        scanf("%d", &num);
        arr.push_back(num);
        if(cnt.count(num) == 0)
            cnt[num] = 1;
        else
            cnt[num]++;
    }
    sort(arr.begin(), arr.end());
    int sum = 0;
    for(int num : arr) {
        sum += num;
    }
    int avg = (int)floor((double)sum/n+0.5);
    int median = arr[n/2];
    int max = 0;
    for(pair<int, int> tmp : cnt) {
        if(tmp.second > max) {
            max = tmp.second;
        }
    }
    vector<int> modes;
    for(pair<int, int> tmp : cnt) {
        if(tmp.second == max)
            modes.push_back(tmp.first);
    }
    int mode;
    if(modes.size() == 1) {
        mode = modes[0];
    } else {
        sort(modes.begin(), modes.end());
        mode = modes[1];
    }
    int range = arr[n-1]-arr[0];
    printf("%d\n", avg);
    printf("%d\n", median);
    printf("%d\n", mode);
    printf("%d\n", range);
    return 0;
}