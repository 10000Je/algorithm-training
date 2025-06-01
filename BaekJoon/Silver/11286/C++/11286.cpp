// no.11286: 절댓값 힙 (S1)

#include <cstdio>
#include <queue>
#include <cmath>
using namespace std;

int main() {
    priority_queue<int> minus;
    priority_queue<int> plus;
    int n;
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        int x;
        scanf("%d", &x);
        if(x>0) {
            plus.push(-x);
        }
        else if(x<0) {
            minus.push(x);
        }
        else {
            if(!minus.empty() && !plus.empty()) {
                if(abs(minus.top()) <= abs(plus.top())) {
                    printf("%d\n", minus.top());
                    minus.pop();
                }
                else {
                    printf("%d\n", -plus.top());
                    plus.pop();
                }
            }
            else if(!plus.empty()) {
                printf("%d\n", -plus.top());
                plus.pop();
            }
            else if(!minus.empty()) {
                printf("%d\n", minus.top());
                minus.pop();
            }
            else {
                printf("0\n");
            }
        }
    }
    return 0;
}