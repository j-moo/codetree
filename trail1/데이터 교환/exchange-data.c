#include <stdio.h>

int main() {
    // Please write your code here
    int a = 5, b = 6, c = 7;
    int temp_1, temp_2;

    temp_1 = c;
    temp_2 = b;

    b = a;
    c = temp_2;
    a = temp_1;

    printf("%d\n%d\n%d", a, b, c);
    return 0;
}