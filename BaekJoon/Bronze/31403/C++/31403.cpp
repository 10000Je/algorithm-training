// no.31403: A+B-C (B4)

#include <cstdio>
#include <string>
#include <cstdlib>
using namespace std;

int main() {
    int a, b, c;
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);
    string temp = to_string(a) + to_string(b);
    printf("%d\n", a+b-c);
    printf("%d\n", stoi(temp)-c);
    return 0;
}