#include <stdio.h>

int main() {
    // Please write your code here.
    int height, weight;

    scanf("%d %d", &height, &weight);

    int bmi = (10000 * weight) / (height * height);
    printf("%d\n", bmi);

    if (bmi >= 25) {
        printf("Obesity");
    };

    return 0;
}