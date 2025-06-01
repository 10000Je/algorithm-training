// no.10871: X보다 작은 수 (B5)

#include <cstdio>
#include <sstream>
using namespace std;

int main() {
    int n, x;
    scanf("%d %d", &n, &x);
    getchar();

    char str[int(1e6)];
    fgets(str, int(1e6), stdin);
    istringstream iss(str);
    int a[int(1e5)];
    for(int i=0; i<n; i++) {
        string buffer;
        getline(iss, buffer, ' ');
        a[i] = stoi(buffer);
    }
    for(int i=0; i<n; i++) {
        if(a[i] < x)
            printf("%d ", a[i]);
    }
    printf("\n");
    return 0;
}