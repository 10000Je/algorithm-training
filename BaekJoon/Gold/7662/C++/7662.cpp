// no.7662: 이중 우선순위 큐 (G4)

#include <cstdio>
#include <set>
#include <algorithm>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    for(int i=0; i<t; i++) {
        int k;
        scanf("%d", &k);
        multiset<int> set1;
        for(int j=0; j<k; j++) {
            char c;
            int n;
            getchar();
            scanf("%c %d", &c, &n);
            if(c == 'D') {
                if(set1.empty())
                    continue;
                if(n == 1) {
                    set<int>::iterator p = set1.end();
                    p--;
                    set1.erase(p);
                }
                else {
                    set<int>::iterator p = set1.begin();
                    set1.erase(p);
                }
            }
            else {
                set1.insert(n);
            }
        }
        if(set1.empty()) {
            printf("EMPTY\n");
        }
        else {
            set<int>::iterator b = set1.begin();
            set<int>::iterator e = set1.end();
            e--;
            printf("%d %d\n", *e, *b);
        }
    }
    return 0;
}