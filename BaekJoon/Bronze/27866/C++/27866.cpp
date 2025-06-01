// no.27866: 문자와 문자열 (B5)

#include <cstdio>
using namespace std;

int main() {
    char str[10000];
    fgets(str, 10000, stdin);
    int i;
    scanf("%d", &i);
    printf("%c\n", str[i-1]);
    return 0;
}