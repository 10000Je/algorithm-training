// no.4949: 균형잡힌 세상 (S4)

#include <cstdio>
#include <stack>
#include <cstring>
using namespace std;

bool IsValidPS(const char* str);

int main() {
    char str[102];
    fgets(str, 102, stdin);
    str[strlen(str)-1] = '\0';
    while(strcmp(str, ".") != 0) {
        if(IsValidPS(str))
            printf("yes\n");
        else
            printf("no\n");
        fgets(str, 102, stdin);
        str[strlen(str)-1] = '\0';
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