// no.10809: 알파벳 찾기 (B2)

#include <cstdio>
using namespace std;

int main() {
    int loc[100] = {0};
    for(int i=0; i<100; i++)
        loc[i] = -1;
    char str[101];
    fgets(str, 101, stdin);
    int idx = 0;
    while(str[idx]) {
        if(loc[str[idx]-'a'] == -1) {
            loc[str[idx]-'a'] = idx;
        }
        idx++;
    }
    for(int i=0; i<26; i++) {
        printf("%d ", loc[i]);
    }
    printf("\n");
    return 0;
}