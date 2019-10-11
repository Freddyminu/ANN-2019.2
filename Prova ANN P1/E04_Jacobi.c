#include <stdio.h>

int main(int argc, char const *argv[])
{
    float 
     x1=-0.4,x2=-4.3,x3=-3.3,x4=3.7,x5=0.2,x6=4.6,x7=1.0;
    float Aux1,Aux2,Aux3,Aux4,Aux5,Aux6,Aux7;
        for(int i=0;i<=8;i++){
            Aux1 = (2.5 + 1.5*x2 + 2.6*x3 - 0.5*x4 + 0.7*x5 + 1.5*x6 + 2.6*x7)/10.9;
            Aux2 = (+1.0*x1 - 3.2 - 2.3*x3 - 1.3*x4 - 2.0*x5 + 0.3*x6 - 0.0*x7)/9.2;
            Aux3 = (+2.4*x1 + 2.7*x2 - 4.7 - 2.3*x4 + 1.1*x5 - 0.6*x6 - 1.3*x7)/14;
            Aux4 = (+1.4*x1 + 2.1*x2 + 2.2*x3 - 5.0 + 2.4*x5 + 2.2*x6 + 0.4*x7)/17.9;
            Aux5 = (-1.9*x1 - 2.0*x2 - 2.7*x3 - 1.4*x4 + 1.1 - 1.5*x6 - 1.9*x7)/14.3;
            Aux6 = (-2.5*x1 - 1.7*x2 - 2.8*x3 + 1.6*x4 + 0.2*x5 - 0.1 - 2.5*x7)/11.9;
            Aux7 = (-1.2*x1 - 1.7*x2 - 2.8*x3 - 1.3*x4 + 2.6*x5 + 1.0*x6 + 0.6)/11.1;
            x1 = Aux1;
            x2 = Aux2;
            x3 = Aux3;
            x4 = Aux4;
            x5 = Aux5;
            x6 = Aux6;
            x7 = Aux7;
            printf("\n\nIteracao: %d", i+2);
            printf("\nx1: %.8f\nx2: %.8f\nx3: %.8f\nx4: %.8f\nx5: %.8f\nx6: %.8f\nx7: %.8f\n", Aux1,Aux2,Aux3,Aux4,Aux5,Aux6,Aux7);        
        }
    return 0;
}
