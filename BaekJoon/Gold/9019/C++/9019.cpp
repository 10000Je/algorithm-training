// no.9019: DSLR (G5)

#include <cstdio>
#include <queue>
#include <vector>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    for(int i=0; i<t; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        queue<int> que;
        que.push(a);
        vector<pair<int, char>> route(10'000, make_pair(-1, 0));
        route[a] = make_pair(a, 0);
        while(!que.empty()) {
            int cur = que.front();
            que.pop();
            int d = (cur*2)%10'000;
            int s = (cur == 0) ? 9999 : cur-1;
            int l = (cur*10)%10'000 + cur/1'000;
            int r = (cur/10)+(cur%10)*1'000;
            vector<pair<int, char>> nodes = {
                make_pair(d, 'D'), make_pair(s, 'S'),
                make_pair(l, 'L'), make_pair(r, 'R')
            };
            for(pair<int, char> node : nodes) {
                int next = node.first;
                char c = node.second;
                if(route[next].first != -1)
                    continue;
                route[next] = make_pair(cur, c);
                que.push(next);
            }
        }
        int loc = b;
        vector<char> ret;
        while(loc != a) {
            ret.push_back(route[loc].second);
            loc = route[loc].first;
        }
        for(vector<char>::reverse_iterator p=ret.rbegin(); p!=ret.rend(); p++) {
            printf("%c", *p);
        }
        printf("\n");
    }
}