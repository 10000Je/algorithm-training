// no.1966: 프린터 큐 (S3)

#include <cstdio>
#include <queue>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    for(int i=0; i<t; i++) {
        queue<pair<int, int>> que;
        int n, m;
        scanf("%d %d", &n, &m);
        for(int j=0; j<n; j++) {
            int pri;
            scanf("%d", &pri);
            que.push(make_pair(pri, j));
        }
        int cnt = 1;
        while(!que.empty()) {
            pair<int, int> cur = que.front();
            que.pop();
            bool highest = true;
            for(int j=0; j<que.size(); j++) {
                if(que.front().first > cur.first) 
                    highest = false;
                pair<int, int> tmp = que.front();
                que.pop();
                que.push(tmp);
            }
            if(highest && m!=cur.second) {
                cnt++;
            }
            if(highest && m==cur.second) {
                printf("%d\n", cnt);
                break;
            }
            if(!highest) {
                que.push(cur);
            }
        }
    }
    return 0;
}