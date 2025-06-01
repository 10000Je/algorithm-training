// no.1931: 회의실 배정 (G5)

#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<pair<int, int>> arr;
    for(int i=0; i<n; i++) {
        int s, e;
        scanf("%d %d", &s, &e);
        arr.push_back(make_pair(e, s));
    }
    sort(arr.begin(), arr.end());
    int last = 0;
    int cnt = 0;
    for(int i=0; i<n; i++) {
        if(arr[i].second >= last) {
            cnt++;
            last = arr[i].first;
        }
    }
    printf("%d\n", cnt);
    return 0;
}