// no.2745: 진법 변환 (B2)

#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

int main() {
    char str[50];
    int b;
    scanf("%s %d", str, &b);
    int ret = 0;
    int len = strlen(str);
    for(int i=0; i<len; i++) {
        if('A'<=str[i] && str[i]<='Z') {
            ret += (str[i]-'A'+10)*int(pow(b, len-(i+1)));
        }
        else {
            ret += (str[i]-'0')*int(pow(b, len-(i+1)));
        }
    }
    printf("%d\n", ret);
    return 0;
}