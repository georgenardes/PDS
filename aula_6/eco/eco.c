/* Implementa��o de um filtro M�dia M�vel
L� um arquivo bin�rio com amostras em 16bits
Salva arquivo filtrado tamb�m em 16 bits
Walter vers�o 1.0
 */
#include <stdio.h>
#include <fcntl.h>
#include <io.h>


#define Fs 8000    // Freq amost
#define T1 1       // Delay time
#define T2 1.5     // Delay time
#define N1 (int)(T1*Fs)     // Delay discreto
#define N2 (int)(T2*Fs)     // Delay discreto
#define A0 (float)0.5
#define A1 (float)0.3
#define A2 (float)0.2

#define SV_FILE_NAME "result_eco.pcm"

int main() {
  FILE * in_file, * out_file;
  int i, n, n_amost;

  short entrada, saida;
  short sample[N2];

  float y = 0;

  /* abre os arquivos de entrada e saida */
  if ((in_file = fopen("sweep_100_2k.pcm", "rb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de entrada\n");
    return 0;
  }
  if ((out_file = fopen(SV_FILE_NAME, "wb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de saida\n");
    return 0;
  }

  // zera vetor de amostras
  for (i = 0; i < N2; i++) {
    sample[i] = 0;
  }

  // execu��o do filtro
  do {

    //zera sa�da do filtro
    y = 0;

    //l� dado do arquivo
    n_amost = fread( & entrada, sizeof(short), 1, in_file);
    sample[0] = entrada;

    // atrasa sinais
    y = A0 * sample[0] + A1 * sample[N1-1] + A2 * sample[N2-1];

    //desloca amostra
    for (n = N2 - 1; n > 0; n--) {
      sample[n] = sample[n - 1];
    }

    saida = (short) y;

    //escreve no arquivo de sa�da
    fwrite(&saida, sizeof(short), 1, out_file);

  } while (n_amost);

  //fecha os arquivos de entrada de sa�da
  fclose(out_file);
  fclose(in_file);
  return 0;
}
