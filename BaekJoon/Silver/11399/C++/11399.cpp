// no.11399: ATM (S4)

#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> arr;
    for(int i=0; i<n; i++) {
        int p;
        scanf("%d", &p);
        arr.push_back(p);
    }
    sort(arr.begin(), arr.end());
    vector<int> times;
    int sum = 0;
    for(int p : arr) {
        sum += p;
        times.push_back(sum);
    }
    int ret = 0;
    for(int time : times) {
        ret += time;
    }
    printf("%d\n", ret);
    return 0;
}