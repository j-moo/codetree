#include <stdio.h>

int main() {
    // Please write your code here.
    int a, b, c;

    scanf("%d %d %d", &a, &b, &c);
    printf("%d", b > a && b < c ? 1 : 0);
    return 0;
}