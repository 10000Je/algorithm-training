// no.1474: 밑 줄

#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int main() {
    int n, m;
    vector<string> words;
    scanf("%d %d", &n, &m);
    int len = 0;
    for(int i=0; i<n; i++) {
        char str[11];
        scanf("%s", str);
        words.push_back(str);
        len += words.back().length();
    }
    vector<int> bar(n, 0);
    int cnt = (m-len)%(n-1);
    for(int i=1; i<n; i++) {
        if('a'<=words[i].at(0) && words[i].at(0)<='z') {
            if(cnt > 0) {
                bar[i]++;
                cnt--;
            }
            else {
                break;
            }
        }
    }
    for(int i=n-1; i>=0; i--) {
        if(cnt>0 && bar[i]==0) {
            bar[i]++;
            cnt--;
        }
    }
    for(int i=1; i<n; i++) {
        bar[i]+=(m-len)/(n-1);
    }
    for(int i=0; i<n; i++) {
        for(int j=0; j<bar[i]; j++) {
            printf("_");
        }
        printf("%s", words[i].c_str());
    }
    printf("\n");
    return 0;
}