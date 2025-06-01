// no.10828: 스택 (S4)

#include <cstdio>
#include <stack>
#include <cstring>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    stack<int> stk;
    for(int i=0; i<n ;i++) {
        char inst[20];
        scanf("%s", inst);
        if(strcmp(inst, "push") == 0) {
            int val;
            scanf("%d", &val);
            stk.push(val);
        }
        if(strcmp(inst, "pop") == 0) {
            if(stk.empty()) {
                printf("-1\n");
                continue;
            }
            printf("%d\n", stk.top());
            stk.pop();
        }
        if(strcmp(inst, "size") == 0) {
            printf("%lu\n", stk.size());
        }
        if(strcmp(inst, "empty") == 0) {
            printf("%d\n", stk.empty() ? 1 : 0);
        }
        if(strcmp(inst, "top") == 0) {
            if(stk.empty()) {
                printf("-1\n");
                continue;
            }
            printf("%d\n", stk.top());
        }
    }
    return 0;
}