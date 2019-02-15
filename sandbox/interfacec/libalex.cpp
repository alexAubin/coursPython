#include <stdio.h>
#include <math.h>

extern "C" float exponent(int n, float f)
{
    return pow(n, f);
}

extern "C" float sum(float* tab, int length)
{
    float acc = 0;
    for (int i = 0 ; i < length ; i++)
        acc += tab[i];

    return acc;
}

