// no.2743: 단어 길이 재기 (B5)

#include <cstdio>
#include <string>
using namespace std;

int main() {
    char tmp[int(1e4)];
    fgets(tmp, int(1e4), stdin);
    string str = tmp;
    printf("%ld\n", str.length()-1);
    return 0;
}