// no.2754: 학점계산 (B3)

#include <cstdio>
using namespace std;

int main() {
    double score;
    char str[10];
    fgets(str, 10, stdin);
    switch(str[0]) {
        case 'A':
            score = 4;
            break;
        case 'B':
            score = 3;
            break;
        case 'C':
            score = 2;
            break;
        case 'D':
            score = 1;
            break;
        default:
            printf("0.0\n");
            return 0;
    }
    switch(str[1]) {
        case '+':
            score += 0.3;
            break;
        case '-':
            score -= 0.3;
            break;
        default:
            break;
    }
    printf("%.1lf\n", score);
    return 0;
}