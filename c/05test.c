#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "stack.c"
#include "tile.c"

#define KEY 0
#define SYM 1
#define NUM 2
/*
 * lays the groundwork for parsing tokens using tiles
 * and stacks. Each tile is a token, and the stack
 * contains the information needed
 */

int main(void){
    Tile *origin = newTile();
    Tile *inst = newTile();
    Tile *next_i = inst;

    char *str = "wasd";
    for (int i=0; i<strlen(str);i++){
        push(next_i->head, (int) str[i]);
        push(next_i->head, KEY);
        next_i = walk(next_i, 2);
    }
    printf("\n");
    tileFree(origin);
    tileFree(inst);
    return 0;
}