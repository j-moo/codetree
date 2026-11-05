#include <stdio.h>
#include <stdbool.h>

int main() {
    // Please write your code here.
    int a_math, a_english;
    int b_math, b_english;

    scanf("%d %d %d %d", &a_math, &a_english, &b_math, &b_english);

    if (a_math > b_math && a_english > b_english) {
        printf("%d", true);
    } else {
        printf("%d", false);
    }
    return 0;
}