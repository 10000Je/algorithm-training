// no.9375: 패션왕 신해빈 (S3)

#include <cstdio>
#include <vector>
#include <unordered_map>
#include <string>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    for(int i=0; i<t; i++) {
        int n;
        scanf("%d", &n);
        unordered_map<string, vector<string>> mp;
        for(int j=0; j<n; j++) {
            char name[21];
            char type[21];
            scanf("%s %s", name, type);
            mp[type].push_back(name);
        }
        int ret = 1;
        for(pair<string, vector<string>> tmp : mp) {
            ret *= tmp.second.size()+1;
        }
        ret--;
        printf("%d\n", ret);
    }    
    return 0;
}