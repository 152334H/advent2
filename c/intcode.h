#pragma once
#include <stdint.h>
#ifndef CODEMAX
#define	CODEMAX 1024
#endif
#define MAXARGS	3
typedef struct Opcode Opcode;
typedef struct Opcode {
	int8_t op; //op < 100
	int8_t md[MAXARGS];
} Opcode;
typedef struct Intcode {
	__int128_t *s;
	__int128_t in;
	__int128_t out;
	int32_t i; //max index should be containable in a 32 bit int
  int32_t rb;
	_Bool gotIn;
	_Bool gotOut;
	_Bool run;
	_Bool shouldFree;
	_Bool debug;
} Intcode;
Opcode instr(uint32_t n);
void exec(Intcode *in); //run Intcode until i/o request await
void kill(Intcode* in);	//free()s *in, and also in->s iff in->shouldFree is true
//_Bool functions will return 0 iff successful.
_Bool send(Intcode* in, __int128_t v);	//input() && exec(in)
_Bool input(Intcode* in, __int128_t v);	//modify in to have v queued as input value.
__int128_t get(Intcode* in);	//
__int128_t push(Intcode* in, __int128_t v);
__int128_t next(Intcode* in);
Intcode* instance(void);
Intcode* runtime(__int128_t *s, uint32_t len);
Intcode* phaseInit(__int128_t *s, uint32_t len, __int128_t v);
