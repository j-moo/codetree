#include <stdio.h>

int main() {
    // Please write your code here.
    int a, b, c;

    scanf("%d %d %d", &a, &b, &c);

    int sum = a + b + c;
    int avg = sum / 3;
    int diff = sum - avg;

    printf("%d\n", sum);
    printf("%d\n", avg);
    printf("%d", diff);
    return 0;
}