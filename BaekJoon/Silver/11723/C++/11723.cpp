// no.11723: 집합 (S5)

#include <cstdio>
#include <cstring>
using namespace std;

int main() {
    int m;
    scanf("%d", &m);
    int s=0;
    for(int i=0; i<m; i++) {
        char cmd[10];
        scanf("%s", cmd);
        if(strcmp(cmd, "add")==0) {
            int x;
            scanf("%d", &x);
            s = s|(1<<x);
        }
        if(strcmp(cmd, "remove")==0) {
            int x;
            scanf("%d", &x);
            s = s&~(1<<x);
        }
        if(strcmp(cmd, "check")==0) {
            int x;
            scanf("%d", &x);
            if(s&(1<<x))
                printf("1\n");
            else
                printf("0\n");
        }
        if(strcmp(cmd, "toggle")==0) {
            int x;
            scanf("%d", &x);
            if(s&(1<<x))
                s = s&~(1<<x);
            else
                s = s|(1<<x);
        }
        if(strcmp(cmd, "all")==0) {
            s = ~s;
        }
        if(strcmp(cmd, "empty")==0) {
            s = 0;
        }
    }
    return 0;
}