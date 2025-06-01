// no.2744: 대소문자 바꾸기 (B5)

#include <cstdio>
using namespace std;

int main() {
    char str[int(1e4)];
    fgets(str, int(1e4), stdin);
    for(int i=0; str[i]!='\n'; i++) {
        if('A'<=str[i] && str[i]<='Z') {
            printf("%c", str[i]+('a'-'A'));
        } else {
            printf("%c", str[i]-('a'-'A'));
        }
    }
    printf("\n");
    return 0;
}