#include <stdio.h>
#include <stdlib.h>

void zeraVetor(int *vet, int tam){
    for(int i=0; i < tam; i++){
        vet[i] = 0;
    }
}

int somaTudo(int *vet, int tam){
    int resultado = 0;
    for(int i = 0; i < tam; i ++){
        resultado += vet[i];
    }
    return resultado;
}

void deslocamento(int *vet, int tam){
    for(int i = tam-1; i > 0; i--){
        vet[i] = vet[i-1];
    }
}
int main()
{
    int sample_rate = 8000;
    int media_len = 9;
    int media_buf[media_len];
    zeraVetor(media_buf, media_len);

    FILE *input;
    printf("Abrindo arquivo 1.\n");
    input = fopen("../swip.pcm", "rb");
    if(input == NULL){
        printf("Erro ao abrir input arquivo!");
        return 0;
    }

    FILE *output;
    printf("Abrindo arquivo 2.\n");
    output = fopen("media_result.pcm", "wb");
    if(output == NULL){
        printf("Erro ao criar output arquivo!");
        return 0;
    }

    // buffer para leitura
    short buff = 0;

    // tamanho do arquivo de entrada
    int TAM = 0;

    // le de dois em 2 bytes colocando valor em buff. quando acabar o inputuivo retorna 0
    while(fread(&buff, 2, 1, input) != 0){
        TAM++;
        media_buf[0] = buff;
        short m = somaTudo(media_buf, media_len)/media_len;
        fwrite(&m, 2, 1, output);
        deslocamento(media_buf, media_len);
    }

    printf("Tamanho do arquivo de entrada %d bytes\n", 2*TAM);

    fclose(input);
    fclose(output);
    return 0;
}
