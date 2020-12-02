/* Implementação de um filtro
Lê um arquivo binário com amostras em 16bits
Salva arquivo filtrado também em 16 bits
George
 */
#include <stdio.h>
#include <cycles.h>

#define NSAMPLES 160 // quantidade de coef


extern short convolve(short *, short*, int);
extern short desloca(short *, int);

int main() {
  
  cycle_stats_t stats;
  
  CYCLES_INIT(stats);
  
  FILE * in_file, * out_file;
  int i, n, n_amost;

  short entrada, saida;
  short sample[NSAMPLES] = {
    0x0
  };

  int y_pb = 0;
  int y_pf = 0;
  int y_pa = 0;
  int y = 0;

  // ganhos dos filtros
  int g_pb = 22937; // 0.7;
  int g_pf = 16384; // 0.5
  int g_pa = 9830;  // 0.3;

  //Carregando os coeficientes do filtro pb
  short coef_pb[NSAMPLES] = {
        #include "coefs_pb_eq.dat" // NSAMPLES
  };

  //Carregando os coeficientes do filtro pb
  short coef_pf[NSAMPLES] = {
        #include "coefs_pf_eq.dat" // NSAMPLES
  };

  //Carregando os coeficientes do filtro pb
  short coef_pa[NSAMPLES] = {
        #include "coefs_pa_eq.dat" // NSAMPLES
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

  // execução do filtro
  do {

    //zera saída do filtro
    y_pb = 0;
    y_pf = 0;
    y_pa = 0;

    //lê dado do arquivo
    n_amost = fread( & entrada, sizeof(short), 1, in_file);
    sample[0] = entrada;
    
    CYCLES_START(stats);
    
    /* convolucoes */
    y_pb = convolve(sample, coef_pb, NSAMPLES);
	y_pf = convolve(sample, coef_pf, NSAMPLES);
	y_pa = convolve(sample, coef_pa, NSAMPLES);
	
	CYCLES_START(stats);
	
	/* deslocamento */
	desloca(sample, NSAMPLES);
    
    // soma as saidas
    y = g_pb*y_pb + g_pf*y_pf + g_pa*y_pa;

    saida = y >> 15;

    //escreve no arquivo de saída
    fwrite( & saida, sizeof(short), 1, out_file);

  } while (n_amost);
  
  CYCLES_PRINT(stats);

  //fecha os arquivos de entrada de saída
  fclose(out_file);
  fclose(in_file);
  return 0;
}
