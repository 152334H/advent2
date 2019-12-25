#include <stdio.h>
#include <string.h>
#include "tri.h"
/*
#define REQUIREHASH
#include "day.h"*/
#define MAXMOVE 512
#define is_y(c) (c-'x')
typedef struct path {
	int dist;
	int orig;
	_Bool pos;
	_Bool is_y;
} path;

int main(){
	int s[2][MAXMOVE][2], max[2];
	FILE *f = fopen("i.3", "r");
	for (int i = 0; i < 2; i++)
		for (max[i] = 0;;max[i]++){
			s[i][max[i]][1] = fgetc(f);
			fscanf(f, "%d", s[i][max[i]]);
			if (fgetc(f) != ',') break;
		}
	tPointi lines[2][MAXMOVE][2];
	tPointi cur;
	for (int i = 0; i < 2; i++)
		for (int j = 0;j < max[i];j++){
			_Bool dir = strchr("UD", s[i][j][1]);	//pos if y
			_Bool pos = strchr("UR", s[i][j][1]);
			PointAssign(*lines[i][j], cur);
			cur[dir] += *s[i][j];
			PointAssign(lines[i][j][1], cur);
			//printf("%c%d ", s[i][j][1], *s[i][j]);
		}
	int sect = 0;
	for (int i = 0; i < *max; i++)
		for (int j = 0; j < max[1]; j++)
			sect += Intersect(lines[0][i][0], lines[0][i][1], lines[1][j][0], lines[1][j][1]);
	printf("%d\n", sect);
}
//with open("i.3") as f: s = map(lambda s: map(lambda m: (int(m[1:])*(lambda c: -1 if c in "DL" else 1)(m[0]), m[0]), s.split(',')), f.read().split('\n')[:-1])
