#include <bits/stdc++.h>

int main(){

    float x1 = 1.61, x2 = 1.52;
    float Det;
    float A, B;
    int NUM = 4;
    
    printf("Iteração x1 = [%.8f,%.8f]\n",x1,x2);
    /* 
        f'(x) = 2*x1 -6*x2    f'(x) na -1 = 4*x2 6*x2  
                2*x1  4*x2                 -2*x1 2*x1
    */
    for(int i =2;i<=NUM;i++){

        A = pow(x1,2) - 3*pow(x2,2) + 5; // correto
        B = pow(x1,2) + 2*pow(x2,2) - 5; // correto

        Det = 1/( (2*x1*4*x2) - (-6*x2*2*x1) ); // correto
            
        float a11,a12,a21,a22;
        a11 = 4*x2;
        a12 = 6*x2;
        a21 = -2*x1;
        a22 = 2*x1;           

        x1 = x1 - (Det * ((a11*A)+(a12*B))); 
        x2 = x2 - (Det * ((a21*A)+(a22*B))); 

    printf("Interação x%d = [%.8f,%.8f]\n",i,x1,x2);

        
        
    }
}