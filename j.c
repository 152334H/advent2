#include <stdio.h>
#include <stdint.h>
#define CODEMAX 1<<18
#include "intcode.h"
int main(){
	__int128_t intcode[CODEMAX], max = 0;
	FILE *f = fopen("i.9", "r");
	for (; EOF != fscanf(f, "%lld", intcode+max++); fgetc(f));
	Intcode *r = runtime(intcode, max);
	printf("%d\n", push(r, 1));
}
