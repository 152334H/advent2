#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include "intcode.h"
const int8_t SIZE[] = {-1,3,3,1,1,2,2,3,3,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
Opcode instr(uint32_t n) { // n < 100000
	Opcode rtr;
	rtr.op = n%100;
	n /= 100;
	for (uint8_t i = 0; i < SIZE[rtr.op]; i++){
		rtr.md[i] = n%10;
		n /= 10;
	}
	return rtr;
}
void exec(Intcode *in) {
	while (in->s[in->i] != 99){
		Opcode code = instr(in->s[in->i]);
		//printf("code (");
		//for (int8_t j = 0; j < 4; j++) printf("%lld, ", in->s[in->i+j]);
		//printf(") op: %lld, modes: ",  code.op);
		__int128_t p[4];
		for (uint8_t j = 0; j < SIZE[code.op]; j++)
			p[j] = code.md[j] ? (code.md[j] == 2 ? in->s[in->i+j+1]+in->rb : in->i+j+1) : in->s[in->i+j+1];
		//for (int8_t j = 0; j < SIZE[code.op]; j++) printf("%lld:%lld, ", code.md[j], p[j]);
		//puts(")");
		switch(code.op){
			case 1:
				in->s[p[2]] = in->s[*p] + in->s[p[1]];
				break;
			case 2:
				in->s[p[2]] = in->s[*p] * in->s[p[1]];
				break;
			case 3:
				if (in->gotIn) {
					in->s[*p] = in->in;
					in->gotIn = 0;
				} else return; //wait until input appears
				break;
			case 4: //both 3 and 4 work because in->i isn't incremented if the function returns
				if (!in->gotOut) {
					in->gotOut = 1;
					in->out = in->s[*p];
				} else return;
				break;
			case 5:
				if (in->s[*p])
					in->i = in->s[p[1]]-SIZE[code.op]-1;
				break;
			case 6:
				if (!in->s[*p])
					in->i = in->s[p[1]]-SIZE[code.op]-1;
				break;
			case 7:
				in->s[p[2]] = in->s[*p] < in->s[p[1]];
				break;
			case 8:
				in->s[p[2]] = in->s[*p] == in->s[p[1]];
				break;
			case 9:
				in->rb += in->s[*p];
				break;
			default: printf("PANIC");
		}
		in->i += SIZE[code.op]+1;
	}
	in->run = 0;
	return;
}
_Bool input(Intcode* in, __int128_t v){
	if (in->gotIn){
		puts("ERR");
		return 1;
	}
	in->gotIn = 1;
	in->in = v;
	return 0;
}
__int128_t get(Intcode* in){
	if (!in->gotOut) return puts("ERRR");	//garbage
	in->gotOut = 0;
	return in->out;
}
__int128_t push(Intcode* in, __int128_t v){
	if (input(in,v)) return 0;	//garbage value
	exec(in);
	return get(in);
}
_Bool send(Intcode* in, __int128_t v){
	if (input(in,v)) return 1;	//garbage value
	exec(in);
}
__int128_t next(Intcode* in){
	exec(in);
	return get(in);
}
Intcode* runtime(__int128_t *s, uint32_t len){
	__int128_t *cpy = malloc((len+1)*sizeof(__int128_t));
	memcpy(cpy, s, sizeof(__int128_t)*len+1);
	s[len] = '\0'; //in case
	Intcode *in = malloc(sizeof(Intcode));
	in->s = cpy;
	in->i = in->in = in->out = in->gotIn = in->gotOut = in->rb = 0;
	in->run = in->shouldFree = 1;
	exec(in);
	return in;
}
Intcode* phaseInit(__int128_t *s, uint32_t len, __int128_t v){
	Intcode *in = runtime(s, len);
	send(in, v);
	return in;
}
void kill(Intcode* in){
	if (in->shouldFree) free(in->s);
	free(in);
}
