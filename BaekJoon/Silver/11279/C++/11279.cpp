// no.11279: 최대 힙 (S2)

#include <cstdio>
#include <queue>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    priority_queue<int> heap;
    for(int i=0; i<n; i++) {
        int x;
        scanf("%d", &x);
        if(x==0) {
            if(heap.empty()) {
                printf("0\n");
            }
            else {
                printf("%d\n", heap.top());
                heap.pop();
            }
        }
        else {
            heap.push(x);
        }
    }
    return 0;
}