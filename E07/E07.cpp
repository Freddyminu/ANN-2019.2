#include <iostream>
#include <math.h>
using namespace std;
int main(void)
{
    // Entrada
    double Num;
    // Vetores 
    double a[20][20], b, x[20];
    // Vetor de Y
    double NUMY[20] = {0.56, 2.53, 4.92, 4.04, 1.36, 5.56, 2.58, 5.67, 5.37, 0.34, 5.09, 1.55, 4.48, 3.55, 0.68};
    
    int TAM = 14;

    for (int i = 0; i <= TAM; i++)
    {
        scanf("%lf", &Num);
        for (int j = 0; j <= 15; j++)
        {
            a[i][j] = pow(Num, j);
            a[i][15] = NUMY[i];
        }
    }

    for (int j = 0; j <= TAM; j++)
    {
        for (int i = 0; i <= TAM; i++)
        {
            if (i != j)
            {
                b = a[i][j] / a[j][j];
                for (int k = 0; k <= TAM + 1; k++)
                {
                    a[i][k] = a[i][k] - b * a[j][k];
                }
            }
        }
    }

    for (int i = 0; i <= TAM; i++)
    {
        x[i] = a[i][TAM + 1] / a[i][i];
        printf("a%d = %.9lf\n", i, x[i]);
    }
}