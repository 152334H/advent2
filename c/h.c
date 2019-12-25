#include <stdio.h>
#include <string.h>
#define H 6
#define W 25
#define PX 150
#define MAX 128
#define ord(c)	(c-'0')
char pretty[] = {'.', '@', ' '};	//for printing part 2
int main(){
	FILE *f = fopen("i.8", "r");
	char s[MAX][PX+5], im[PX];
	memset(im, '2', PX);
	int layers;
	for (layers = 0; fgets(s[layers], PX+1, f); layers++);
	if (*s[layers-1] == '\n') layers--;

	int min0 = 999999999, a1;
	for (int l = 0; l < layers; l++){
		int c[3] = {0, 0, 0};
		for (int i = 0; i < PX; i++){
			if (im[i] == '2')	//part 1
				im[i] = s[l][i];
			c[ord(s[l][i])]++;	//part 2
		}
		if (min0 > *c){
			a1 = c[1]*c[2];
			min0 = *c;
		}
	}
	printf("%d\n", a1);
	for (int y = 0; y < H; y++, putchar(10))
		for (int x = 0; x < W; x++)
			putchar(pretty[ord(im[y*W +x])]);
}
