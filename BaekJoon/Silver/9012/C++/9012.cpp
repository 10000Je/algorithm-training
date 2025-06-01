// no.9012: 괄호 (S4)

#include <cstdio>
#include <stack>
#include <cstring>
using namespace std;

bool IsValidPS(const char* str);

int main() {
    int n;
    scanf("%d", &n);
    getchar();

    char str[52];
    for(int i=0; i<n; i++) {
        fgets(str, 52, stdin);
        str[strlen(str)-1] = 0;
        if(IsValidPS(str))
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}

bool IsValidPS(const char* str) {
    stack<char> stk;
    for(int i=0; str[i] != '\0'; i++) {
        if(str[i]=='(' || str[i]=='[')
            stk.push(str[i]);
        if(str[i]==')') {
            if(stk.empty() || stk.top()!='(')
                return false;
            stk.pop();
        }
        if(str[i]==']') {
            if(stk.empty() || stk.top()!='[')
                return false;
            stk.pop();
        }
    }
    return stk.empty();
}