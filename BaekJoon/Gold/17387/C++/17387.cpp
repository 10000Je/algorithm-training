// no.17387: 선분 교차 2 (G2)

#include <iostream>
#include <cmath>
#include <algorithm>
#include <functional>
using namespace std;

typedef long long int64;

pair<int, int> vt(pair<int, int> p1, pair<int, int> p2);

int64 product(pair<int, int> vt1, pair<int, int> vt2);

int cmp(int64 a, int64 b);

int main()
{
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    int x3, y3, x4, y4;
    cin >> x3 >> y3 >> x4 >> y4;
    
    pair<int, int> vt1 = vt(make_pair(x1, y1), make_pair(x2, y2));
    pair<int, int> vt2 = vt(make_pair(x3, y3), make_pair(x4, y4));

    int64 p1 = product(vt1, vt(make_pair(x1, y1), make_pair(x3, y3)));
    int64 p2 = product(vt1, vt(make_pair(x1, y1), make_pair(x4, y4)));
    int64 p3 = product(vt2, vt(make_pair(x3, y3), make_pair(x1, y1)));
    int64 p4 = product(vt2, vt(make_pair(x3, y3), make_pair(x2, y2)));

    if(
        (cmp(p1, p2) < 0 && cmp(p3, p4) <= 0) || 
        (cmp(p1, p2) <= 0 && cmp(p3, p4) < 0)
    )
        printf("1\n");
    else if(
        cmp(p1, p2) == 0 && cmp(p3, p4) == 0 && 
        abs(max({x1, x2, x3, x4})-min({x1, x2, x3, x4})) <= abs(x1-x2)+abs(x3-x4) && 
        abs(max({y1, y2, y3, y4})-min({y1, y2, y3, y4})) <= abs(y1-y2)+abs(y3-y4)
    )
        printf("1\n");
    else
        printf("0\n");
    return 0;
}

pair<int, int> vt(pair<int, int> p1, pair<int, int> p2)
{
    int x1 = p1.first, y1 = p1.second, x2 = p2.first, y2 = p2.second;
    return make_pair(x2-x1, y2-y1);
}

int64 product(pair<int, int> vt1, pair<int, int> vt2)
{
    int64 a = vt1.first, b = vt1.second, c = vt2.first, d = vt2.second;
    return a*d - b*c;
}

int cmp(int64 a, int64 b)
{
    if((a > 0 && b > 0) || (a < 0 && b < 0))
        return 1;
    else if(a == 0 || b == 0)
        return 0;
    else
        return -1;
}