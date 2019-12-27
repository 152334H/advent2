#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef struct Pt {
  int x;
  int y;
} Pt;
Pt PointOf(int x, int y)
{
  return (Pt) { .x = x, .y = y };
}
_Bool PtEq(Pt p1, Pt p2)
{
  return p1.x == p2.x && p1.y == p2.y;
}
_Bool within(int x, int y)
{
  return x >= 0 && x < 5 && y >= 0 && y < 5;
}
int calc(_Bool *grid)
{
  int sum = 0;
  for (char i = 0; i < 25; i++) sum += grid[i]<<i;
  return sum;
}
_Bool hash[1<<26];
Pt *adj(int x, int y)
{
  Pt *rtr = calloc(4, sizeof(int64_t));
  if (!rtr) exit(1); //check
  Pt tmp[] = {PointOf(x, y+1),
              PointOf(x, y-1),
              PointOf(x+1, y),
              PointOf(x-1, y)};
  memcpy(rtr, tmp, sizeof(Pt)*4);
  return rtr;
}
void printGrid(_Bool* g)
{
  for (char y = 0; y < 5; y++, putchar(10))
    for (char x = 0; x < 5; x++)
      putchar(g[y*5+x]?'#':'.');
  putchar(10);
}
_Bool _grids[1024][32];
void modifyState(_Bool *grid)
{
  _Bool cpy[32];
  for (char i = 0; i < 25; i++) cpy[i] = grid[i];
  for (char i = 0; i < 25; i++) {
    char x = i%5, y = i/5;
    Pt *adj_ls = adj(x, y);
    char around = 0;
    for (char j = 0; j < 4; j++){
      Pt c = adj_ls[j];
      if (within(c.x, c.y) && cpy[c.y*5+c.x])
        around++;
    }
    free(adj_ls);
    if (!cpy[i] && around && around < 3)
      grid[i] = 1;
    if (cpy[i] && around != 1)
      grid[i] = 0;
  }
}
void modifyStates(_Bool (*g)[32], int dmi, int dma)
{
  dmi--, dma++;
  _Bool _cpy[dma-dmi][32];
  _Bool (*cpy)[32] = _cpy-dmi;
  for (int d = dmi; d < dma; d++) {
    for (char i = 0; i < 25; i++)
      cpy[d][i] = g[d][i];
  }
  for (int d = dmi+1; d < dma-1; d++)
    for (char i = 0; i < 25; i++) {
      char x = i%5, y = i/5;
      if (x == 2 && y == 2) continue;
      Pt *adj_ls = adj(x, y);
      char around = 0;
      for (char j = 0; j < 4; j++){
        Pt c = adj_ls[j];
        if (PtEq(c, PointOf(2,2))) {
          int xmi = 0, xma = 0, ymi = 0, yma = 0;
          if (y == 2) yma = 5;
          else  xma = 5;
          if (x == 1) xma = 1;
          else if (x == 3) xmi = 4, xma = 5;
          else if (y == 1) yma = 1;
          else if (y == 3) ymi = 4, yma = 5;
          for (char Y = ymi; Y < yma; Y++)
            for (char X = xmi; X < xma; X++)
              around += cpy[d+1][Y*5+X];
        } else if (within(c.x, c.y)) around += cpy[d][c.y*5+c.x];
        else {
          char X = 2, Y = 2;
          if (c.x == -1) X = 1;
          else if (c.x == 5) X = 3;
          else if (c.y == -1) Y = 1;
          else if (c.y == 5) Y = 3;
          if (c.x != 2 || c.y != 2) around += cpy[d-1][Y*5+X];
        }
      }
      if (!cpy[d][i] && around && around < 3) g[d][i] = 1;
      else if (cpy[d][i] && around != 1) g[d][i] = 0;
      free(adj_ls);
    }
}
int main()
{
  FILE *f = fopen("i.24", "r");
  char s[6][6];
  for (char i = 0; i < 5; i++) fgets(s[i], 7, f);
  _Bool grid[32];
  for (char y = 0; y < 5; y++)
    for (char x = 0; x < 5; x++)
      grid[5*y+x] = s[y][x] == '#';
  int v;
  while (!hash[v = calc(grid)]) {
    hash[v] = 1;
    modifyState(grid);
  }
  printf("%d\n", v);
  //part 2
  _Bool (*grids)[32] = _grids+512;
  for (char y = 0; y < 5; y++)
    for (char x = 0; x < 5; x++)
      grids[0][5*y+x] = s[y][x] == '#';
  int mi = 0, ma = 1;
  for (int i = 0; i < 200; i++) {
    if (i%2 == 0) mi--, ma++;
    modifyStates(grids, mi, ma);
  }
  int total = 0;
  for (int i = mi; i < ma; i++)
    for (char j = 0; j < 25; j++)
      total += grids[i][j];
  printf("%d\n", total);
}
