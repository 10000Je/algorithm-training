// no.1802: 종이 접기 (S1)

#include <cstdio>
#include <cstring>
using namespace std;

bool fold(const char*, int, int);

int main() {
    int t;
    scanf("%d", &t);
    for(int i=0; i<t; i++) {
        char str[3000];
        scanf("%s", str);
        int len = strlen(str);
        int l=0, r=len-1;
        bool ret = fold(str, l, r);
        if(ret)
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}

bool fold(const char* str, int l, int r) {
    if(l==r)
        return true;
    bool ret = true;
    int lptr = l, rptr = r;
    while(lptr < rptr) {
        if(str[lptr]==str[rptr]) {
            ret = false;
            break;
        }
        lptr++;
        rptr--;
    }
    if(ret) {
        return fold(str, l, r/2-1);
    }
    else {
        return false;
    }
}