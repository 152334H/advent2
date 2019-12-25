#include <stdio.h>
#include <stdint.h>
#define	CODEMAX 1024
#include "intcode.h"
int main(){
	FILE *f = fopen("i.5", "r");
	__int128_t intcode[CODEMAX], max = 0;
	for (; EOF != fscanf(f, "%lld", intcode+max++); fgetc(f));
	Intcode *in = phaseInit(intcode, max, 1);
	int64_t rtr;
	while (1){
		rtr = next(in);
		if (!in->run) break;
	}
	printf("part1: %lld\n", rtr);
	kill(in);
	in = phaseInit(intcode, max, 5);
	printf("part2: %lld\n", next(in));
	kill(in);
	in = NULL;
}
