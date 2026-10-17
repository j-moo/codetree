#include <stdio.h>

int main() {
    // Please write your code here
    int a = 2, b = 5;
    int temp;

    temp = a;
    a = b;
    b = temp;

    printf("%d\n%d", a, b);
    return 0;
}