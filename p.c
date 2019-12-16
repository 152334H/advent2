#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TEXTLEN 650 //requires manual checking
#define COPY    10000
#define useSAT(m,e) switch (m) {\
    case 1: sum += S[e]-S[start]; break;\
    case 3: sum += S[start]-S[e]; break;\
} //this directive exists to reduce retyping
char v[COPY*TEXTLEN]; /* v[] and o[] are both used to store the signal */
char o[COPY*TEXTLEN]; /* the 2nd one exists to store changes during a phase */
int _S[COPY*TEXTLEN+1]; //1D Summed Area Table
int *S = _S+1; //allows for indexing of -1
char *try(int length) {
    char *cur = v, *new = o; //v and o are swapped pointer-wise every iteration
    for (short p = 0; p < 100; p++) {
        //build SAT
        for (int i = 0; i < length; i++) S[i] = cur[i] + S[i-1];
        for (int i = 0; i < length; i++) { //runs 1 phase of FFT, storing result in new[]
            int sum = 0, start = i-1;
            char mode = 1; //start at mode 1 for simplicity
            for (int end = 2*i; end < length; end+=i+1, start+=i+1) {
                //for each iteration, if mode in [1,3], use values within (start, end]
                useSAT(mode++, end); //using mode++ for this macro is ok; mode++ is only cited once
                mode %= 4; //cycle mode around [0,1,0,-1]
            } //because the for() loop breaks when `end` overflows, a final addition is required
            useSAT(mode, length-1);
            new[i] = abs(sum%10);
        }
        char *tmp = new;
        new = cur, cur = tmp;
    }
    return cur;
}
int main() {
    //read from input
    FILE *f = fopen("i.16", "r");
    for (short i = 0; i < TEXTLEN; i++) v[i] = fgetc(f)-'0';
    fclose(f);
    //get offset
    int offset = 0;
    for (short i = 0; i < 7; offset*=10) offset+=v[i++];
    offset /= 10;
    //do part 1 and keep memory for part 2
    for (short i = 1; i < COPY; i++) memcpy(v+TEXTLEN*i, v, TEXTLEN);
    char *final = try(TEXTLEN);
    for (short i = 0; i < 8 || !putchar(10); i++) putchar('0'+final[i]);
    //reset memory to do part 2
    memcpy(v, v+TEXTLEN, TEXTLEN);
    final = try(COPY*TEXTLEN);
    for (short i = 0; i < 8 || !putchar(10); i++) putchar('0'+final[offset+i]);
}
