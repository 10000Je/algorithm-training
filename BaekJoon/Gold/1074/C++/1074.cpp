// no.1074: Z (G5)

#include <cstdio>
#include <utility>
#include <cmath>
#include <vector>
using namespace std;

int dnc(int, pair<int, int>, pair<int, int>, int);

int main() {
    int n, r, c;
    scanf("%d %d %d", &n, &r, &c);
    int ret = dnc(n, make_pair(0, 0), make_pair(r, c), 0);
    printf("%d\n", ret);
    return 0;
}

int dnc(int n, pair<int, int> loc, pair<int, int> dest, int ret) {
    if(n==0) {
        if(loc==dest)
            return ret;
    }
    else {
        int r=dest.first, c=dest.second;
        int a=loc.first, b=loc.second;
        if(r<a+pow(2, n-1) && c<b+pow(2, n-1)) {
            return dnc(n-1, loc, dest, ret);
        }
        if(r<a+pow(2, n-1) && c>=b+pow(2, n-1)) {
            return dnc(n-1, make_pair(a, b+pow(2, n-1)), dest, ret+pow(2, 2*n-2));
        }
        if(r>=a+pow(2, n-1) && c<b+pow(2, n-1)) {
            return dnc(n-1, make_pair(a+pow(2, n-1), b), dest, ret+2*pow(2, 2*n-2));
        }
        if(r>=a+pow(2, n-1) && c>=b+pow(2, n-1)) {
            return dnc(n-1, make_pair(a+pow(2, n-1), b+pow(2, n-1)), dest, ret+3*pow(2, 2*n-2));
        }
    }
    return ret;
}