// no.9935: 문자열 폭발 (G4)

#include <cstdio>
#include <vector>
#include <cstring>
using namespace std;

char str[1'000'001];

int main() {
    scanf("%s", str);
    getchar();
    char bomb[40];
    scanf("%s", bomb);

    vector<char> stack;
    int len = strlen(bomb);
    for(int i=0; str[i]!=0; i++) {
        stack.push_back(str[i]);
        if(stack.size() >= len) {
            bool match = true;
            for(int j=0; j<len; j++) {
                if(bomb[j] != stack[stack.size()-len+j]) {
                    match = false;
                    break;
                }
            }
            if(match) {
                for(int j=0; j<len; j++)
                    stack.pop_back();
            }
        }
    }
    if(stack.empty()) {
        printf("FRULA\n");
    }
    else {
        for(char ch : stack)
            printf("%c", ch);
        printf("\n");
    }
    return 0;
}