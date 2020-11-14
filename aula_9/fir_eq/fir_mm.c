/* Implementa��o de um filtro
L� um arquivo bin�rio com amostras em 16bits
Salva arquivo filtrado tamb�m em 16 bits
George
 */
#include <stdio.h>
#include <fcntl.h>
#include <io.h>

#define NSAMPLES 160 // quantidade de coef

int main() {
  FILE * in_file, * out_file;
  int i, n, n_amost;

  short entrada, saida;
  short sample[NSAMPLES] = {
    0x0
  };

  float y = 0;

  // ganhos dos filtros
  float g_pb = 0.1;
  float g_pf = 0.5;
  float g_pa = 0.9;

  //Carregando os coeficientes do filtro pb
  float coef_pb[NSAMPLES] = {
        #include "..\coefs_pb_eq.dat" // NSAMPLES
  };

  //Carregando os coeficientes do filtro pb
  float coef_pf[NSAMPLES] = {
        #include "..\coefs_pf_eq.dat" // NSAMPLES
  };

  //Carregando os coeficientes do filtro pb
  float coef_pa[NSAMPLES] = {
        #include "..\coefs_pa_eq.dat" // NSAMPLES
  };

  /* abre os arquivos de entrada e saida */
  if ((in_file = fopen("../swip.pcm", "rb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de entrada\n");
    return 0;
  }
  if ((out_file = fopen("resultado_filtro_c.pcm", "wb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de saida\n");
    return 0;
  }

  // zera vetor de amostras
  for (i = 0; i < NSAMPLES; i++) {
    sample[i] = 0;
  }

  // execu��o do filtro
  do {

    //zera sa�da do filtro
    y = 0;

    //l� dado do arquivo
    n_amost = fread( & entrada, sizeof(short), 1, in_file);
    sample[0] = entrada;

    //Convolu��o e acumula��o
    for (n = 0; n < NSAMPLES; n++) {
      y += g_pb * coef_pb[n] * sample[n];
    }

    //Convolu��o e acumula��o
    for (n = 0; n < NSAMPLES; n++) {
      y += g_pf* coef_pf[n] * sample[n];
    }

    //Convolu��o e acumula��o
    for (n = 0; n < NSAMPLES; n++) {
      y += g_pa * coef_pa[n] * sample[n];
    }

    //desloca amostra
    for (n = NSAMPLES - 1; n > 0; n--) {
      sample[n] = sample[n - 1];
    }

    saida = (short) y;

    //escreve no arquivo de sa�da
    fwrite( & saida, sizeof(short), 1, out_file);

  } while (n_amost);

  //fecha os arquivos de entrada de sa�da
  fclose(out_file);
  fclose(in_file);
  return 0;
}
