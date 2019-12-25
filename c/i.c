#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#define CODEMAX 1<<18
#include "intcode.h"
int main(){
	__int128_t intcode[CODEMAX], max = 0;
	FILE *f = fopen("i.9", "r");
	for (; EOF != fscanf(f, "%lld", intcode+max++); fgetc(f));

	for (int i = 0; i < 2; i++){
		__int128_t *s = calloc(CODEMAX, sizeof(__int128_t));
		memcpy(s, intcode, sizeof(__int128_t)*max);
		memset(s+max, 0, sizeof(__int128_t)*(CODEMAX-max));

		Intcode *r = instance();
		r->s = s;
		r->shouldFree = 1;
		//r->debug = 1;

		exec(r);
		printf("%lld\n", push(r, i));
		kill(r);
	}
}
