#include <stdio.h>
#define LINEMAX 2048
#define LINELEN 8	//guaranteed to be 8 for day 6
#define D_HASH
#define H_MAX	1<<25
#define V_MAX	LINEMAX
#define BR_MAX	32
#include "day.h"
#undef REQUIRES_HASH
#define toInt(leaf)	((*s<<16)+(s[1]<<8)+*s)
#define getKid(ptr,i)	(ptr.kids[hash_get(ptr.kidNum, i)])
void addKid(Node* n, int v){
	if (n == NULL) {
		n = malloc(sizeof(Node));
		n->kids = calloc(BR_MAX, sizeof(Node*));
		n->kidNum = create_Hash(-1);
		n->max = BR_MAX;
		n->kidc = 0;
	}
	n->kids = 
	n->kidNum++;
typedef struct Node {
	Hash *kidNum;
	struct Node **kids;
	char kidc;
	short max;
} Node;
const char rootName[] = "COM";
const int rootHash = toInt(rootName);
int main(){
	FILE *f = fopen("i.6", "r");
	char s[LINELEN];
	int links[LINEMAX][2], linkc;
	for (linkc = 0; fgets(s, LINELEN, f); linkc++){
		if (*s == '\n'){
			linkc--;
			break;
		}
		links[linkc][0] = toInt(s);
		links[linkc][1] = toInt(s+4);
	}
	Node root = { .kidNum = create_Hash(-1), .kidc = 1, .kids = calloc(LINEMAX, sizeof(Node*)), .max = LINEMAX};
	safe_hash_push(root.kidNum, toInt(rootName));
	memset(root.kids, NULL, LINEMAX);
	root.kids[0] = calloc(1, sizeof(Node));

	Hash *seen = create_Hash(-1);
	while (seen->len < linkc){
		for (int i = 0; i < linkc; i++){
			if (hash_get(seen,*links[i]) == -1) continue;
			//loc
			Node* parent = getKid(root, *links[i]);
			parent->kidNum++;
			parent->
			safe_hash_push(seen, i);
		}
	}
}
