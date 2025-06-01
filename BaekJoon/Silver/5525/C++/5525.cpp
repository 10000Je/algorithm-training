// no.5525: IOIOI (S1)

#include <cstdio>
#include <stack>
using namespace std;

char s[1'000'001];

int main() {
    int n, m;
    scanf("%d", &n);
    scanf("%d", &m);
    scanf("%s", s);
    stack<char> stk;
    int ret = 0;
    for(int i=0; i<m; i++) {
        if(s[i]=='I') {
            if(stk.empty()) {
                stk.push(s[i]);
            }
            else if(stk.top()=='O') {
                stk.push(s[i]);
            }
            else {
                while(!stk.empty())
                    stk.pop();
                stk.push(s[i]);
            }
            if(stk.size()==2*n+1) {
                ret++;
                for(int j=0; j<2; j++) {
                    stk.pop();
                }
            }
        }
        if(s[i]=='O') {
            if(!stk.empty() && stk.top()=='I') {
                stk.push(s[i]);
            }
            else if(!stk.empty() && stk.top()=='O') {
                while(!stk.empty())
                    stk.pop();
            }
        }
    }
    printf("%d\n", ret);
    return 0;
}