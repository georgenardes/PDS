/* Implementa��o de um filtro
L� um arquivo bin�rio com amostras em 16bits
Salva arquivo filtrado tamb�m em 16 bits
George
 */
#include <stdio.h>


#define NSAMPLES 4 // quantidade de coef


extern short convolve(short *, short*, int);

int main() {
  FILE * in_file, * out_file;
  int i, n, n_amost;

  short entrada, saida;
  short sample[NSAMPLES] = {
    0x0
  };

  int y = 0;

  //Carregando os coeficientes do filtro m�dia m�vel
  short coef[NSAMPLES] = {
        #include "../coefs_pb.dat" // NSAMPLES
  };

  /* abre os arquivos de entrada e saida */
  if ((in_file = fopen("../swip.pcm", "rb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de entrada\n");
    return 0;
  }
  if ((out_file = fopen("../resultado_filtro_c.pcm", "wb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de saida\n");
    return 0;
  }

  // zera vetor de amostras
  for (i = 0; i < NSAMPLES; i++) {
    sample[i] = 0;
  }

  // execu��o do filtro
  do {

    //l� dado do arquivo
    n_amost = fread( & entrada, sizeof(short), 1, in_file);
    sample[0] = entrada;

    // convolu��o
    saida = convolve(sample, coef, NSAMPLES);
    
    //escreve no arquivo de sa�da
    fwrite( & saida, sizeof(short), 1, out_file);

  } while (n_amost);

  //fecha os arquivos de entrada de sa�da
  fclose(out_file);
  fclose(in_file);
  return 0;
}
