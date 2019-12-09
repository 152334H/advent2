#include <stdio.h>
#include <string.h>
#include <stdint.h>
#define	CODEMAX 1024
#include "intcode.h"
int main(){
	FILE *f = fopen("i.2", "r");
	int64_t intcode[CODEMAX], max = 0;
	for (; EOF != fscanf(f, "%lld", intcode+max++); fgetc(f));
	for (int n = 0; n < 100; n++)
		for (int v = 0; v < 100; v++){
			intcode[1] = n; intcode[2] = v;
			Intcode* in = runtime(intcode, max);
			exec(in);
			if (n == 12 && v == 2) printf("part 1: %d\n", *(in->s));
			if (*(in->s) == 19690720) printf("part 2: %d\n", n*100+v);
		}
}
