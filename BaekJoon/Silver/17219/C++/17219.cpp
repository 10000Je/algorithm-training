// no.17219: 비밀번호 찾기 (S4)

#include <cstdio>
#include <unordered_map>
#include <string>
using namespace std;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    unordered_map<string, string> pw;
    for(int i=0; i<n; i++) {
        char website[21];
        char password[21];
        scanf("%s %s", website, password);
        pw[website] = password;
    }
    for(int i=0; i<m; i++) {
        char tmp[21];
        scanf("%s", tmp);
        printf("%s\n", pw[tmp].c_str());
    }
    return 0;
}