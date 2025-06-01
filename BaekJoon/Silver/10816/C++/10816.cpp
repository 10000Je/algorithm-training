// no.10816: 숫자 카드 2 (S4)

#include <cstdio>
#include <unordered_map>
using namespace std;

int main() {
    int n;
    unordered_map<int, int> dict;
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        int num;
        scanf("%d", &num);
        if(dict.find(num) == dict.end()) {
            dict[num] = 1;
        } else {
            dict[num]++;
        }
    }
    int k;
    scanf("%d", &k);
    for(int i=0; i<k; i++) {
        int num;
        scanf("%d", &num);
        if(dict.find(num) == dict.end()) {
            printf("0 ");
        } else {
            printf("%d ", dict[num]);
        }
    }
    printf("\n");
    return 0;
}