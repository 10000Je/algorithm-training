// no.11651: 좌표 정렬하기 2 (S5)

#include <cstdio>
#include <algorithm>
using namespace std;

struct Point {
    int x;
    int y;
};

int main() {
    int n;
    scanf("%d", &n);
    Point* arr = new Point[n];
    for(int i=0; i<n; i++) {
        scanf("%d %d", &(arr[i].x), &(arr[i].y));
    }
    sort(arr, arr+n, [](Point a, Point b) {
        if(a.y < b.y) {
            return true;
        } else if(a.y == b.y) {
            if(a.x < b.x) {
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    });
    for(int i=0; i<n; i++) {
        printf("%d %d\n", arr[i].x, arr[i].y);
    }
    delete []arr;
    return 0;
}