// no.11866: 요세푸스 문제 0 (S4)

#include <cstdio>
#include <queue>
using namespace std;

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    queue<int> que;
    for(int i=1; i<=n; i++) {
        que.push(i);
    }
    printf("<");
    while(!que.empty()) {
        for(int i=0; i<k-1; i++) {
            int tmp = que.front();
            que.pop();
            que.push(tmp);
        }
        if(que.size() == 1) {
            printf("%d>\n", que.front());
        } else {
            printf("%d, ", que.front());
        }
        que.pop();
    }
    return 0;
}