// no.30047: 함수 문자열
/*
 * 분할정복 풀이.. O(N^2)? 이라서 시간초과
 */

#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int dnc(int, int);

char str[int(1e7)];

int main() {
    scanf("%s", str);
    int len = strlen(str);
    int ret = dnc(0, len-1);
    printf("%d\n", ret);
    return 0;
}

int dnc(int lptr, int rptr) {
    if(str[lptr] == 'f') {
        if(rptr-lptr < 2) {
            return -1;
        }
        int cur = __INT_MAX__;
        for(int i=lptr+1; i<rptr; i++) {
            int ret1 = dnc(lptr+1, i);
            int ret2 = dnc(i+1, rptr);
            if(ret1 == -1 || ret2 == -1) {
                continue;
            }
            else {
                return min(ret1, ret2);
            }
        }
        return -1;
    }
    if(str[lptr] == 'g') {
        if(lptr == rptr) {
            return -1;
        }
        else {
            int ret = dnc(lptr+1, rptr);
            if(ret == -1) {
                return -1;
            }
            else {
                return ret+1;
            }
        }
    }
    if(str[lptr] == 'x') {
        if(lptr != rptr) {
            return -1;
        }
        else {
            return 0;
        }
    }
    return -1;
}