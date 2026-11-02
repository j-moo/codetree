#include <stdio.h>

int main() {
    int length, width;

    scanf("%d %d", &length, &width);
    
    length += 8;
    width *= 3;

    printf("%d\n%d\n%d", length, width, length * width);

    return 0;
}