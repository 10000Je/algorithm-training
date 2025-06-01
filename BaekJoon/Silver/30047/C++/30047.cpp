// no.30047: 함수 문자열 (S1)
/*
 * 체감 난이도: G5
 * 스택 해법을 떠올리는 것이 쉽지 않음.
 */

#include <cstdio>
#include <cstring>
#include <stack>
using namespace std;

char str[int(1e7)];

int main() {
    scanf("%s", str);
    stack<int> ret;
    for(int i=strlen(str)-1; i>=0; i--) {
        if(str[i] == 'x') {
            ret.push(0);
        }
        if(str[i] == 'g') {
            if(ret.empty())
                break;
            int tmp = ret.top();
            ret.pop();
            ret.push(tmp+1);
        }
        if(str[i] == 'f') {
            if(ret.empty())
                break;
            int tmp1 = ret.top();
            ret.pop();
            if(ret.empty())
                break;
            int tmp2 = ret.top();
            ret.pop();
            ret.push(min(tmp1, tmp2));
        }
    }
    if(ret.size() != 1) {
        printf("-1\n");
    }
    else {
        printf("%d\n", ret.top());
    }
    return 0;
}