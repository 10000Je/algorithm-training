// no.10773: 제로 (S4)

#include <cstdio>
#include <stack>
using namespace std;

int main() {
    int k;
    scanf("%d", &k);
    stack<int> stk;
    for(int i=0; i<k; i++) {
        int n;
        scanf("%d", &n);
        if(n==0)
            stk.pop();
        else
            stk.push(n);
    }
    int sum = 0;
    while(!stk.empty()) {
        sum += stk.top();
        stk.pop();
    }
    printf("%d\n", sum);
    return 0;
}