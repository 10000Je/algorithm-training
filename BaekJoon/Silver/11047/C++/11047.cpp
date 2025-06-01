// no.11047: 동전 0 (S4)

#include <cstdio>
#include <stack>
using namespace std;

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    stack<int> coins;
    for(int i=0; i<n; i++) {
        int a;
        scanf("%d", &a);
        coins.push(a);
    }
    int cnt = 0;
    while(!coins.empty()) {
        int val = coins.top();
        coins.pop();
        cnt += k/val;
        k %= val;
    }
    printf("%d\n", cnt);
    return 0;
}