#include <cstdio>
#include <vector>
#include <stack>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<char> ret;
    stack<int> stk;
    int last_num = 1;
    for(int i = 0; i < n; i++) {
        int num;
        scanf("%d", &num);
        if(num >= last_num) {
            while(last_num <= num) {
                stk.push(last_num);
                ret.push_back('+');
                last_num++;
            }
        }
        if(stk.top() == num) {
            stk.pop();
            ret.push_back('-');
        } else {
            printf("NO\n");
            return 0;
        }
    }
    for(char c : ret)
        printf("%c\n", c);
    return 0;
}