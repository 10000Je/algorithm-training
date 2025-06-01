// no. 15686: 치킨 배달

#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;

void dfs(int, int, int);
int dist(pair<int, int>, pair<int, int>);
vector<pair<int, int>> homes;
vector<pair<int, int>> chickens;
int n, m;
int ret = -1;

int main() {
    scanf("%d %d", &n, &m);
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            int data;
            scanf("%d", &data);
            switch(data) {
                case 1:
                    homes.push_back(make_pair(i, j));
                    break;
                case 2:
                    chickens.push_back(make_pair(i, j));
                    break;
            }
        }
    }
    dfs(0, -1, 0);
    printf("%d\n", ret);
    return 0;
}

void dfs(int chosen, int last, int depth) {
    if(depth == m) {
        int total = 0;
        for(pair<int, int> home : homes) {
            int tmp = -1;
            for(size_t i=0; i<chickens.size(); i++) {
                if(!((1<<i)&chosen))
                    continue;
                if(tmp == -1 || dist(home, chickens[i]) < tmp) {
                    tmp = dist(home, chickens[i]);
                }
            }
            total += tmp;
        }
        if(ret == -1 || total < ret) {
            ret = total;
        }
        return;
    }
    for(size_t i=last+1; i<chickens.size(); i++) {
        if((1<<i)&chosen)
            continue;
        dfs((1<<i)|chosen, i, depth+1);
    }
}

int dist(pair<int, int> a, pair<int, int> b) {
    return abs(a.first-b.first) + abs(a.second-b.second);
}