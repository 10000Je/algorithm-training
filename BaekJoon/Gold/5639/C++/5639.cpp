// no.5639: 이진 검색 트리 (G4)

#include <cstdio>
using namespace std;

void postorder(int);
void insert(int, int);
int tree[1'000'000][2];

int main() {
    int n;
    int root = -1;
    while(scanf("%d", &n) == 1) {
        if(root == -1) {
            root = n;
            continue;
        }
        insert(root, n);
    }
    postorder(root);
    return 0;
}

void insert(int root, int val) {
    if(val < root) {
        if(tree[root][0] == 0)
            tree[root][0] = val;
        else
            insert(tree[root][0], val);
    }
    else {
        if(tree[root][1] == 0)
            tree[root][1] = val;
        else
            insert(tree[root][1], val);

    }
}

void postorder(int root) {
    if(tree[root][0] != 0)
        postorder(tree[root][0]);
    if(tree[root][1] != 0)
        postorder(tree[root][1]);
    printf("%d\n", root);
}

