#include <stdio.h>
#include <stdint.h>
#define	CODEMAX 1024
#include "intcode.h"
__int128_t intcode[CODEMAX], max = 0, ans = 0;
void swap(uint8_t *a, uint8_t *b){
	uint8_t t = *a;
	*a = *b;
	*b = t;
}
void execPermutations(uint8_t *arr, uint8_t i, uint8_t len, void (*f)(uint8_t*)){
	if (len == i){
		f(arr);
		return;
	}
	for (uint8_t j = i; j < len; j++){
		swap(arr+i, arr+j);
		execPermutations(arr, i+1, len, f);
		swap(arr+i, arr+j);
	}
}
void run5(uint8_t *arr){
	Intcode *in[5] = {runtime(intcode, max), runtime(intcode, max), runtime(intcode, max), runtime(intcode, max), runtime(intcode, max)};
	for (uint8_t i = 0; i < 5; i++) send(in[i], arr[i]);
	_Bool cont = 1;
	int64_t rtr = 0;
	do	for (uint8_t i = 0; i < 5; i++)
			if (in[i]->run) rtr = push(in[i], rtr);
			else	cont = 0;
	while (cont); //this assumes that rtr is always increasing per cycle
	if (rtr > ans) ans = rtr;
	for (uint8_t i = 0; i < 5; i++) kill(in[i]);
}
int main(){
	FILE *f = fopen("i.7", "r");
	for (; EOF != fscanf(f, "%lld", intcode+max++); fgetc(f));
	uint8_t arr[2][5] = {{0,1,2,3,4}, {5,6,7,8,9}};
	for (int i = 0; i < 2; printf("part %d: %lld\n", ++i, ans))
		execPermutations(arr[i], 0, 5, run5);
}
