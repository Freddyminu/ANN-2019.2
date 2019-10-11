#include <bits/stdc++.h>
using namespace std;

class lagrange{
    public:
        static double i(double *vetX,double *vetY, int tam, int loc);
};

double lagrange::i(double *vetX,double *vetY,int tam, int loc){
    /*
    Vamos criar um novo vetor Y, que será um tamanho menor do anterior, ele vai
    guardar nossos novos valores(a.k.a: A,B,C,D)
    */
    double *newVetY = (double*)malloc(sizeof(double)*(tam-1));
    /*
    Esse for faz o calculo, vamos guardar A,B,C,D...etc dentro do novo vetor
    */
    for(int l=0;l<tam-1;l++){
        newVetY[l] = (vetY[l+1]-vetY[l])/(vetX[l+1+loc]-vetX[l]);
        cout << newVetY[l] << " ";
    }
    cout << endl;
    /*
    Se o vetor tiver tamanho 1, ou seja, não tem como continuar os calculos, então retornamos o último A
    */
    if(tam==1) return newVetY[0];
    return i(vetX,newVetY,tam-1, loc+1);
}

int main(void){
    /*
    Primeiramente vamos pegar o tamanho dos vetores, basicamente quantas pontos de entrada
    isso vai ser usado na criação de vetores(array) do tamanho correto
    */
    int tam;
    cin >> tam;

    /*Criação dos vetores X e Y*/
    double *vetX = (double*)malloc(sizeof(double)*tam);
    double *vetY = (double*)malloc(sizeof(double)*tam);

    /*Entrada dos valores dos pontos*/
    for(int i=0;i<tam;i++){
        cin >> vetX[i];
        cin >> vetY[i];
    }

    /*Algoritimo de lagrange*/
    lagrange::i(vetX,vetY,tam,0);

    return 0;
}
