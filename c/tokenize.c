#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define KEY 0
#define SYM 1
#define NUM 2
#define INT_BUFF 10

const char* validKeys = "wasdlptecrg\nv^fmhxkuz";
const char* validSyms = ".?";

int isValidKey(char ch){
    for (int i=0;i<strlen(validKeys);i++){
        if (ch == validKeys[i]){
            return 1;
        }
    }
    return 0;
}

int isValidSym(char ch) {
    for (int i=0;i<strlen(validSyms);i++){
        if (ch == validSyms[i]){
            return 1;
        }
    }
    return 0;
}

Tile *tokenize(Tile *inst, char *fname){
    FILE* fp;
    char ch;

    Tile *ptr;
    inst = newTile();
    ptr = inst;

    char num[INT_BUFF], to_add[2];
    to_add[1] = '\0';


    fp = fopen(fname, "r");
    if ( fp ) {
        while ( (ch = fgetc(fp)) != EOF ) {
            //printf("%c",ch);
            if (!isdigit(ch)) {
                if (isValidKey(ch)) {
                    push(ptr->head, (int) ch);
                    push(ptr->head, KEY);
                    ptr = walk(ptr, 0);
                    // printf("%c",ch);
                } else if (isValidSym(ch)) {
                    push(ptr->head, (int) ch);
                    push(ptr->head, SYM);
                    ptr = walk(ptr, 0);
                    // printf("%c",ch);
                }
            } else if (isdigit(ch)) {
                memset(num,0,INT_BUFF);
                while (isdigit(ch)){
                    to_add[0] = ch;
                    strcat(num, to_add);
                    ch = fgetc(fp);
                }
                // printf("NUMER: %s\n", num);
                push(ptr->head, atoi(num));
                push(ptr->head, NUM);
                ptr = walk(ptr, 0);
                ungetc(ch, fp);
            }
        }
    }
    else {
         printf("File open errrorrs\n");
         exit(1);
    }
    //tileFree(inst);
    fclose (fp);
    return inst;
}


