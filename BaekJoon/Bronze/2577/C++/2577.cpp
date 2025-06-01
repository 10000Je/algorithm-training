// no.2577: 숫자의 개수 (B2)

#include <cstdio>
#include <string>
using namespace std;

int main() {
    int a, b, c;
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);
    string result = to_string(a*b*c);
    int count[10] = {0};
    for(int i=0; i<result.length(); i++) {
        count[result.at(i)-'0']++;
    }
    for(int i=0; i<10; i++) {
        printf("%d\n", count[i]);
    }
    return 0;
}