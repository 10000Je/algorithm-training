// no.9086: 문자열 (B5)

#include <cstdio>
#include <cstring>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    getchar();

    for(int i=0; i<t; i++) {
        char tmp[1000];
        fgets(tmp, 1000, stdin);
        printf("%c%c\n", tmp[0], tmp[strlen(tmp)-2]);
    }
    return 0;
}