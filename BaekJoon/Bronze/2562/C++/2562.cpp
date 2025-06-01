// no.2562: 최댓값 (B3)

#include <cstdio>
using namespace std;

int main() {
    int min = 0;
    int min_idx = 0;
    for(int i=0; i<9; i++) {
        int num;
        scanf("%d", &num);
        if(num > min) {
            min_idx = i+1;
            min = num;
        }
    }
    printf("%d\n", min);
    printf("%d\n", min_idx);
    return 0;
}