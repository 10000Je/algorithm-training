// no.10669: 오늘 날짜 (B5)

#include <cstdio>
#include <ctime>
using namespace std;

int main() {
    time_t timer = time(NULL);
    struct tm* t = localtime(&timer);
    
    printf("%4d-%02d-%02d\n", t->tm_year+1900, t->tm_mon+1, t->tm_mday);
    return 0;
}