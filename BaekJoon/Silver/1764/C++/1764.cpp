// no.1764: 듣보잡 (S4)

#include <cstdio>
#include <unordered_set>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    unordered_set<string> hear;
    unordered_set<string> see;
    for(int i=0; i<n; i++) {
        char tmp[21];
        scanf("%s", tmp);
        hear.insert(tmp);
    }
    for(int i=0; i<m; i++) {
        char tmp[21];
        scanf("%s", tmp);
        see.insert(tmp);
    }
    vector<string> hearsee;
    for(string name : hear) {
        if(see.count(name)!=0)
            hearsee.push_back(name);
    }
    sort(hearsee.begin(), hearsee.end());
    printf("%lu\n", hearsee.size());
    for(string name : hearsee)
        printf("%s\n", name.c_str());
    return 0;
}