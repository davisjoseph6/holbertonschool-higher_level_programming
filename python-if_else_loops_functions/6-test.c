#include <stdio.h>

int main() {
    for (int i = 0; i < 10; i++) {
        for (int j = i + 1; j < 10; j++) {
            putchar(i + '0');
            putchar(',');
            putchar(' ');
            putchar(j + '0');
            if (i != 8 || j != 9) {  // Don't print ", " after the last combination
                putchar(' ');
            }
        }
    }
    putchar('\n');

    return 0;
}
