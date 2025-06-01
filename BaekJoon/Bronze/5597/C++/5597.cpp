// no.5597: 과제 안 내신 분..? (B3)

#include <cstdio>
using namespace std;

int main() {
    bool arr[31] = {false};
    for(int i=0; i<28; i++) {
        int n;
        scanf("%d", &n);
        arr[n] = true;
    }
    for(int i=1; i<31; i++) {
        if(!arr[i])
            printf("%d\n", i);
    }
    return 0;
}