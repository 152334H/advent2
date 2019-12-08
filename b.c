#include <stdio.h>
#include <string.h>
#define	CODEMAX 1024
int main(){
	FILE *f = fopen("i.2", "r");
	int intcode[CODEMAX], max = 0;
	for (; EOF != fscanf(f, "%d", intcode+max++); fgetc(f));
	for (int n = 0; n < 100; n++)
		for (int v = 0; v < 100; v++){
			int s[max];
			memcpy(s, intcode, sizeof(int)*max);
			s[1] = n; s[2] = v;
			for (int i = 0; s[i] != 99; i+=4){
				switch(s[i]){
					case 1:
						s[s[i+3]] = s[s[i+1]] + s[s[i+2]];
						break;
					case 2:
						s[s[i+3]] = s[s[i+1]] * s[s[i+2]];
						break;
					default: printf("PANIC");
				}
			}
			if (n == 12 && v == 2) printf("part 1: %d\n", *s);
			if (*s == 19690720) printf("part 2: %d\n", n*100+v);
		}
}
