// no.10814: 나이순 정렬 (S5)

#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;

struct Person {
    int age;
    char name[101];
};

int main() {
    int n;
    scanf("%d", &n);
    Person arr[n];
    for(int i=0; i<n; i++) {
        scanf("%d %s", &(arr[i].age), arr[i].name);
    }
    stable_sort(arr, arr+n, [](Person a, Person b) {
        if(a.age < b.age) {
            return true;
        } else {
            return false;
        }
    });
    for(Person temp : arr) {
        printf("%d %s\n", temp.age, temp.name);
    }
    return 0;
}