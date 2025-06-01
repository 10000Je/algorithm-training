// no.8958: OX퀴즈 (B2)

#include <cstdio>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    getchar();
    for(int i=0; i<t; i++) {
        char str[100];
        fgets(str, 100, stdin);
        int score = 0;
        int point = 1;
        int idx = 0;
        while(str[idx] != '\0') {
            if(str[idx] == 'O') {
                score += point++;
            } else {
                point = 1;
            }
            idx++;
        }
        printf("%d\n", score);
    }
    return 0;
}