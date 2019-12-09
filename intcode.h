#pragma once
#include <stdint.h>
#ifndef CODEMAX
#define	CODEMAX 1024
#endif
#define MAXARGS	3
typedef struct Opcode Opcode;
typedef struct Opcode {
	int8_t op;
	int8_t md[MAXARGS];
} Opcode;
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
Opcode instr(int64_t n);
void exec(Intcode *in);
void kill(Intcode* in);
_Bool send(Intcode* in, int64_t v);
_Bool input(Intcode* in, int64_t v);
int64_t get(Intcode* in);
int64_t push(Intcode* in, int64_t v);
int64_t next(Intcode* in);
Intcode* runtime(int64_t *s, uint32_t len);
Intcode* phaseInit(int64_t *s, uint32_t len, int64_t v);
