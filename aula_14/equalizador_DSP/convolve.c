
short convolve (short *ent, short *coefs,  int N)
{
	int n;
	int y = 0;

	//Convolução e acumulação
    for (n = 0; n < N; n++) {
      y += coefs[n] * ent[n];
    }
    
    return y >> 15;

}


void desloca (short *ent, int N)
{
	int n;
	
	//desloca amostra
    for (n = N - 1; n > 0; n--) {
      ent[n] = ent[n - 1];      
    }
}
