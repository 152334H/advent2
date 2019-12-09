#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#define	CODEMAX 1024
#define MAXARGS	3
const int8_t SIZE[] = {-1,3,3,1,1,2,2,3,3,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
typedef struct Opcode {
	int8_t op;
	int8_t md[MAXARGS];
} Opcode;
Opcode instr(int64_t n) {
	Opcode rtr;
	rtr.op = n%100;
	n /= 100;
	for (int8_t i = 0; i < SIZE[rtr.op]; i++){
		rtr.md[i] = n%10;
		n /= 10;
	}
	return rtr;
}
typedef struct Intcode {
	int64_t *s;
	int64_t in;
	int64_t out;
	int32_t i; //max index should be containable in a 32 bit int
	_Bool gotIn;
	_Bool gotOut;
	_Bool run;
	_Bool shouldFree;
} Intcode;
void exec(Intcode *in) {
	int32_t rb = 0;
	while (in->s[in->i] != 99){
		Opcode code = instr(in->s[in->i]);
		//printf("code (");
		//for (int8_t j = 0; j < 4; j++) printf("%lld, ", in->s[in->i+j]);
		//printf(") op: %lld, modes: ",  code.op);
		int64_t p[4];
		for (int8_t j = 0; j < SIZE[code.op]; j++)
			p[j] = code.md[j] ? (code.md[j] == 2 ? in->s[in->i+j+1]+rb : in->i+j+1) : in->s[in->i+j+1];
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
			default: printf("PANIC");
		}
		in->i += SIZE[code.op]+1;
	}
	in->run = 0;
	return;
}
_Bool input(Intcode* in, int64_t v){
	if (in->gotIn){
		puts("ERR");
		return 1;
	}
	in->gotIn = 1;
	in->in = v;
	return 0;
}
int64_t get(Intcode* in){
	if (!in->gotOut) return puts("ERRR");	//garbage
	in->gotOut = 0;
	return in->out;
}
int64_t push(Intcode* in, int64_t v){
	if (input(in,v)) return 0;	//garbage value
	return get(in);
}
int64_t next(Intcode* in){
	exec(in);
	return get(in);
}
Intcode* runtime(int64_t *s, uint32_t len){
	int64_t *cpy = malloc((len+1)*sizeof(int64_t));
	memcpy(cpy, s, sizeof(int64_t)*len+1);
	s[len] = '\0'; //in case
	Intcode *in = malloc(sizeof(Intcode));
	in->s = cpy;
	in->i = in->in = in->out = in->gotIn = in->gotOut = 0;
	in->run = in->shouldFree = 1;
	exec(in);
	return in;
}
void kill(Intcode* in){
	if (in->shouldFree) free(in->s);
	free(in);
}
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
