
short convolve (short *ent, short *coefs,  int N)
{
	int n;
	int y = 0;

	//Convolução e acumulação
    for (n = 0; n < N; n++) {
      y += coefs[n] * ent[n];
    }

    //desloca amostra
    for (n = N - 1; n > 0; n--) {
      ent[n] = ent[n - 1];
      
    }

    
    return y >> 15;

}
