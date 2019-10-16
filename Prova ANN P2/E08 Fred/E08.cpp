#include <bits/stdc++.h>
using namespace std;

class Larange
{
public:
    static double i(double *vetX, double *vetY, int tam, int loc);
};

double Larange::i(double *vetX, double *vetY, int tam, int loc)
{

    double *newVetY = (double *)malloc(sizeof(double) * (tam - 1));

    for (int l = 0; l < tam - 1; l++)
    {
        newVetY[l] = (vetY[l + 1] - vetY[l]) / (vetX[l + 1 + loc] - vetX[l]);
        if (l == 0)
            cout << newVetY[l] << " ";
    }
    cout << endl;

    if (tam == 1)
        return newVetY[0];
    return i(vetX, newVetY, tam - 1, loc + 1);
}

int main(void)
{

    int tam;
    cin >> tam;

    double *vetX = (double *)malloc(sizeof(double) * tam);
    double *vetY = (double *)malloc(sizeof(double) * tam);

    for (int i = 0; i < tam + 1; i++)
    {
        cin >> vetX[i];
        cin >> vetY[i];
    }

    Larange::i(vetX, vetY, tam, 0);

    return 0;
}
