#include <stdio.h>
#include <stdint.h>
#define	CODEMAX 1024
#include "intcode.h"
int main(){
	FILE *f = fopen("i.5", "r");
	int64_t intcode[CODEMAX], max = 0;
	for (; EOF != fscanf(f, "%lld", intcode+max++); fgetc(f));
	Intcode *in = runtime(intcode, max);
	input(in, 1);
	int64_t rtr; 
	while (1){
		rtr = next(in);
		printf("returned: %lld\n", rtr);
		if (!in->run) break;
	}
	kill(in);
	in = runtime(intcode, max);
	input(in, 5);
	printf("part2: %lld\n", next(in));
	kill(in);
	in = NULL;
}
