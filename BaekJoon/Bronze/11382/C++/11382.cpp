// no.11382: 꼬마 정민 (B5)

#include <cstdio>
#include <sstream>
using namespace std;

int main() {
    char str[100];
    fgets(str, 100, stdin);
    istringstream iss(str);
    string buffer;
    long long sum = 0;
    while(getline(iss, buffer, ' ')) {
        sum += stoll(buffer);
    }
    printf("%lld\n", sum);
    return 0;
}
