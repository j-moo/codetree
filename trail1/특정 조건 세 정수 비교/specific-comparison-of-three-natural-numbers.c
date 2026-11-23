#include <stdio.h>

int main() {
    // Please write your code here.
    int a, b, c;

    scanf("%d %d %d", &a, &b, &c);
    
    if (a <= b && a <= c) {
        printf("%d ", 1);
    } else {
        printf("%d ", 0);
    }

    if (a == b && b == c) {
        printf("%d", 1);
    } else {
        printf("%d", 0);
    }
    return 0;
}