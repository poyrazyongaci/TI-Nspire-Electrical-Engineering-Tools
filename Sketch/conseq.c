#include <stdio.h>
#include <stdlib.h>

int * convseq(int * seq1, int,int* seq2, int);

int * convseq(int *seq1, int size1,int *seq2, int size2){
    //convolution of two sequences
    int convsize = size1 + size2 - 1;
    
    int *result = (int*)malloc(convsize*sizeof(int));
    for (int i = 0; i < convsize; i++){
        result[i] = 0;
    }
    for (int i = 0; i < size1; i++){
        for (int j = 0; j < size2; j++){
            result[i+j] += seq1[i]*seq2[j];
        }
    }

    for (int i = 0; i < convsize; i++){
        printf("%d ",result[i]);
    }
}

void main(){
    int seq1[3] = {1,2,3};
    int seq2[3] = {1,1,1};
    convseq(seq1,3,seq2,3);
}