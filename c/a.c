#include <stdio.h>
#define fuel(m)	(m/3-2)
#define NUMS	200	//increase if needed
int main(){
	FILE* f = fopen("i.1", "r");
	int sum = 0, arr[NUMS], max = 0;
	for (; EOF != fscanf(f, "%d\n", arr+max); max++)
		sum += (arr[max] = fuel(arr[max]));
	fclose(f);
	printf("%d\n", sum); //part 1

	_Bool cont = 0;
	do {
		cont = 0;
		for (int i = 0; i < max; i++){
			if (!arr[i]) continue; //minor speedup
			int new = fuel(arr[i]);
			if (new > 0){
				cont = 1;
				sum += (arr[i] = new);
			} else arr[i] = 0;
		}
	} while (cont);
	printf("%d\n", sum); //part 2
}
