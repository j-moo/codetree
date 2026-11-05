#include <stdio.h>

int main() {
    // Please write your code here.
    int t;

    scanf("%d", &t);

    if (t < 0) {
        printf("ice");
    } else if (t >= 100) {
        printf("vapor");
    } else {
        printf("water");
    }
    return 0;
}