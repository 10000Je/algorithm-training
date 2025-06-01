// no.2675: 문자열 반복 (B2)

#include <cstdio>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    for(int i=0; i<t; i++) {
        int r;
        char s[100];
        scanf("%d %s", &r, s);
        char result[1000];
        int j=0;
        while(s[j]) {
            for(int k=0; k<r; k++) {
                result[r*j+k] = s[j];
            }
            j++;
        }
        result[r*j] = '\0';
        printf("%s\n", result);
    }
    return 0;
}