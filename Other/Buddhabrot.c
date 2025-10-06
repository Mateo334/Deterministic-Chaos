#include <stdio.h>
#include <math.h>
int main() {
    // Open a file in write mode
    FILE *file = fopen("output.txt", "w");
    // double xstep = 0.00081; double ystep = 0.001; //3072 myslim
    double xstep = 0.0015; double ystep = 0.002;
    // double xstep = 0.00031; double ystep = 0.0004; //8000
    double dummy_var_1 = 0;
    double dummy_var_2 = 0;
    for (double i = -2; i<0.5; i+=xstep){//Need to rescale this to fit the window
        for (double j = -1; j<1; j+=ystep){
            double start_real = 0;
            double start_imag = 0;
            double dummy_var_3 = 0;
            for (int a = 0; a<100; a++){//Number of iterations before it "diverges"
                dummy_var_1 = 2*start_imag*start_real + j;
                dummy_var_2 = start_real*start_real - start_imag*start_imag + i;
                

                start_imag = dummy_var_1;
                start_real = dummy_var_2;//z**2 +c  
                dummy_var_3 = sqrt(pow(fabs(start_imag),2.0)+pow(fabs(start_real),2.0)); 
                if(dummy_var_3>2){
                    fprintf(file, "%.3f %.3f %.1d\n", i, j, a);
                    // printf(a);
                    break;
                } 
            } 
            if(dummy_var_3<2){
                fprintf(file, "%.3f %.3f %.1f\n", i, j, 100);
            } 
            // fprintf(file, "%.6f %.6f %.6f\n", i, j, fabs(start_real)+fabs(start_imag));
    }
    }
    fclose(file);
    return 0;
}
