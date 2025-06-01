// no.30804: 과일 탕후루 (S2)

#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> fruit;
    vector<int> cnt(10, 0);
    for(int i=0; i<n; i++) {
        int s;
        scanf("%d", &s);
        fruit.push_back(s);
    }
    int l = 0;
    int r = 0;
    int ret = 0;
    cnt[fruit[0]]++;
    while(r < n) {
        int type = 0;
        for(int i=1; i<=9; i++) {
            if(cnt[i]) {
                type++;
            }
        }
        if(type > 2) {
            cnt[fruit[l]]--;
            l++;
        }
        else {
            ret = max(ret, r-l+1);
            r++;
            cnt[fruit[r]]++;
        }
    }
    printf("%d\n", ret);
    return 0;
}