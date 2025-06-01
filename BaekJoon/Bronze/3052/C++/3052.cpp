// no.3052: 나머지 (B2)

#include <cstdio>
using namespace std;

int main() {
    int count[43] = {0};
    for(int i=0; i<10; i++) {
        int num;
        scanf("%d", &num);
        count[num%42]++;
    }
    int result = 0;
    for(int i=0; i<42; i++) {
        if(count[i] >= 1)
            result++;
    }
    printf("%d\n", result);
    return 0;
}
