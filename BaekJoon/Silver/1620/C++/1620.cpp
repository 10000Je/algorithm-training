// no.1620: 나는야 포켓몬 마스터 이다솜 (S4)

#include <cstdio>
#include <unordered_map>
#include <string>
#include <cstdlib>
using namespace std;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    unordered_map<int, string> m1;
    unordered_map<string, int> m2;
    for(int i=1; i<=n; i++) {
        char tmp[21];
        scanf("%s", tmp);
        m1[i] = tmp;
        m2[tmp] = i;
    }
    for(int i=0; i<m; i++) {
        char tmp[21];
        scanf("%s", tmp);
        if(m2.count(tmp)==0)
            printf("%s\n", m1[atoi(tmp)].c_str());
        else
            printf("%d\n", m2[tmp]);
    }
    return 0;
}
