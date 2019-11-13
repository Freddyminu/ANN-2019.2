#include <iostream>
#include <math.h>
#include <iomanip> 
using namespace std;

float Function(float x){
    return exp(-0.983*pow(x,2));
}

void Trapezio(float h,int N,float PointA,float PointB){
    float Aux = 0;
    int i = 0;
    long double FXARRAY[N];
    // Criando a arry de f(x)
    for(float x = PointA; x < PointB ;x += h){
        FXARRAY[i] = Function(x);
        i++;
    } 
    // Somando todos os Valores de f(x1) ate f(xn-1)
    for(int i = 1; i<N;i++){
        Aux = FXARRAY[i] + Aux;
    }
    cout << "\nIntegral Aproximada: " << setprecision(14) << (h/2*(FXARRAY[0]+(2*Aux)+FXARRAY[N])) << endl;
}

int main(){
    float PointA = -2;
    float PointB = 2;
    float h = 0.01;
    int N = (PointB - PointA)/h;

    cout << "\nNumero de Intervalos(N): " << N << endl;
    cout << "Passo(h): " << h << endl;
    cout << "Do ponto(A): "<< PointA << " Até o ponto(B): " << PointB << endl; 

    Trapezio(h,N,-2,2);

}