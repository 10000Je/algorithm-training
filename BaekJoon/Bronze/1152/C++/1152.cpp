// no.1152: 단어의 개수 (B2)

#include <cstdio>
#include <sstream>
using namespace std;

char str[1'000'001];

int main() {
    fgets(str, 1'000'001, stdin);
    stringstream ss(str);
    string buffer;
    int count = 0;
    while(ss >> buffer) {
        count++;
    }
    printf("%d\n", count);
    return 0;
}