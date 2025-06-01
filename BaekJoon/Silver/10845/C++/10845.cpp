// no.10845: 큐 (S4)

#include <cstdio>
#include <deque>
#include <cstring>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    deque<int> deq;
    for(int i=0; i<n; i++) {
        char inst[20];
        scanf("%s", inst);
        if(strcmp(inst, "push")==0) {
            int x;
            scanf("%d", &x);
            deq.push_back(x);
        }
        if(strcmp(inst, "pop")==0) {
            if(deq.empty()) {
                printf("-1\n");
                continue;
            }
            printf("%d\n", deq.front());
            deq.pop_front();
        }
        if(strcmp(inst, "size")==0) {
            printf("%lu\n", deq.size());
        }
        if(strcmp(inst, "empty")==0) {
            printf("%d\n", deq.empty() ? 1 : 0);
        }
        if(strcmp(inst, "front")==0) {
            if(deq.empty()) {
                printf("-1\n");
                continue;
            }
            printf("%d\n", deq.front());
        }
        if(strcmp(inst, "back")==0) {
            if(deq.empty()) {
                printf("-1\n");
                continue;
            }
            printf("%d\n", deq.back());
        }
    }
    return 0;
}