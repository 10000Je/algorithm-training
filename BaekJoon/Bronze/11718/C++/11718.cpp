// no.11718: 그대로 출력하기 (B3)

#include <cstdio>
using namespace std;

int main() {
    char str[1000];
    while(fgets(str, 1000, stdin)) {
        printf("%s", str);
    }
    return 0;
}