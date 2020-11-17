/* Implementação de um filtro
Lê um arquivo binário com amostras em 16bits
Salva arquivo filtrado também em 16 bits
George
 */
#include <stdio.h>
#include <fcntl.h>
#include <io.h>

#define NSAMPLES 320 // quantidade de coef

int main() {
  FILE *in_file, *out_file;
  int i, n, n_amost;

  short entrada, saida;
  short sample[NSAMPLES];

  double dn = 0.0;
  double yn = 0.0;
  double erro = 0.0;

  //Carregando os coeficientes de um filtro
  float coef[NSAMPLES] = {
        #include "..\coefs_pa.dat" // NSAMPLES
  };

  // coeficientes para descobrir sinal
  double coef_adpt [NSAMPLES];


  /* abre os arquivos de entrada e saida */
  if ((in_file = fopen("../ruido_branco.pcm", "rb")) == NULL) {
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
    coef_adpt[i] = 0.0;
  }


  // execução do filtro
  do {

    //zera saída do filtro
    dn = 0;
    yn = 0;

    //lê dado do arquivo
    n_amost = fread( & entrada, sizeof(short), 1, in_file);
    sample[0] = entrada;

    //Convolução e acumulação DN
    for (n = 0; n < NSAMPLES; n++) {
      dn += coef[n] * sample[n];
    }

    //Convolução e acumulação YN
    for (n = 0; n < NSAMPLES; n++) {
      yn += coef_adpt[n] * sample[n];
    }

    // calculo erro
    erro = dn - yn;

    printf("erro %f\n", erro);

    for (n = 0; n < NSAMPLES; n++) { // atualiza coefs
        coef_adpt[n] = coef_adpt[n] + 2.0 * 0.000000000001 * erro * sample[n];
    }

    //desloca amostra
    for (n = NSAMPLES - 1; n > 0; n--) {
      sample[n] = sample[n - 1];
    }

    // cast para escrita
    saida = (short) erro;

    //escreve no arquivo de saída
    fwrite( & saida, sizeof(short), 1, out_file);

  } while (n_amost);

  //fecha os arquivos de entrada de saída
  fclose(out_file);
  fclose(in_file);
  return 0;
}
