#include <stdio.h>

int main() {
    int sides = 6;
    int target1 = 1; // The target on the first roll
    int target2 = 4; // The target on the second roll

    // Calculate the probability
    double probability = (1.0 / sides) * (1.0 / sides);

    // Print the result with 3 decimal places
    printf("%.3lf\n", probability);

    return 0;
}

